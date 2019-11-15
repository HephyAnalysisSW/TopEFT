''' Class to interpret string based cuts
'''

import logging
logger = logging.getLogger(__name__)

jetSelection    = "njet"
bJetSelectionM  = "nBTag"

mIsoWP = { "VT":5, "T":4, "M":3 , "L":2 , "VL":1, 0:"None" }

special_cuts = {
    #"looseLeptonVeto":   "Sum$(lep_pt>15&&lep_relIso03<0.4)==2",
    "dilep":             "nLeptons_tight_SS==2",
    "SSdilep":           "nlep==2&&(lep_pdgId[0]*lep_pdgId[1])>0",
#    "lepSelTTW":         "lep_pt[1]>25&&(
    "dilepOFOS":         "nGoodElectrons==1&&nGoodMuons==1&&nlep==2&&(lep_pdgId[0]*lep_pdgId[1])<0",
    "dilepOS":           "nlep==2&&(lep_pdgId[0]*lep_pdgId[1])<0",
    "dilepSFOS":         "(nGoodElectrons==2||nGoodMuons==2)&&nlep==2&&(lep_pdgId[0]*lep_pdgId[1])<0",
    "trilep":            "nLeptons_tight_3l==3&&!(nLeptons_tight_4l>=4)",
    "trilepFO":          "nLeptons_FO_3l>=3&&!(nLeptons_tight_3l==3)&&!(nLeptons_tight_4l>=4)",
    "looseVetoDL":       "nlep==2",
    "looseVeto":         "nlep==3",
    "WlepPt20":          "lep_pt[nonZ_l1_index]>20",
    "quadlep":           "nLeptons_tight_4l>=4&&min_dl_mass>12&&totalLeptonCharge==0",
    "quadlepTWZ":        "nLeptons_tight_4l>=4",
    "trilepTTWW":        "nLeptons_tight_4l>=3",
    "Zcand":             "Z_mass>0",
#    "lepSelTTZ":         "lep_pt[0]>40&&lep_pt[1]>20&&lep_pt[2]>10",
    "lepSelTTZ":         "Sum$(lep_pt>40&&lep_tight_3l>0)>0 && Sum$(lep_pt>20&&lep_tight_3l>0)>1 && Sum$(lep_pt>10&&lep_tight_3l>0)>2",
#    "lepSelTTZ":         "Sum$(lep_pt>40&&lep_tight>0&&(abs(lep_pdgId)==11||(abs(lep_pdgId)==13&&lep_mediumMuonId)))>0 && Sum$(lep_pt>20&&lep_tight>0&&(abs(lep_pdgId)==11||(abs(lep_pdgId)==13&&lep_mediumMuonId)))>1 && Sum$(lep_pt>10&&lep_tight>0&&(abs(lep_pdgId)==11||(abs(lep_pdgId)==13&&lep_mediumMuonId)))>2",
    "lepSelTTG2l":       "lep_pt[0]>40&&lep_pt[1]>20",
    "lepSelTTG1l":       "lep_pt[0]>20",
    "lepSelQuad":        "Sum$(lep_pt>40&&lep_tight_4l>0)>0 && Sum$(lep_pt>10&&lep_tight_4l>0)>3 ",
    "lepSelQuadSUSY":    "Sum$(lep_pt>25&&lep_tight_4l>0)>0&&Sum$(lep_pt>20&&lep_tight_4l>0)>3 ",
    "lepSel":            "nlep==3&&lep_pt[0]>40&&lep_pt[1]>20&&lep_pt[2]>10&&Z_mass>0",
    "lepSelDY":          "lep_pt[0]>40&&lep_pt[1]>20",
    "lepSelDilepSUSY":   "Sum$(lep_pt>25&&lep_tight_4l>0)>1",# && Sum$(lep_pt>10&&lep_tight_4l>0)>1 ",
    "onZ":               "abs(Z_mass-91.1876)<10",
    "noZ12":             "((!(abs(Z1_mass_4l-91.2)<20))||(!(abs(Z2_mass_4l-91.2)<20)))",
    "noZ2":              "(!(abs(Z2_mass_4l-91.2)<20))",
    "tightZ":            "Z_fromTight>0",
    "onZZ":              "abs(Z1_mass_4l-91.1876)<20&&abs(Z2_mass_4l-91.1876)<20",
    "onZ1":              "abs(Z1_mass_4l-91.1876)<20",
    "offZ2":             "(1)",# taken care off in plot script. Think of something better! "abs(Z2_mass_4l-91.1876)>20",
    "offZ2met":          "(1)",# taken care off in plot script. Think of something better! "abs(Z2_mass_4l-91.1876)>20",
    "onZloose":          "abs(Z_mass-91.1876)<15",
    "offZ":              "abs(Z_mass-91.1876)>10",
    "offZSF":            "(abs(Z_mass-91.1876)>10&&(nGoodElectrons==2||nGoodMuons==2))||(nGoodElectrons!=2&&nGoodMuons!=2)",#cut Z-Window only for SF dilep events, only usable for nlep==2 (I guess)
  }

