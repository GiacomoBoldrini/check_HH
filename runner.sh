#!/bin/sh
set -e
#set -x

RUN_DIR=${PWD}
echo ">> Setting RUN_DIR to ${RUN_DIR}"

CMSSW_RELEASE=CMSSW_12_4_16
SCRAM_ARCH=el8_amd64_gcc10

if [ "${CMSSW_RELEASE}" != "local" ]; then
    if [ -d ${CMSSW_RELEASE} ]; then
      echo ">> Cleaning up existing ${CMSSW_RELEASE} directory"
      rm -r ${CMSSW_RELEASE}
    fi
    echo ">> Setting up release area for ${CMSSW_RELEASE} and arch ${SCRAM_ARCH}"
    if [ ! -d ${CMSSW_RELEASE} ]; then
      scram project CMSSW ${CMSSW_RELEASE}
    fi

    cd ${CMSSW_RELEASE}/src
    eval `scramv1 runtime -sh`
    cd -

fi

cmsRun nanGenScratch.py
