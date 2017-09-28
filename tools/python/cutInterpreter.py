''' Class to interpret string based cuts
'''

import logging
logger = logging.getLogger(__name__)

jetSelection    = "nJetGood"
bJetSelectionM  = "nBTag"

mIsoWP = { "VT":5, "T":4, "M":3 , "L":2 , "VL":1, 0:"None" }

special_cuts = {
    # ("multiIsoVT":        "(1)", 
    "looseLeptonVeto":   "Sum$(LepGood_pt>15&&LepGood_relIso03<0.4)==2",

    "lepSel":            "l1_pt>40&&l2_pt>20&&l3_pt>10&&isTTZcand&&mlmZ_mass>0",
    "allZ":              "(1)",
    "onZ":               "abs(dl_mass-91.1876)<15",
    "offZ":              "abs(dl_mass-91.1876)>15",
    "llgNoZ":            "(abs(dlg_mass-91.1876)>15||isEMu)",

    "gLepdR":            "(1)",
    "gJetdR":            "(1)",
   
    "dPhiJet0":          "Sum$( ( cos(met_phi-JetGood_phi)>0.8 )*(Iteration$==0) )==0",
    "dPhiJet1":          "Sum$( ( cos(met_phi-JetGood_phi)>cos(0.25) )*(Iteration$<2) )==0",
    "dPhiInv":           '(!(cos(met_phi-JetGood_phi[0])<0.8&&cos(met_phi-JetGood_phi[1])<cos(0.25)))', # here we want an njet requirement
    "metInv":            "met_pt<80",
    "metSigInv":         "metSig<5",

    "extraLepVeto":      "Sum$(abs(LepGood_pdgId)==13&&LepGood_pt>20&&( abs(LepGood_dz)>0.2 || abs(LepGood_dxy)>0.2 ) ) + Sum$(abs(LepOther_pdgId)==13&&LepOther_pt>20&&( abs(LepOther_dz)>0.2 || abs(LepOther_dxy)>0.2 ) )==0",

  }

continous_variables = [ ("metSig", "metSig"), ("mll", "dl_mass"), ("met", "met_pt"), ("mt2ll", "dl_mt2ll"), ("mt2blbl", "dl_mt2blbl"), ("htCMG", "htJet40j"), ("photon","photon_pt") ]
discrete_variables  = [ ("njet", "nJetGood"), ("btag", "nBTag") , ("nCMGjet", "nJet30")]

class cutInterpreter:
    ''' Translate var100to200-var2p etc.
    '''

    @staticmethod
    def translate_cut_to_string( string ):

        if string.startswith("multiIso"):
            str_ = mIsoWP[ string.replace('multiIso','') ]
            return "l1_mIsoWP>%i&&l2_mIsoWP>%i" % (str_, str_)
        elif string.startswith("relIso"):
           iso = float( string.replace('relIso','') )
           return "l1_relIso03<%3.2f&&l2_relIso03<%3.2f"%( iso, iso )
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
    print cutInterpreter.cutString("njet2-btag0p-multiIsoVT-relIso0.12-looseLeptonVeto-mll20-onZ-met80-metSig5-dPhiJet0-dPhiJet1-mt2ll100")
    print
    print cutInterpreter.cutList("njet2-btag0p-multiIsoVT-relIso0.12-looseLeptonVeto-mll20-onZ-met80-metSig5-dPhiJet0-dPhiJet1-mt2ll100")