continous_variables = [ ("metSig", "metSig"), ("mll", "Z_mass"), ("met", "met_pt"), ("mt2ll", "dl_mt2ll"), ("mt2blbl", "dl_mt2blbl"), ("htCMG", "htJet40j"), ("photon","photon_pt"), ("ZlldPhi","Z_lldPhi"), ("Zpt","Z_pt"), ("min_mll", "min_dl_mass")]
discrete_variables  = [ ("njet", "nJetSelected"), ("btag", "nBTag") , ("nlep","nlep") ]

class cutInterpreter:
    ''' Translate var100to200-var2p etc.
    '''

    @staticmethod
    def translate_cut_to_string( string ):

        # special cuts
        if string in special_cuts.keys(): return special_cuts[string]

        # continous Variables
        for var, tree_var in continous_variables:
            if string.startswith( var ):
                num_str = string[len( var ):].replace("to","To").split("To")
                upper = None
                lower = None
                if len(num_str)==2:
                    lower, upper = num_str
                elif len(num_str)==1:
                    lower = num_str[0]
                else:
                    raise ValueError( "Can't interpret string %s" % string )
                res_string = []
                if lower: res_string.append( tree_var+">="+lower )
                if upper: res_string.append( tree_var+"<"+upper )
                return "&&".join( res_string )

        # discrete Variables
        for var, tree_var in discrete_variables:
            logger.debug("Reading discrete cut %s as %s"%(var, tree_var))
            if string.startswith( var ):
                # So far no njet2To5
                if string[len( var ):].replace("to","To").count("To"):
                    raise NotImplementedError( "Can't interpret string with 'to' for discrete variable: %s. You just volunteered." % string )

                num_str = string[len( var ):]
                # logger.debug("Num string is %s"%(num_str))
                # var1p -> tree_var >= 1
                if num_str[-1] == 'p' and len(num_str)==2:
                    # logger.debug("Using cut string %s"%(tree_var+">="+num_str[0]))
                    return tree_var+">="+num_str[0]
                # var123->tree_var==1||tree_var==2||tree_var==3
                else:
                    vls = [ tree_var+"=="+c for c in num_str ]
                    if len(vls)==1:
                      # logger.debug("Using cut string %s"%vls[0])
                      return vls[0]
                    else:
                      # logger.debug("Using cut string %s"%'('+'||'.join(vls)+')')
                      return '('+'||'.join(vls)+')'
        raise ValueError( "Can't interpret string %s. All cuts %s" % (string,  ", ".join( [ c[0] for c in continous_variables + discrete_variables] +  special_cuts.keys() ) ) )

    @staticmethod
    def cutString( cut, select = [""], ignore = [], photonEstimated=False):
        ''' Cutstring syntax: cut1-cut2-cut3
        '''
        cuts = cut.split('-')
        # require selected
        cuts = filter( lambda c: any( sel in c for sel in select ), cuts )
        # ignore
        cuts = filter( lambda c: not any( ign in c for ign in ignore ), cuts )

        cutString = "&&".join( map( cutInterpreter.translate_cut_to_string, cuts ) )

        if photonEstimated:
          for var in ['met_pt','met_phi','metSig','dl_mt2ll','dl_mt2bb']:
            cutString = cutString.replace(var, var + '_photonEstimated')

        return cutString
    
    @staticmethod
    def cutList ( cut, select = [""], ignore = []):
        ''' Cutstring syntax: cut1-cut2-cut3
        '''
        cuts = cut.split('-')
        # require selected
        cuts = filter( lambda c: any( sel in c for sel in select ), cuts )
        # ignore
        cuts = filter( lambda c: not any( ign in c for ign in ignore ), cuts )
        return [ cutInterpreter.translate_cut_to_string(cut) for cut in cuts ] 
        #return  "&&".join( map( cutInterpreter.translate_cut_to_string, cuts ) )

if __name__ == "__main__":
    print cutInterpreter.cutString("lepSel-njet3p-btag1p-Zpt100")
    print cutInterpreter.cutList("lepSel-njet3p-btag1p-ZptTo100")
