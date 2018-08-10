''' Class for reading Delphes files.
'''

# Standard imports
import ROOT
import uuid
import os
import shutil

# Logging
import logging
logger = logging.getLogger(__name__)

# RootTools
from RootTools.core.DelphesReaderBase import DelphesReaderBase

class DelphesReader( DelphesReaderBase ):

    def muonsTight( self ):
        res = self.read_collection( 'MuonTight', 
            [   ('PT', 'pt'), ( 'Eta', 'eta'), ('Phi', 'phi'), 
                ('Charge', 'charge'), ('IsolationVar', 'isolationVar'), ('IsolationVarRhoCorr', 'isolationVarRhoCorr'),  
                ('SumPtCharged', 'sumPtCharged'),  ('SumPtNeutral', 'sumPtNeutral'), ('SumPtChargedPU', 'sumPtChargedPU'),  ('SumPt', 'sumPt') 
            ])
        for r in res:
            r['pdgId'] = -13*r['charge']
            r['ehadOverEem'] = float('nan')
        return res

    def muonsLoose( self ):
        res = self.read_collection( 'MuonLoose', 
            [   ('PT', 'pt'), ( 'Eta', 'eta'), ('Phi', 'phi'), 
                ('Charge', 'charge'), ('IsolationVar', 'isolationVar'), ('IsolationVarRhoCorr', 'isolationVarRhoCorr'),  
                ('SumPtCharged', 'sumPtCharged'),  ('SumPtNeutral', 'sumPtNeutral'), ('SumPtChargedPU', 'sumPtChargedPU'),  ('SumPt', 'sumPt') 
            ])
        for r in res:
            r['pdgId'] = -13*r['charge']
            r['ehadOverEem'] = float('nan')
        return res

    def electrons( self ):
        res = self.read_collection( 'Electron', 
            [   ('PT', 'pt'), ( 'Eta', 'eta'), ('Phi', 'phi'), 
                ('Charge', 'charge'), ('IsolationVar', 'isolationVar'), ('IsolationVarRhoCorr', 'isolationVarRhoCorr'),  
                ('SumPtCharged', 'sumPtCharged'),  ('SumPtNeutral', 'sumPtNeutral'), ('SumPtChargedPU', 'sumPtChargedPU'),  ('SumPt', 'sumPt'),
                ('EhadOverEem','ehadOverEem')
            ])
        for r in res:
            r['pdgId'] = -11*r['charge']
        return res

    def jets( self ):
        return self.read_collection( 'JetPUPPI', 
            [   ('PT', 'pt'), ( 'Eta', 'eta'), ('Phi', 'phi'),
                ('BTag', 'bTag'), ( 'BTagPhys', 'bTagPhys'), ('BTagAlgo', 'bTagAlgo'),
                ('DeltaEta', 'deltaEta'),
                ('DeltaPhi', 'deltaPhi'),
                ('Flavor', 'flavor'),
                ('FlavorAlgo', 'flavorAlgo'),
                ('FlavorPhys', 'flavorPhys'),

                ('Charge', 'charge'),
                ('EhadOverEem', 'ehadOverEem'),
                ('NCharged', 'nCharged'),
                ('NNeutrals', 'nNeutrals'),
            ])

    def met( self ):
        return self.read_collection( 'PuppiMissingET', [('MET', 'pt'), ('Phi', 'phi')] )

