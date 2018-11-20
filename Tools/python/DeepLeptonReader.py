#Standard imports
import pickle
import ROOT
import os
import shutil
import uuid
import operator
import copy
#from guppy import hpy
#h = hpy()

from math import *
import numpy as np

class InputData:
    def __init__( self, filename, treename = "tree"):

        # read class from file
        file_= ROOT.TFile.Open( filename.replace('root://hephyse.oeaw.ac.at', 'root://hephyse.oeaw.ac.at:11001') )
        tree = file_.Get(treename)
        # tmp locations
        self.tmpdir = "."
        self.tmpname = "DL_reader_"+uuid.uuid4().hex
        self.tmp_filenames = [ "%s.C"%self.tmpname, "%s.h"%self.tmpname ]
        # make class
        tree.MakeClass( self.tmpname )
        file_.Close()

        # move files to tmp area
        for file in self.tmp_filenames:
            shutil.move( file, os.path.join( self.tmpdir, file ) )

        # load the newly created files as macro
        ROOT.gROOT.LoadMacro( os.path.join( self.tmpdir, self.tmpname+'.C' ) )

        # make chain (can be used with more files)
        self.chain = ROOT.TChain( treename )
        self.chain.Add( filename )

        # make instance
        self.event = getattr(ROOT, "%s" % self.tmpname )( self.chain )

        self.chain.GetEntries()

        self.nevent = None

    def getEntry( self, nevent ):
        self.chain.GetEntry( nevent )
        self.nevent = nevent

    # Clean up the tmp files
    def __del__( self ):
        import os #Interesting. os gets un-imported in the destructor :-)
        for file_ in self.tmp_filenames:
           filename = os.path.join( self.tmpdir, file_ )
           if os.path.exists( filename ):
                os.remove( filename )
        
def ptRel(p4,axis):
    a = ROOT.TVector3(axis.Vect().X(),axis.Vect().Y(),axis.Vect().Z())
    o = ROOT.TLorentzVector(p4.Px(),p4.Py(),p4.Pz(),p4.E())
    return o.Perp(a)

def deltaPhi(phi1, phi2):
    dphi = phi2-phi1
    if  dphi > pi:
        dphi -= 2.0*pi
    if dphi <= -pi:
        dphi += 2.0*pi
    return abs(dphi)

def deltaR2(eta1, phi1, eta2, phi2):
    return deltaPhi(phi1, phi2)**2 + (eta1 - eta2)**2

def deltaR(*args, **kwargs):
    return sqrt(deltaR2(*args, **kwargs))

