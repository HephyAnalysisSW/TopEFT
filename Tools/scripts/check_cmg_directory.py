#!/usr/bin/env python
import os
from TopEFT.Tools.helpers import checkRootFile

def get_parser():
    ''' Argument parser.
    '''
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for cmgPostProcessing")

    argParser.add_argument('--directory',                   action='store',         nargs='?',  type=str,                           default='.', help="Name of the directory")

    return argParser

args = get_parser().parse_args()
missing_root_files_dirs = []
missing_txt_files_dirs  = []
inconsistent_filesize_paths = []
broken_files      = []
broken_directories= []
for root, dirs, files in os.walk(args.directory):
    path = root.split(os.sep)
    if any(file.endswith('.root') for file in files):
        #print "Checking", root
        sizes = [os.stat(os.path.join( root, file)).st_size for file in files if file.endswith('.root')]
        rel_diff = (max(sizes)-min(sizes))/(0.5*float( max(sizes)+min(sizes)))
        if rel_diff>0.03:
            inconsistent_filesize_paths.append( os.path.join( root ) )
            print "WARNING! Directory %s contains root files whose size differ by %3.2f " % (root, rel_diff)
    if any(file.endswith('.root') or file.endswith('.txt') for file in files):
        root_files = [file for file in files if file.endswith('.root')]
        txt_files = [file for file in files if file.endswith('.txt')]
        
        if file.endswith('.root') and not checkRootFile(os.path.join( root, file), checkForObjects=["Events"]):
            broken_files.append( os.path.join( root, file) )    
            if root not in broken_directories: broken_directories.append(root)
        n_txt = []
        for txt_file in txt_files:
            try:
                n_txt.append( ( int(txt_file.rstrip('.txt').split('njob')[-1]), txt_file) )
            except IndexError:
                pass
        n_root = []
        for root_file in root_files:
            try:
                n_root.append( ( int(root_file.rstrip('.root').split('_')[-1]), root_file) )
            except IndexError:
                pass

        for n, f in n_txt:
            if n not in [ n_ for (n_,f_) in n_root ]:
                print "Have txt file without root file: ", f
                if not root in missing_root_files_dirs: missing_root_files_dirs.append(root)
        for n, f in n_root:
            if n not in [ n_ for (n_,f_) in n_txt ]:
                print "Have root file without txt file: ", f
                if not root in missing_txt_files_dirs: missing_txt_files_dirs.append(root)

if len(inconsistent_filesize_paths)>0:
    print "\nVarying root file sizes:"
    for path in inconsistent_filesize_paths:
        print path
if len(broken_directories)>0:
    print "\nPaths with broken files:"
    for path in broken_directories:
        print path
if len(broken_files)>0:
    print "\nBroken files:"
    for file in broken_files:
        print file
if len(missing_txt_files_dirs)>0:
    print "\nPaths with missing txt files:"
    for path in missing_txt_files_dirs:
        print path
if len(missing_root_files_dirs)>0:
    print "\nPaths with missing root files:"
    for path in missing_root_files_dirs:
        print path
