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

def ZPolarisationFit( shape, isData, var_name, fit_plot_directory, fit_filename = None):
    ''' Polarisation fit for Z
    '''

    logger.info( "Performing Z polarisation fit" )
    # declare the observable mean, and import the histogram to a RooDataHist
    pol_var     = ROOT.RooRealVar(var_name, var_name,-1,1) ;
    dh          = ROOT.RooDataHist("datahistshape","datahistshape",ROOT.RooArgList(pol_var),ROOT.RooFit.Import(shape)) ;
    
    # plot the data hist with error from sum of weighted events
    frame       = pol_var.frame(ROOT.RooFit.Title(var_name))
    if isData:
        logger.debug( "Settings for data with Poisson error bars" )
        dh.plotOn(frame,ROOT.RooFit.DataError(ROOT.RooAbsData.Poisson))
    else:
        logger.debug( "Settings for mc with SumW2 error bars" )
        dh.plotOn(frame,ROOT.RooFit.DataError(ROOT.RooAbsData.SumW2)) ;

    # create polarisation PDFs
    Z_pol_p     = ROOT.RooGenericPdf("Z_pol_p","Z_pol_p", "1+@0**2-0.437825*@0", ROOT.RooArgList(pol_var)) 
    Z_mol_m     = ROOT.RooGenericPdf("Z_mol_m","Z_mol_m", "1+@0**2+0.437825*@0", ROOT.RooArgList(pol_var)) 
    Z_mol_L     = ROOT.RooGenericPdf("Z_mol_L","Z_mol_L", "1-@0**2", ROOT.RooArgList(pol_var)) 

    Z_pol_p_frac= ROOT.RooRealVar("Z_pol_p_frac","Z_pol_p_frac",0.333,0,1)
    Z_mol_m_frac= ROOT.RooRealVar("Z_mol_m_frac","Z_mol_m_frac",0.333,0,1)

    Z_pol_Pdf   = ROOT.RooAddPdf("Z_pol_Pdf","Z_pol_Pdf",ROOT.RooArgList(Z_pol_p, Z_mol_m, Z_mol_L), ROOT.RooArgList(Z_pol_p_frac, Z_mol_m_frac)) 
    
    # now do the fit and extract the parameters with the correct error
    if isData: 
        Z_pol_Pdf.fitTo(dh, ROOT.RooFit.Save(),                             )# ROOT.RooFit.Range(dh.mean(pol_var)-2*dh.sigma(pol_var),dh.mean(pol_var)+2*dh.sigma(pol_var)))
    else:
        Z_pol_Pdf.fitTo(dh, ROOT.RooFit.Save(), ROOT.RooFit.SumW2Error(True))#,ROOT.RooFit.Range(dh.mean(pol_var)-2*dh.sigma(pol_var),dh.mean(pol_var)+2*dh.sigma(pol_var)))

    Z_pol_Pdf.plotOn(frame)
    Z_pol_Pdf.plotOn(frame, ROOT.RooFit.Components("Z_pol_p"), ROOT.RooFit.LineStyle(ROOT.kDashed), ROOT.RooFit.LineColor(ROOT.kRed) )
    Z_pol_Pdf.plotOn(frame, ROOT.RooFit.Components("Z_mol_m"), ROOT.RooFit.LineStyle(ROOT.kDashed), ROOT.RooFit.LineColor(ROOT.kGreen) )
    Z_pol_Pdf.plotOn(frame, ROOT.RooFit.Components("Z_mol_L"), ROOT.RooFit.LineStyle(ROOT.kDashed), ROOT.RooFit.LineColor(ROOT.kMagenta) )

    argset_fit = ROOT.RooArgSet(Z_pol_p_frac,Z_mol_m_frac)
    Z_pol_Pdf.paramOn(frame,ROOT.RooFit.Format("NELU",ROOT.RooFit.AutoPrecision(1)),ROOT.RooFit.Layout(0.55)) 
    frame.SetMaximum(frame.GetMaximum()*1.2)

    # add chi2 info
    chi2_text = ROOT.TPaveText(0.3,0.8,0.4,0.9,"BRNDC")
    chi2_text.AddText("#chi^{2} fit = %s" %round(frame.chiSquare(6),2))
    chi2_text.SetTextSize(0.04)
    chi2_text.SetTextColor(2)
    chi2_text.SetShadowColor(0)
    chi2_text.SetFillColor(0)
    chi2_text.SetLineColor(0)
    frame.addObject(chi2_text)

    if fit_filename is not None:
        c = ROOT.TCanvas()
        frame.Draw()
        if not os.path.exists(fit_plot_directory): os.makedirs(fit_plot_directory)
        # c.SaveAs(os.path.join( fit_plot_directory, fit_filename+".pdf"))
        c.SaveAs(os.path.join( fit_plot_directory, fit_filename+".png"))
        del c

    return Z_pol_p_frac.getVal(), Z_mol_m_frac.getVal(), 1-Z_pol_p_frac.getVal()-Z_mol_m_frac.getVal()  