class Evaluator:

    flavors =       [ 'neutral', 'charged', 'photon',  'electron', 'muon', 'SV'] # don't change the sequence!
    lengths =       [     5,        25,       10,         3,          3,     4 ] # input lengths in the RNN. This must be consistent with the training! 
    max_n_pf_cand = { 'neutral':200, 'charged':500, 'photon': 200, 'electron': 50, 'muon': 50, 'SV': 200 } # max lengths in the event. avoid buffer errors. 
    def __init__( self ): 

        self.init_getters()

        # dict cache for all pf candidates in the event
        self._pf_candidates = {} 
        self.means          = None

        # verbosity
        self.verbosity = 0

        self._nevent = None

        self.event = None

    # Setters to store means and branches
    def setMeans( self, means ):
        self.means = means
    def setFeatureBranches( self, feature_branches ):
        self.feature_branches = feature_branches
    def setPFBranches( self, pf_branches ):
        self.pf_branches = pf_branches
    def setEvent( self, event ):
        self.event = event

    # Store a list of functors that retrieve the correct branch from the event
    def feature_getters( self, collection_name):
        # return getters, if collection_name known, otherwise create      
        if self._feature_getters.has_key(collection_name): return self._feature_getters[collection_name] 
        self._feature_getters[collection_name] = {
                          "lep_pt":operator.attrgetter(collection_name+'_pt'),
                         "lep_eta":operator.attrgetter(collection_name+'_eta'),
                         "lep_dxy":operator.attrgetter(collection_name+'_dxy'),
                          "lep_dz":operator.attrgetter(collection_name+'_dz'),
                        "lep_edxy":operator.attrgetter(collection_name+'_edxy'),
                         "lep_edz":operator.attrgetter(collection_name+'_edz'),
                        "lep_ip3d":operator.attrgetter(collection_name+'_ip3d'),
                       "lep_sip3d":operator.attrgetter(collection_name+'_sip3d'),
              "lep_innerTrackChi2":operator.attrgetter(collection_name+'_innerTrackChi2'),
  "lep_innerTrackValidHitFraction":operator.attrgetter(collection_name+'_innerTrackValidHitFraction'),
                     "lep_ptErrTk":operator.attrgetter(collection_name+'_ptErrTk'),
                         "lep_rho":operator.attrgetter(collection_name+'_rho'),
                       "lep_jetDR":operator.attrgetter(collection_name+'_jetDR'),
         "lep_trackerLayers_float":operator.attrgetter(collection_name+'_trackerLayers'),
           "lep_pixelLayers_float":operator.attrgetter(collection_name+'_pixelLayers'),
           "lep_trackerHits_float":operator.attrgetter(collection_name+'_trackerHits'),
              "lep_lostHits_float":operator.attrgetter(collection_name+'_lostHits'),
         "lep_lostOuterHits_float":operator.attrgetter(collection_name+'_lostOuterHits'),
                    "lep_relIso03":operator.attrgetter(collection_name+'_relIso03'),
           "lep_miniRelIsoCharged":operator.attrgetter(collection_name+'_miniRelIsoCharged'),
           "lep_miniRelIsoNeutral":operator.attrgetter(collection_name+'_miniRelIsoNeutral'),
                "lep_jetPtRatiov1":operator.attrgetter(collection_name+'_jetPtRatiov1'),
                  "lep_jetPtRelv1":operator.attrgetter(collection_name+'_jetPtRelv1'),
                "lep_jetPtRatiov2":operator.attrgetter(collection_name+'_jetPtRatiov2'),
                  "lep_jetPtRelv2":operator.attrgetter(collection_name+'_jetPtRelv2'),
              "lep_jetBTagDeepCSV":operator.attrgetter(collection_name+'_jetBTagDeepCSV'),
        "lep_segmentCompatibility":operator.attrgetter(collection_name+'_segmentCompatibility'),
          "lep_muonInnerTrkRelErr":operator.attrgetter(collection_name+'_muonInnerTrkRelErr'),
          "lep_isGlobalMuon_float":operator.attrgetter(collection_name+'_isGlobalMuon'),
           "lep_chi2LocalPosition":operator.attrgetter(collection_name+'_chi2LocalPosition'),
           "lep_chi2LocalMomentum":operator.attrgetter(collection_name+'_chi2LocalMomentum'),
             "lep_globalTrackChi2":operator.attrgetter(collection_name+'_globalTrackChi2'),
         "lep_glbTrackProbability":operator.attrgetter(collection_name+'_glbTrackProbability'),
                     "lep_trkKink":operator.attrgetter(collection_name+'_trkKink'),
           "lep_caloCompatibility":operator.attrgetter(collection_name+'_caloCompatibility'),
             "lep_nStations_float":operator.attrgetter(collection_name+'_nStations'),
                         "lep_phi":operator.attrgetter(collection_name+'_phi'),
                       "lep_pdgId":operator.attrgetter(collection_name+'_pdgId'),
        }
        return self._feature_getters[collection_name] 

    # Store a list of functors that retrieve the correct branch from the event
    def init_getters( self):
        self._feature_getters = {}

        self.pf_collection_names = { 
            "neutral":  "DL_pfCand_neutral",
            "charged":  "DL_pfCand_charged",
            "photon":   "DL_pfCand_photon",
            "muon":     "DL_pfCand_muon",
            "electron": "DL_pfCand_electron",
            "SV":       "DL_SV",
            }

        self.pf_size_getters = { key:operator.attrgetter( "n"+name ) for key, name in self.pf_collection_names.iteritems() } 

        self.pf_getters = { 'neutral':{
            "pfCand_neutral_pt_ptRelSorted":operator.attrgetter( "DL_pfCand_neutral_pt"),
   "pfCand_neutral_puppiWeight_ptRelSorted":operator.attrgetter( "DL_pfCand_neutral_puppiWeight"),
        "pfCand_neutral_fromPV_ptRelSorted":operator.attrgetter( "DL_pfCand_neutral_fromPV"),
           "pfCand_neutral_eta_ptRelSorted":operator.attrgetter( "DL_pfCand_neutral_eta"),
           "pfCand_neutral_phi_ptRelSorted":operator.attrgetter( "DL_pfCand_neutral_phi"),
        },
                            'charged':{
            "pfCand_charged_pt_ptRelSorted":operator.attrgetter( "DL_pfCand_charged_pt"),
   "pfCand_charged_puppiWeight_ptRelSorted":operator.attrgetter( "DL_pfCand_charged_puppiWeight"),
        "pfCand_charged_fromPV_ptRelSorted":operator.attrgetter( "DL_pfCand_charged_fromPV"),
        "pfCand_charged_dxy_pf_ptRelSorted":operator.attrgetter( "DL_pfCand_charged_dxy_pf"),
         "pfCand_charged_dz_pf_ptRelSorted":operator.attrgetter( "DL_pfCand_charged_dz_pf"),
"pfCand_charged_dzAssociatedPV_ptRelSorted":operator.attrgetter( "DL_pfCand_charged_dzAssociatedPV"),
           "pfCand_charged_eta_ptRelSorted":operator.attrgetter( "DL_pfCand_charged_eta"),
           "pfCand_charged_phi_ptRelSorted":operator.attrgetter( "DL_pfCand_charged_phi"),
        },
                            'photon':{
             "pfCand_photon_pt_ptRelSorted":operator.attrgetter( "DL_pfCand_photon_pt"),
    "pfCand_photon_puppiWeight_ptRelSorted":operator.attrgetter( "DL_pfCand_photon_puppiWeight"),
         "pfCand_photon_fromPV_ptRelSorted":operator.attrgetter( "DL_pfCand_photon_fromPV"),
            "pfCand_photon_eta_ptRelSorted":operator.attrgetter( "DL_pfCand_photon_eta"),
            "pfCand_photon_phi_ptRelSorted":operator.attrgetter( "DL_pfCand_photon_phi"),
        },
                            'electron':{
           "pfCand_electron_pt_ptRelSorted":operator.attrgetter( "DL_pfCand_electron_pt"),
       "pfCand_electron_dxy_pf_ptRelSorted":operator.attrgetter( "DL_pfCand_electron_dxy_pf"),
        "pfCand_electron_dz_pf_ptRelSorted":operator.attrgetter( "DL_pfCand_electron_dz_pf"),
        "pfCand_electron_pdgId_ptRelSorted":operator.attrgetter( "DL_pfCand_electron_pdgId"),
          "pfCand_electron_eta_ptRelSorted":operator.attrgetter( "DL_pfCand_electron_eta"),
          "pfCand_electron_phi_ptRelSorted":operator.attrgetter( "DL_pfCand_electron_phi"),
        },
                            'muon':{
               "pfCand_muon_pt_ptRelSorted":operator.attrgetter( "DL_pfCand_muon_pt"),
           "pfCand_muon_dxy_pf_ptRelSorted":operator.attrgetter( "DL_pfCand_muon_dxy_pf"),
            "pfCand_muon_dz_pf_ptRelSorted":operator.attrgetter( "DL_pfCand_muon_dz_pf"),
            "pfCand_muon_pdgId_ptRelSorted":operator.attrgetter( "DL_pfCand_muon_pdgId"),
              "pfCand_muon_eta_ptRelSorted":operator.attrgetter( "DL_pfCand_muon_eta"),
              "pfCand_muon_phi_ptRelSorted":operator.attrgetter( "DL_pfCand_muon_phi"),
        },
                            'SV':{
                          "SV_pt_ptSorted":operator.attrgetter("DL_SV_pt"),
                        "SV_chi2_ptSorted":operator.attrgetter("DL_SV_chi2"),
                        "SV_ndof_ptSorted":operator.attrgetter("DL_SV_ndof"),
                         "SV_dxy_ptSorted":operator.attrgetter("DL_SV_dxy"),
                        "SV_edxy_ptSorted":operator.attrgetter("DL_SV_edxy"),
                        "SV_ip3d_ptSorted":operator.attrgetter("DL_SV_ip3d"),
                       "SV_eip3d_ptSorted":operator.attrgetter("DL_SV_eip3d"),
                       "SV_sip3d_ptSorted":operator.attrgetter("DL_SV_sip3d"),
                    "SV_cosTheta_ptSorted":operator.attrgetter("DL_SV_cosTheta"),
                "SV_maxDxyTracks_ptSorted":operator.attrgetter("DL_SV_maxDxyTracks"),
                "SV_secDxyTracks_ptSorted":operator.attrgetter("DL_SV_secDxyTracks"),
                "SV_maxD3dTracks_ptSorted":operator.attrgetter("DL_SV_maxD3dTracks"),
                "SV_secD3dTracks_ptSorted":operator.attrgetter("DL_SV_secD3dTracks"),
                         "SV_eta_ptSorted":operator.attrgetter("DL_SV_eta"),
                         "SV_phi_ptSorted":operator.attrgetter("DL_SV_phi"),
        },
    }

    # for a given lepton, read the pf candidate mask and return the PF indices
    def get_pf_indices( self, flavor, collection_name, n_lep):
        n = min( self.max_n_pf_cand[flavor], self.pf_size_getters[flavor](self.event) )
        pf_mask = getattr(self.event, "%s_%s_mask" % (self.pf_collection_names[flavor], "selectedLeptons" if collection_name=="LepGood" else "otherLeptons" ) )
        mask_ = (1<<n_lep)
        try:
            return filter( lambda i: mask_&pf_mask[i], range(n))
        except IndexError as e:
            print "n_lep", n_lep, n, flavor, self.event.evt, self.event.lumi, self.event.run
            raise e

    def _get_all_pf_candidates( self, flavor):
        n = min( self.max_n_pf_cand[flavor], self.pf_size_getters[flavor](self.event) )
        att_getters = self.pf_getters[flavor]
        try: 
            return [ {name: getter(self.event)[i] for name, getter in self.pf_getters[flavor].iteritems()} for i in range(n) ]
        except IndexError as e:
            print n, flavor, self.event.evt, self.event.lumi, self.event.run
            raise e
    
    # cached version of get_all_pf_candidates
    @property
    def pf_candidates( self ):
        if self._nevent == self.event.evt:
            return self._pf_candidates
        else:
            self._pf_candidates = {flavor: self._get_all_pf_candidates(flavor) for flavor in self.flavors}
            self._nevent = self.event.evt
            return self._pf_candidates

    # put all inputs together
    def pf_candidates_for_lepton( self, collection_name, n_lep):

        # read pf indices, then select the candidates
        pf_candidates = {}
        for flavor in self.flavors:
            pf_indices            = self.get_pf_indices( flavor, collection_name, n_lep )
            pf_candidates[flavor] = [ self.pf_candidates[flavor][i] for i in pf_indices]

            # now calculate the pf_candidate features that depend on the lepton in question
            lep_p4 = ROOT.TLorentzVector()
            lep_getters = self.feature_getters( collection_name )
            lep_p4.SetPtEtaPhiM( lep_getters["lep_pt"](self.event)[n_lep], lep_getters["lep_eta"](self.event)[n_lep], lep_getters["lep_phi"](self.event)[n_lep], 0. )

            name = "pfCand_"+flavor+"_%s_ptRelSorted" if flavor!="SV" else "SV_%s_ptSorted"
            ptRel_name = name%"ptRel"
            dR_name    = name%"deltaR"
            for cand in pf_candidates[flavor]:

                cand_p4 = ROOT.TLorentzVector()
                cand_p4.SetPtEtaPhiM( 
                    cand[name%"pt"], cand[name%"eta"],cand[name%"phi"],0.
                    )
                
                cand[ptRel_name] = ptRel( cand_p4, lep_p4 )
                cand[dR_name]    = deltaR( cand[name%"eta"], cand[name%"phi"], lep_getters["lep_eta"](self.event)[n_lep], lep_getters["lep_phi"](self.event)[n_lep])

            # ptRel sorting
            pf_candidates[flavor].sort( key = lambda p:-p[ptRel_name] )

            # filter lepton from list of candidates 
            if flavor=="electron" and abs(lep_getters["lep_pdgId"](self.event)[n_lep])==11:
                pf_candidates["electron"] = filter( lambda p: p[dR_name]>3*10**-4 or p[name%"pdgId"]!=lep_getters["lep_pdgId"](self.event)[n_lep], pf_candidates["electron"]) 
            if flavor=="muon" and abs(lep_getters["lep_pdgId"](self.event)[n_lep])==13:
                pf_candidates["muon"]     = filter( lambda p: p[dR_name]>3*10**-4 or p[name%"pdgId"]!=lep_getters["lep_pdgId"](self.event)[n_lep], pf_candidates["muon"]) 

        return pf_candidates

    def features_for_lepton( self, collection_name, n_lep):
        # read the lepton features
        return [ self.feature_getters( collection_name )[b](self.event)[n_lep] for b in self.feature_branches ]

    @property 
    def pf_norm_zero( self ):
        if not hasattr( self, "_pf_norm_zero"):
            self._pf_norm_zero = []
            for i_flavor, flavor in enumerate(self.flavors):
                cand_res = []
                for i_cand in range(self.lengths[i_flavor]):
                    branch_res = [] 
                    for b in self.pf_branches[i_flavor]:
                        branch_res.append( -self.means[b][0]/self.means[b][1] )
                    cand_res.append( branch_res )
                self._pf_norm_zero.append( cand_res )
        return copy.deepcopy(self._pf_norm_zero)

    @property 
    def pf_zero( self ):
        if not hasattr( self, "_pf_zero"):
            self._pf_zero = []
            for i_flavor, flavor in enumerate(self.flavors):
                cand_res = []
                for i_cand in range(self.lengths[i_flavor]):
                    branch_res = [] 
                    for b in self.pf_branches[i_flavor]:
                        branch_res.append( 0 )
                    cand_res.append( branch_res )
                self._pf_zero.append( cand_res )
        return copy.deepcopy(self._pf_zero)

    def prepare_features_normalized( self, collection_name, n_lep):
        
        features            = self.features_for_lepton( collection_name, n_lep )
        features_normalized = [ (features[i_b]-self.means[b][0])/self.means[b][1] for i_b, b in enumerate( self.feature_branches ) ]
        return features_normalized

    def prepare_pf_normalized( self, collection_name, n_lep):
        
        pf_candidates = self.pf_candidates_for_lepton( collection_name, n_lep )

        pf_norm_res = self.pf_norm_zero  
        #pf_res      = self.pf_zero  
        for i_flavor, (flavor, branches) in enumerate(zip(self.flavors, self.pf_branches)):
            if self.verbosity>=5: print "flavor %10s"%flavor,"cands %2i"%len(pf_candidates[flavor]),"max %2i"%self.lengths[i_flavor]
            for i_cand, cand in enumerate(pf_candidates[flavor][:self.lengths[i_flavor]]):
                branch_res = [] 
                for i_branch, branch in enumerate(branches):
                        pf_norm_res[i_flavor][i_cand][i_branch] = (cand[branch]-self.means[branch][0])/self.means[branch][1]
                        if self.verbosity>=10: print "  flavor %10s cand %2i  branch %40s val %6.4f mean %6.4f var %6.4f norm %6.4f" % ( flavor, i_cand, branch, cand[branch], self.means[branch][0], self.means[branch][1], pf_norm_res[i_flavor][i_cand][i_branch] )
         
        #return features_normalized, pf_norm_res, pf_res 
        return pf_norm_res 

