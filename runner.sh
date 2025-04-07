#!/bin/sh
set -e
#set -x

RUN_DIR=${PWD}
echo ">> Setting RUN_DIR to ${RUN_DIR}"
source /cvmfs/cms.cern.ch/cmsset_default.sh
CMSSW_RELEASE=CMSSW_12_4_16
SCRAM_ARCH=el8_amd64_gcc10

export SCRAM_ARCH=$SCRAM_ARCH

cmsrel $CMSSW_RELEASE

cd $CMSSW_RELEASE/src; cmsenv; cd -

cmsRun nanGenScratch.py
