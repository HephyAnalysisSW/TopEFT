# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/HIG-RunIIFall17wmLHEGS-00041-fragment.py --datatier GEN --conditions 93X_mc2017_realistic_v3 --beamspot Realistic25ns13TeVEarly2017Collision --step LHE,GEN --era Run2_2017 --python_filename GEN.py --no_exec -n 10
import FWCore.ParameterSet.Config as cms

import FWCore.ParameterSet.VarParsing as VarParsing
options = VarParsing.VarParsing ('standard')
options.register('gridpack', '/afs/cern.ch/work/s/schoef/CMS/gen/gridpacks/ttZ0j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz',  VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string,  "Which Gridpack?")
options.register('outputDir','./',          VarParsing.VarParsing.multiplicity.singleton, VarParsing.VarParsing.varType.string,  "Where to store the output root file?")
options.maxEvents=10 # maxEvents is a registered option. 

if not 'ipython' in VarParsing.sys.argv[0]:
  options.parseArguments()
else:
  print "No parsing of arguments!"

import os
print options.outputDir
print os.path.isdir(options.outputDir)
if not os.path.isdir(options.outputDir):
    os.makedirs(options.outputDir)


from Configuration.StandardSequences.Eras import eras

process = cms.Process('GEN',eras.Run2_2017)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13TeVEarly2017Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/HIG-RunIIFall17wmLHEGS-00041-fragment.py nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('GEN_LO_0j.root'),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '93X_mc2017_realistic_v3', '')

#process.generator = cms.EDFilter("Pythia8HadronizerFilter",
#    PythiaParameters = cms.PSet(
#        parameterSets = cms.vstring('pythia8CommonSettings', 
#            'pythia8CP5Settings', 
#            'processParameters'),
##        processParameters = cms.vstring('JetMatching:setMad = off', 
##            'JetMatching:scheme = 1', 
##            'JetMatching:merge = on', 
##            'JetMatching:jetAlgorithm = 2', 
##            'JetMatching:etaJetMax = 5.', 
##            'JetMatching:coneRadius = 1.', 
##            'JetMatching:slowJetPower = 1', 
##            'JetMatching:qCut = 60.', 
##            'JetMatching:nQmatch = 5', 
##            'JetMatching:nJetMax = 0', 
##            'JetMatching:doShowerKt = off'),
#        pythia8CP5Settings = cms.vstring('Tune:pp 14', 
#            'Tune:ee 7', 
#            'MultipartonInteractions:ecmPow=0.03344', 
#            'PDF:pSet=20', 
#            'MultipartonInteractions:bProfile=2', 
#            'MultipartonInteractions:pT0Ref=1.41', 
#            'MultipartonInteractions:coreRadius=0.7634', 
#            'MultipartonInteractions:coreFraction=0.63', 
#            'ColourReconnection:range=5.176', 
#            'SigmaTotal:zeroAXB=off', 
#            'SpaceShower:alphaSorder=2', 
#            'SpaceShower:alphaSvalue=0.118', 
#            'SigmaProcess:alphaSvalue=0.118', 
#            'SigmaProcess:alphaSorder=2', 
#            'MultipartonInteractions:alphaSvalue=0.118', 
#            'MultipartonInteractions:alphaSorder=2', 
#            'TimeShower:alphaSorder=2', 
#            'TimeShower:alphaSvalue=0.118'),
#        pythia8CommonSettings = cms.vstring('Tune:preferLHAPDF = 2', 
#            'Main:timesAllowErrors = 10000', 
#            'Check:epTolErr = 0.01', 
#            'Beams:setProductionScalesFromLHEF = off', 
#            'SLHA:keepSM = on', 
#            'SLHA:minMassSM = 1000.', 
#            'ParticleDecays:limitTau0 = on', 
#            'ParticleDecays:tau0Max = 10', 
#            'ParticleDecays:allowPhotonRadiation = on')
#    ),
#    comEnergy = cms.double(13000.0),
#    filterEfficiency = cms.untracked.double(1.0),
#    maxEventsToPrint = cms.untracked.int32(1),
#    pythiaHepMCVerbosity = cms.untracked.bool(False),
#    pythiaPylistVerbosity = cms.untracked.int32(1)
#)

process.generator = cms.EDFilter("Pythia8HadronizerFilter",
                         maxEventsToPrint = cms.untracked.int32(1),
                         pythiaPylistVerbosity = cms.untracked.int32(1),
                         filterEfficiency = cms.untracked.double(1.0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(13000.),
                         PythiaParameters = cms.PSet(
        parameterSets = cms.vstring('pythia8CommonSettings', 
            'pythia8CP5Settings'), 
        pythia8CP5Settings = cms.vstring('Tune:pp 14', 
            'Tune:ee 7', 
            'MultipartonInteractions:ecmPow=0.03344', 
            'PDF:pSet=20', 
            'MultipartonInteractions:bProfile=2', 
            'MultipartonInteractions:pT0Ref=1.41', 
            'MultipartonInteractions:coreRadius=0.7634', 
            'MultipartonInteractions:coreFraction=0.63', 
            'ColourReconnection:range=5.176', 
            'SigmaTotal:zeroAXB=off', 
            'SpaceShower:alphaSorder=2', 
            'SpaceShower:alphaSvalue=0.118', 
            'SigmaProcess:alphaSvalue=0.118', 
            'SigmaProcess:alphaSorder=2', 
            'MultipartonInteractions:alphaSvalue=0.118', 
            'MultipartonInteractions:alphaSorder=2', 
            'TimeShower:alphaSorder=2', 
            'TimeShower:alphaSvalue=0.118'),
        pythia8CommonSettings = cms.vstring('Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:keepSM = on', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on')
    ),
)

#ProductionFilterSequence = cms.Sequence(generator)

process.externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    #args = cms.vstring('/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/ttZ01j_5f/v1/ttZ01j_5f.tar.xz'),
    #args = cms.vstring('/afs/cern.ch/work/s/schoef/CMS/gen/gridpacks/ttZ0j_rwgt_slc6_amd64_gcc630_CMSSW_9_3_0_tarball.tar.xz'),
    args = cms.vstring(options.gridpack),
    nEvents = cms.untracked.uint32(10),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)


# Path and EndPath definitions
process.lhe_step = cms.Path(process.externalLHEProducer)
process.generation_step = cms.Path(process.pgen)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.lhe_step,process.generation_step,process.genfiltersummary_step,process.endjob_step,process.RECOSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	if path in ['lhe_step']: continue
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