#   # feature structure:
#    [ np.array( features_normalized[i_lep][i_feat], np=float32), 
#      np.array( pf_norm[flavor][i_lep][i_cand][i_feat], np=float32) ]

    def evaluate( self):
        features_normalized = np.array( [ self.prepare_features_normalized( "LepGood", i_lep ) for i_lep in range(self.event.nLepGood) ], dtype=np.float32 )
        # [i_lep][i_flavor][i_cand][i_feat]
        pf_normalized       = np.array( [ self.prepare_pf_normalized( "LepGood", i_lep ) for i_lep in range(self.event.nLepGood) ] )
        # make [i_flavor][i_lep][i_cand][i_feat]
        pf_normalized = np.swapaxes(pf_normalized, 0,1)
        np_features = [ features_normalized ] + [ np.array(list(pf_normalized[i]), dtype=np.float32) for i in range(len(pf_normalized))] 
        prediction = deepLeptonModel.predict( np_features )
        return prediction

## Theano config
#import uuid, os
#theano_compile_dir = '/afs/hephy.at/data/%s01/theano_compile_tmp/%s'%( os.environ['USER'], str(uuid.uuid4()) )
#if not os.path.exists( theano_compile_dir ):
#    os.makedirs( theano_compile_dir )
##os.environ['THEANO_FLAGS'] = 'cuda.root=/cvmfs/cms.cern.ch/slc6_amd64_gcc630/external/cuda/8.0.61/,device=cpu,base_compiledir=%s'%theano_compile_dir 
#os.environ['THEANO_FLAGS'] = 'cuda.enabled=False,base_compiledir=%s'%theano_compile_dir 
#os.environ['KERAS_BACKEND'] = 'theano'

