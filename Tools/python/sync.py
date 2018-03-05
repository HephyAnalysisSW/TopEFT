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
        logger.sync( "lepton %2i pdgId %+2i tight %i pt/eta/phi %7.3f/%+3.2f/%+3.2f MVA %+7.6f"%( i_lep, lep['pdgId'], lep['tight'], lep['pt'], lep['eta'], lep['phi'], lep['mvaTTV'] ) )
        if abs(lep['pdgId'])==13:
            logger.sync( " "*20 + "trkMult %4.3f mRelIsoCh %4.3f mRelIsoNeu %4.3f ptrel %4.3f ptratio %4.3f iso03 %4.3f jetCSV %4.3f sip3d %4.3f segmComp %4.3f", \
                lep['trackMult'], lep['miniRelIsoCharged'], lep['miniRelIsoNeutral'], lep['jetPtRelv2'], lep['jetPtRatiov2'], lep['relIso03'], lep['jetBTagCSV'], lep['sip3d'], lep['segmentCompatibility'] )
            logger.sync( " "*20 + "mediumMuonId %i", lep['mediumMuonId'] )
        if abs(lep['pdgId'])==11:
            logger.sync( " "*20 + "convVeto %i tightCharge %i lostHits %i", lep['convVeto'], lep['tightCharge'], lep['lostHits'] )
            logger.sync( " "*20 + "trkMult %4.3f mRelIsoCh %4.3f mRelIsoNeu %4.3f ptrel %4.3f ptratio %4.3f iso03 %4.3f jetCSV %4.3f sip3d %4.3f eleMVA %4.3f", \
                lep['trackMult'], lep['miniRelIsoCharged'], lep['miniRelIsoNeutral'], lep['jetPtRelv2'], lep['jetPtRatiov2'], lep['relIso03'], lep['jetBTagCSV'], lep['sip3d'], lep['mvaIdSpring16'] )
