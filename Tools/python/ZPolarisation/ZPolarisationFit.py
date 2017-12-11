# Standard importts
import os
import ROOT
ROOT.gROOT.SetBatch(True)

# RooFit
ROOT.gSystem.Load("libRooFit.so")
ROOT.gSystem.Load("libRooFitCore.so")
ROOT.gROOT.SetStyle("Plain") # Not sure this is needed
ROOT.gSystem.SetIncludePath( "-I$ROOFITSYS/include/" )

# Logging
import logging
logger = logging.getLogger(__name__)

def ZPolarisationFit( shape, pol_histos=None, sumW2Error = True, fit_plot_directory=None, fit_filename = None):
    ''' Polarisation fit for Z
    '''

    logger.info( "Performing Z polarisation fit" )
    var_name = "cosThetaStar"
    # declare the observable mean, and import the histogram to a RooDataHist
    pol_var     = ROOT.RooRealVar(var_name, var_name,-1,1) ;
    dh          = ROOT.RooDataHist("datahistshape","datahistshape",ROOT.RooArgList(pol_var),ROOT.RooFit.Import(shape)) ;
    
    # plot the data hist with error from sum of weighted events
    frame       = pol_var.frame(ROOT.RooFit.Title(var_name))
    if not sumW2Error:
        logger.debug( "Settings for data with Poisson error bars" )
        dh.plotOn(frame,ROOT.RooFit.DataError(ROOT.RooAbsData.Poisson))
    else:
        logger.debug( "Settings for mc with SumW2 error bars" )
        dh.plotOn(frame,ROOT.RooFit.DataError(ROOT.RooAbsData.SumW2)) ;

    # create polarisation PDFs
    if pol_histos is None:
        Z_pol_p     = ROOT.RooGenericPdf("Z_pol_p","Z_pol_p", "1+@0**2-0.437825*@0", ROOT.RooArgList(pol_var)) 
        Z_mol_m     = ROOT.RooGenericPdf("Z_mol_m","Z_mol_m", "1+@0**2+0.437825*@0", ROOT.RooArgList(pol_var)) 
        Z_mol_L     = ROOT.RooGenericPdf("Z_mol_L","Z_mol_L", "1-@0**2", ROOT.RooArgList(pol_var))
    else: 
        dh_p = ROOT.RooDataHist('dh_p','dh_p', ROOT.RooArgList(pol_var),ROOT.RooFit.Import(pol_histos[0]))
        dh_m = ROOT.RooDataHist('dh_m','dh_m', ROOT.RooArgList(pol_var),ROOT.RooFit.Import(pol_histos[1]))
        dh_L = ROOT.RooDataHist('dh_L','dh_L', ROOT.RooArgList(pol_var),ROOT.RooFit.Import(pol_histos[2]))
        Z_pol_p     = ROOT.RooHistPdf("Z_pol_p","Z_pol_p", ROOT.RooArgSet(pol_var), dh_p) 
        Z_mol_m     = ROOT.RooHistPdf("Z_mol_m","Z_mol_m", ROOT.RooArgSet(pol_var), dh_m)
        Z_mol_L     = ROOT.RooHistPdf("Z_mol_L","Z_mol_L", ROOT.RooArgSet(pol_var), dh_L)

    Z_pol_p_yield= ROOT.RooRealVar("Z_pol_p_yield","Z_pol_p_yield",10,0,10000)
    Z_mol_m_yield= ROOT.RooRealVar("Z_mol_m_yield","Z_mol_m_yield",10,0,10000)
    Z_mol_L_yield= ROOT.RooRealVar("Z_mol_L_yield","Z_mol_L_yield",100,0,10000)

    Z_pol_Pdf   = ROOT.RooAddPdf("Z_pol_Pdf","Z_pol_Pdf",ROOT.RooArgList(Z_pol_p, Z_mol_m, Z_mol_L), ROOT.RooArgList(Z_pol_p_yield, Z_mol_m_yield, Z_mol_L_yield )) 
    
    # now do the fit and extract the parameters with the correct error
    Z_pol_Pdf.fitTo(dh, ROOT.RooFit.Save(), ROOT.RooFit.SumW2Error(sumW2Error), ROOT.RooFit.Extended())#,ROOT.RooFit.Range(dh.mean(pol_var)-2*dh.sigma(pol_var),dh.mean(pol_var)+2*dh.sigma(pol_var)))

    Z_pol_Pdf.plotOn(frame)
    Z_pol_Pdf.plotOn(frame, ROOT.RooFit.Components("Z_pol_p"), ROOT.RooFit.LineStyle(ROOT.kDashed), ROOT.RooFit.LineColor(ROOT.kRed) )
    Z_pol_Pdf.plotOn(frame, ROOT.RooFit.Components("Z_mol_m"), ROOT.RooFit.LineStyle(ROOT.kDashed), ROOT.RooFit.LineColor(ROOT.kGreen) )
    Z_pol_Pdf.plotOn(frame, ROOT.RooFit.Components("Z_mol_L"), ROOT.RooFit.LineStyle(ROOT.kDashed), ROOT.RooFit.LineColor(ROOT.kMagenta) )

    argset_fit = ROOT.RooArgSet(Z_pol_p_yield,Z_mol_m_yield, Z_mol_L_yield)
    Z_pol_Pdf.paramOn(frame,ROOT.RooFit.Format("NELU",ROOT.RooFit.AutoPrecision(1)),ROOT.RooFit.Layout(0.55)) 
    frame.SetMaximum(frame.GetMaximum()*1.2)

    ## add chi2 info
    #chi2_text = ROOT.TPaveText(0.3,0.8,0.4,0.9,"BRNDC")
    #chi2_text.AddText("#chi^{2} fit = %s" %round(frame.chiSquare(6),2))
    #chi2_text.SetTextSize(0.04)
    #chi2_text.SetTextColor(2)
    #chi2_text.SetShadowColor(0)
    #chi2_text.SetFillColor(0)
    #chi2_text.SetLineColor(0)
    #frame.addObject(chi2_text)

    if fit_filename is not None:
        c = ROOT.TCanvas()
        frame.Draw()
        if not os.path.exists(fit_plot_directory): os.makedirs(fit_plot_directory)
        # c.SaveAs(os.path.join( fit_plot_directory, fit_filename+".pdf"))
        c.SaveAs(os.path.join( fit_plot_directory, fit_filename+".png"))
        del c

    return ( Z_pol_p_yield.getVal(), Z_pol_p_yield.getError()), ( Z_mol_m_yield.getVal(), Z_mol_m_yield.getError()) , ( Z_mol_L_yield.getVal(), Z_mol_L_yield.getError() )