import tensorflow as tf
from keras.backend.tensorflow_backend import set_session
config = tf.ConfigProto()
#config.gpu_options.per_process_gpu_memory_fraction = 0.3
#config.gpu_options.allow_growth = True
#config.gpu_options.visible_device_list = "0"

assert False, ""
config.intra_op_parallelism_threads = 1
config.inter_op_parallelism_threads = 1

set_session(tf.Session(config=config))

#model_file = "/afs/hephy.at/data/rschoefbeck01/DeepLepton/trainings/DYVsQCD_ptRelSorted_MuonTraining/KERAS_model.h5"
model_file = "/afs/hephy.at/data/gmoertl01/DeepLepton/trainings/muons/20181117/TTs_balanced_pt5toInf_MuonTraining/KERAS_model.h5"
pkl_model_file  = model_file.replace('.h5','pkl') 

#from keras.models import load_model
#deepLeptonModel = load_model(model_file)
#pickle.dump( (deepLeptonModel.to_json(), deepLeptonModel.get_weights()), file(model_file.replace('.h5','pkl'),'w') )

model_json, weights = pickle.load( file(pkl_model_file) )
from keras.models import model_from_json
deepLeptonModel = model_from_json( model_json )
deepLeptonModel.set_weights( weights )
#branches, means   = pickle.load(file("/afs/hephy.at/data/rschoefbeck01/DeepLepton/trainings/DYVsQCD_ptRelSorted_MuonTrainData/branches_means_vars.pkl"))
branches, means   = pickle.load(file("/afs/hephy.at/data/gmoertl01/DeepLepton/trainings/muons/20181117/TTs_balanced_pt5toInf_MuonTrainData/branches_means_vars.pkl"))

