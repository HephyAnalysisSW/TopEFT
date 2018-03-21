import sys
n=0
if len(sys.argv)>1:
    with open(sys.argv[1]) as f:
        for i_line, line in enumerate(f.readlines()):
            for i_char,char in enumerate(line):
                n+=1
                if ord(char) in [10]: continue #backspace
                if ord(char)>ord('~') or ord(char)<ord(' '): print "file %s line %i char %i: ord %i %s" % (sys.argv[1], i_line, i_char, ord(char), char)
    print "Checked %i characters in file %s" %( n, sys.argv[1] )

