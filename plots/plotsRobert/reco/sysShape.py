# Standard imports
import uuid
from math import sqrt

import ROOT

from RootTools.core.standard import *

def getTheorySysFromChain( chain, variable, binning, selectionString, weightString ):

    name = 'h1D_'+uuid.uuid4().hex 
    htmp_original = ROOT.TH1D(name, name, *binning )
    chain.Draw("{var}>>{name}".format(var=variable, name=name), "({selectionString})*({weightString})".format(selectionString=selectionString, weightString=weightString), 'goff')

    name = 'h2D_'+uuid.uuid4().hex 
    htmp_2D = ROOT.TH2D(name, name, *(binning+[111,0,111]) )
    chain.Draw("Iteration$:{var}>>{name}".format(var=variable, name=name), "({selectionString})*({weightString})*LHEweight_wgt/LHEweight_original".format(selectionString=selectionString, weightString=weightString), 'goff')


    n_scale = [0,1,2,3,4,6,8]
    n_pdf   = [9 + i for i in range(100)]
    scale_rel_unc = htmp_original.Clone()
    scale_rel_unc.Reset()
    pdf_rel_unc = htmp_original.Clone()
    pdf_rel_unc.Reset()

    for iBin_x in range(1, 1+htmp_original.GetNbinsX()):
        val = htmp_original.GetBinContent(iBin_x)

        scale_variations  = [  htmp_2D.GetBinContent( htmp_2D.FindBin( htmp_original.GetBinCenter(iBin_x), i_scale) ) for i_scale in n_scale ]
        scale_unc = max(abs(val-variation) for variation in scale_variations)

        pdf_variations  = [  htmp_2D.GetBinContent( htmp_2D.FindBin( htmp_original.GetBinCenter(iBin_x), i_pdf) ) for i_pdf in n_pdf ]
        pdf_rms_unc     = sqrt( 1./len(n_pdf)*sum([ ( val - var) **2 for var in pdf_variations ] ) )

        if val>0: 
            scale_rel_unc.SetBinContent(iBin_x, scale_unc/val )
            pdf_rel_unc.SetBinContent(iBin_x, pdf_rms_unc/val )

    return {'h_pdf_rel_unc':pdf_rel_unc, 'h_scale_rel_unc':scale_rel_unc, 'h_nominal':htmp_original, 'h_2D':htmp_2D}

def add_histos_quadrature( histos ):

    res = histos[0].Clone()

    for histo in histos[1:]:
        if not histo.GetNbinsX() == res.GetNbinsX():
            raise ValueError

        for i_binx in range( 0, 1+histo.GetNbinsX() ):
            res.SetBinContent( i_binx, sqrt( res.GetBinContent( i_binx )**2 + histo.GetBinContent( i_binx )**2 ) )

    return res 
                

def getBoxes( histo, rel_uncertainty_histos, min_y = None, max_y = None):

    result = []
    for i_h, h in enumerate(rel_uncertainty_histos):
        if not histo.GetNbinsX() == h.GetNbinsX():
            raise ValueError
        h_err = add_histos_quadrature( rel_uncertainty_histos[:i_h+1] )
        boxes = []
        for i_binx in range( 1, 1+histo.GetNbinsX() ):
            central = histo.GetBinContent(i_binx)
            relerr  = h_err.GetBinContent(i_binx)
            if relerr>0:
                y_high = central*(1+relerr)
                y_low = central*(1-relerr)
                if max_y is not None:
                    if y_high > max_y: y_high = max_y
                    if y_low > max_y: continue
                if min_y is not None:
                    if y_low < min_y: y_low = min_y
                    if y_high < min_y: continue
                
                boxes.append( ROOT.TBox(h_err.GetBinLowEdge(i_binx), central*(1-relerr), h_err.GetBinLowEdge(i_binx)+h_err.GetBinWidth(i_binx), central*(1+relerr) ) )

        result.append( boxes )

    return result

if __name__=='__main__':

    from TopEFT.samples.cmgTuples_Summer16_mAODv2_postProcessed import * 
    from TopEFT.samples.cmgTuples_signals_Summer16_mAODv2_postProcessed import *
    from TopEFT.Tools.cutInterpreter  import cutInterpreter

    selection = "nGoodMuons+nGoodElectrons==3&&"+cutInterpreter.cutString("lepSelTTZ-njet3p-btag1p-onZ")
    #weightString = "(1)"
    weightString = "weight*36.9"
    binning = [3,0,600]

    bsm = getTheorySysFromChain( ewkDM_ttZ_ll_DC2A_0p20_DC2V_0p20.chain, 'Z_pt', binning, selection, weightString )
    res = getTheorySysFromChain( TTZtoLLNuNu.chain, 'Z_pt', binning, selection, weightString )

    bsm['h_nominal'].Scale( res['h_nominal'].Integral() / bsm['h_nominal'].Integral())

    #c1 = ROOT.TCanvas()

    #res['h_nominal'].Draw()
    res['h_nominal'].SetTitle("")
    res['h_nominal'].GetYaxis().SetRangeUser(0, 1.3*max([ res['h_nominal'].GetMaximum(), bsm['h_nominal'].GetMaximum()] ) )

    all_boxes = getBoxes( res['h_nominal'], [ res['h_pdf_rel_unc'], res['h_scale_rel_unc'] ])
    #all_boxes += getBoxes( bsm['h_nominal'], [ bsm['h_pdf_rel_unc'], bsm['h_scale_rel_unc'] ])

    colors = [ ROOT.kRed, ROOT.kBlue, ROOT.kRed, ROOT.kGreen ]

    for i, boxes in enumerate( reversed( all_boxes ) ):

        for box in boxes:
            box.SetFillColor( colors[i] )
            box.SetFillStyle( 3004 )
            #box.Draw()

    all_boxes.reverse()

    #res['h_nominal'].Draw('same')
    res['h_nominal'].style = styles.lineStyle( ROOT.kBlue)
    bsm['h_nominal'].style = styles.lineStyle( ROOT.kBlack  , errors = True)
    
    bsm['h_nominal'].legendText = "C_{2A}=C_{2V}=0.2"
    res['h_nominal'].legendText = "SM"

    #c1.SetLogy()
    #c1.Print('/afs/hephy.at/user/r/rschoefbeck/www/etc/test2.png')   
    plot = Plot.fromHisto(name = "pTZ_unc", histos = [[ res['h_nominal'] ], [bsm['h_nominal']]], texX = "p_{T}(Z)", texY = "Events" )  
    plotting.draw(plot, plot_directory = "/afs/hephy.at/user/r/rschoefbeck/www/topEFT/gen/", logX = False, logY = False, sorting = False, drawObjects = sum( all_boxes, [])) 