# patch weights
weights         = deepLeptonModel.get_weights()
weights_patched = map( np.nan_to_num, weights )
deepLeptonModel.set_weights( weights_patched )
if not np.array_equal(weights, weights_patched):
    print "Warning! Had to remove NaNs/Infs!"

evaluator = Evaluator()
# specify means, features and branches
evaluator.setMeans( means )
evaluator.setFeatureBranches( branches[0] )
evaluator.setPFBranches(      branches[1:] )
evaluator.verbosity = 5

if __name__ == "__main__": 
    # Information on the training (works only in DL)
    #from trainingInfo import TrainingInfo
    #training_directory = '/afs/hephy.at/data/gmoertl01/DeepLepton/trainings/muons/20181013/DYVsQCD_ptRelSorted_MuonTrainData'
    #trainingInfo = TrainingInfo( training_directory )
    # means = trainingInfo.means

    # Input data
    input_filename = "/afs/hephy.at/data/rschoefbeck01/DeepLepton/data/full_events/WZTo3LNu_amcatnlo_2/treeProducerSusySingleLepton/tree.root"

    inputData = InputData( input_filename )
    inputData.getEntry(0)

    evaluator.setEvent( inputData.event )
    evaluator.verbosity = 0
    # loop over file
    nevents = inputData.chain.GetEntries()
    c = 0
    while True:
        c+=1
        for nevent in range( nevents ): 
            inputData.getEntry(nevent)
            evaluator.evaluate()
        print c
        ROOT.gObjectTable.Print()
        #print h.heap()

        #for i_lep in range( inputData.event.nLepGood ):
        #    if abs(inputData.event.LepGood_pdgId[i_lep])!=13: continue
        #    print "LepGood %i/%i" % (i_lep, inputData.event.nLepGood)
        #    print "nevent %i evt %20i lumi %8i run %8i" %( nevent, inputData.event.evt, inputData.event.lumi, inputData.event.run )
        #    features      =  evaluator.features_for_lepton( "LepGood", i_lep )
        #    features_normalized = evaluator.prepare_features_normalized( "LepGood", i_lep)
        #    pf_norm             = evaluator.prepare_pf_normalized( "LepGood", i_lep)
        #    np_features = [ np.array( [ features_normalized ], dtype=np.float32 ) ] + [ np.array( [ pf_n ], dtype=np.float32 ) for pf_n in pf_norm]
        #    print "Make prediction"
        #    prediction = deepLeptonModel.predict( np_features )
        #    print prediction
        #    if nevent == 9: break
        #if nevent==9: break

    ##benchmark features from Georg
    #from outputfeatures import features as moertel_features
    #prediction = deepLeptonModel.predict( moertel_features )
#print "Georg:\n",prediction
