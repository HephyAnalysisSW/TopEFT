''' Cleaning script for local MG directories
'''

# Standard imports
import os,shutil
import argparse

# Logger
import logging
logger = logging.getLogger(__name__)

argParser = argparse.ArgumentParser(description = "Argument parser")
argParser.add_argument('--force',       action='store_true', help="Force mode")
args = argParser.parse_args()


ls_list = os.listdir("/tmp/")

old_dirs = [ "/tmp/"+a for a in ls_list if len(a) == 32 ]

logger.info( "Will delete the following dirs." )
for d in old_dirs:
    logger.info( "  " + d )

for d in old_dirs:
    if not args.force:
        a = raw_input('Deleting %s. Press any key to continue, s to skip:\n'%d)
        if str(a) == 's': continue
    print "Deleting %s ..."%d
    shutil.rmtree(d)


