
# standard imports
import os

# RootTools
from RootTools.core.standard import *

# Logging
import logging
logger = logging.getLogger(__name__)

dir = "/scratch/rschoefbeck/"

TTZ_200PU        = Sample.fromDirectory("TTZ_200PU",    texName = "ttZ (200PU)",    directory = [os.path.join( dir, "TTZ", "200PU")], treeName = 'Delphes')
TTZ_200PU.xsec   = 0.7152

TTZ_nominal      = Sample.fromDirectory("TTZ_nominal",  texName = "ttZ (nominal)",  directory = [os.path.join( dir, "TTZ", "nominal")], treeName = 'Delphes')
TTZ_nominal.xsec = 0.7152

WZ               = Sample.fromDirectory("WZ",           texName = "WZ",             directory = [os.path.join( dir, "WZ", )], treeName = 'Delphes')
WZ.xsec          = 3.125
