''' Class to interpret string based cuts
'''

import logging
logger = logging.getLogger(__name__)

jetSelection    = "njet"
bJetSelectionM  = "nBTag"

mIsoWP = { "VT":5, "T":4, "M":3 , "L":2 , "VL":1, 0:"None" }

special_cuts = {
    #"looseLeptonVeto":   "Sum$(lep_pt>15&&lep_relIso03<0.4)==2",
    "dilep":             "nlep==2",
    "SSdilep":           "nlep==2&&(lep_pdgId[0]*lep_pdgId[1])>0",
#    "lepSelTTW":         "lep_pt[1]>25&&(
    "dilepOFOS":         "nGoodElectrons==1&&nGoodMuons==1&&nlep==2&&(lep_pdgId[0]*lep_pdgId[1])<0",
    "dilepOS":           "nlep>=2&&(lep_pdgId[0]*lep_pdgId[1])<0",
    "trilep":            "nlep==3",
    "quadlep":           "nlep==4",
    "Zcand":             "Z_mass>0",
    "lepSelTTZ":         "lep_pt[0]>40&&lep_pt[1]>20&&lep_pt[2]>10",
    "lepSelTTZ4l":       "lep_pt[0]>40&&lep_pt[1]>20&&lep_pt[2]>10&&lep_pt[3]>10",
    "lepSel":            "nlep==3&&lep_pt[0]>40&&lep_pt[1]>20&&lep_pt[2]>10&&Z_mass>0",
    "onZ":               "abs(Z_mass-91.2)<10",
    "offZ":              "abs(Z_mass-91.2)>10",
  }

continous_variables = [ ("metSig", "metSig"), ("mll", "Z_mass"), ("met", "met_pt"), ("mt2ll", "dl_mt2ll"), ("mt2blbl", "dl_mt2blbl"), ("htCMG", "htJet40j"), ("photon","photon_pt"), ("ZlldPhi","Z_lldPhi"), ("Zpt","Z_pt") ]
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
    print cutInterpreter.cutString("lepSel-njet3p-btag1p")
