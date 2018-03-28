import os

def get_parser():
    ''' Argument parser.
    '''
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for cmgPostProcessing")

    argParser.add_argument('--directory',                   action='store',         nargs='?',  type=str,                           default='.', help="Name of the directory")

    return argParser

args = get_parser().parse_args()

paths = []
for root, dirs, files in os.walk(args.directory):
    path = root.split(os.sep)
    if any(file.endswith('.root') for file in files):
        #print "Checking", root
        sizes = [os.stat(os.path.join( root, file)).st_size for file in files if file.endswith('.root')]
        rel_diff = (max(sizes)-min(sizes))/(0.5*float( max(sizes)+min(sizes)))
        if rel_diff>0.03:
            paths.append( path )
            print "WARNING! Directory %s contains root files whose size differ by %3.2f " % (root, rel_diff)

print "Problematic:"
for path in paths:
    print path[-1]
