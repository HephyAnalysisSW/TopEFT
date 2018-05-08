''' Helper functions for syncing
'''
#Standard imports
import ROOT

# Logging
import logging
logger = logging.getLogger(__name__)

def print_header( run, lumi, event ):
    logger.sync( "####### %i/%i/%i ######## "%( run, lumi, event ) )

def print_met( met_pt, met_phi ):
    logger.sync( "MET pt/phi %7.3f/%+3.2f"%( met_pt, met_phi ) )

def print_jets( jets ):
    for i_jet, jet in enumerate( jets ):
        logger.sync( "jet %2i id %i pt/eta/phi %7.3f/%+3.2f/%+3.2f deepCSV %+7.6f"%( i_jet, jet['id'], jet['pt'], jet['eta'], jet['phi'], jet['btagDeepCSV'] ) )

def print_leptons( leps ):
    for i_lep, lep in enumerate( leps ):
        logger.sync( "lepton %2i pdgId %+2i tight %i pt/eta/phi %7.3f/%+3.2f/%+3.2f MVA %+7.6f muTrackRelErr %3.4f"%( i_lep, lep['pdgId'], lep['tight_SS'], lep['pt'], lep['eta'], lep['phi'], lep['mvaTTV'], lep['muonInnerTrkRelErr'] ) )
        logger.sync( " "*20 + "FO_4l %i tight_4l %i FO_3l %i tight_3l %i FO_SS %i tight_SS %i"%( lep['FO_4l'], lep['tight_4l'], lep['FO_3l'], lep['tight_3l'], lep['FO_SS'], lep['tight_SS'] ) )
        if abs(lep['pdgId'])==13:
            logger.sync( " "*20 + "trkMult %6.5f mRelIsoCh %6.5f mRelIsoNeu %6.5f ptrel %6.5f ptratio %6.5f iso03 %6.5f jetDeepCSV %6.5f sip3d %6.5f segmComp %6.5f", \
                lep['trackMult'], lep['miniRelIsoCharged'], lep['miniRelIsoNeutral'], lep['jetPtRelv2'], lep['jetPtRatiov2'], lep['relIso03'], lep['jetBTagDeepCSV'], lep['sip3d'], lep['segmentCompatibility'] )
            logger.sync( " "*20 + "mediumMuonId %i", lep['mediumMuonId'] )
        if abs(lep['pdgId'])==11:
            logger.sync( " "*20 + "convVeto %i tightCharge %i lostHits %i chargeConsistency %i", lep['convVeto'], lep['tightCharge'], lep['lostHits'], lep['chargeConsistency'] )
            logger.sync( " "*20 + "trkMult %6.5f mRelIsoCh %6.5f mRelIsoNeu %6.5f ptrel %6.5f ptratio %6.5f iso03 %6.5f jetDeepCSV %6.5f sip3d %6.5f eleMVA %6.5f", \
                lep['trackMult'], lep['miniRelIsoCharged'], lep['miniRelIsoNeutral'], lep['jetPtRelv2'], lep['jetPtRatiov2'], lep['relIso03'], lep['jetBTagDeepCSV'], lep['sip3d'], lep['mvaIdSpring16'] )
