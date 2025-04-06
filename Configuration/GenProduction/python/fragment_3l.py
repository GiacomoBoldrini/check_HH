import FWCore.ParameterSet.Config as cms

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/home/llr/cms/skulac/gridpack_HH_new/ggHH_slc7_amd64_gcc700_CMSSW_10_6_8_workdir3_ggHH_kl_1p00_kt_1p00_c2_0p00_bugfix.tgz'),
    nEvents = cms.untracked.uint32(100),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)


#Link to datacards:
#https://github.com/cms-sw/genproductions/tree/master/bin/MadGraph5_aMCatNLO/cards/production/2017/13TeV/exo_diboson/

import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from Configuration.Generator.PSweightsPythia.PythiaPSweightsSettings_cfi import *
from Configuration.Generator.Pythia8PowhegEmissionVetoSettings_cfi import *

generator = cms.EDFilter("Pythia8HadronizerFilter",
                         maxEventsToPrint = cms.untracked.int32(1),
                         pythiaPylistVerbosity = cms.untracked.int32(1),
                         filterEfficiency = cms.untracked.double(1.0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(13000.),
                         PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        pythia8PSweightsSettingsBlock,
        pythia8PowhegEmissionVetoSettingsBlock,
        processParameters = cms.vstring(
            'POWHEG:nFinal = 2',   ## Number of final state particles
            '23:mMin = 0.05',
            '24:mMin = 0.05',
            '25:m0 = 125.0',
            '25:onMode = off',
            '25:onIfMatch = 24 -24', #H->w+w-
            '25:onIfMatch = 23 23', #H->ZZ
            '23:onMode = off', # disable all Z decay modes
            '23:onIfAny = 1 2 3 4 5 6 7 8 11 13 15', # enable only Z->ll and Z->qq
            'ResonanceDecayFilter:filter = on',
            'ResonanceDecayFilter:exclusive = on', #off: require at least the specified number of daughters, on: require exactly the specified number of daughters
            'ResonanceDecayFilter:mothers = 25,24,23', #? TBC! list of mothers not specified -> count all particles in hard process+resonance decays 
            #(better to avoid specifying mothers when including leptons from the lhe in counting, since intermediate resonances are not gauranteed to appear in general
            # 'ResonanceDecayFilter:wzAsEquivalent = on',
            'ResonanceDecayFilter:eMuAsEquivalent = on', #on: treat electrons and muons as equivalent
            'ResonanceDecayFilter:daughters = 24,24,23,23,11,11,11',
          ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'pythia8PSweightsSettings',
                                    'pythia8PowhegEmissionVetoSettings',
                                    'processParameters'
                                    )
        )
                         )

ProductionFilterSequence = cms.Sequence(generator)