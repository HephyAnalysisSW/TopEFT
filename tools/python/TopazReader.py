''' Class to read the output of Topaz. 
'''

# Standard imports
import ROOT
import os
import array

# Logging
import logging
logger = logging.getLogger(__name__)

class TopazReader:

    def __init__( self, filename ):
        if os.path.exists( filename ): 
            self.filename = filename
        else:
            raise IOError( "File does not exist: %s" % filename )

        self.header = ""
        self.histogram_titles = {}
        self.histogram_data   = {}

        with open( self.filename ) as f:
            reading_header = True
            
            # read content of file
            for line in f.readlines():
                if line.startswith( "# Histogram"):
                    reading_header = False
                    key, value = line.rstrip().lstrip("# Histogram").split(":")
                    self.histogram_titles[int(key)] = value.lstrip().rstrip()
                elif line[0]!='#':
                    s_n, s_x0, s_y, s_y_err, s_hits = line.rstrip().rstrip('|').split('|')
                    n     = int(s_n)
                    x0    = float(s_x0)
                    y     = float(s_y)
                    y_err = float(s_y_err)
                    hits  = int(s_hits)

                    if not self.histogram_data.has_key(n):
                        self.histogram_data[n] = []

                    self.histogram_data[n].append((x0, y, y_err))
                    
                else:
                    if reading_header: self.header+=line

        self.__histos = { n: self.__make_histo__( n ) for n in self.histogram_data.keys() }
        logger.info( "Read %i histograms from file %s", len(self.histogram_data.keys()), filename )

    def __make_histo__( self, n ):
  
        # x values
        x_vals = [v[0] for v in self.histogram_data[n]]
        # assume equal binning and add last bin
        x_vals.append( x_vals[-1] + (x_vals[-1]-x_vals[-2]))

        h = ROOT.TH1D('topaz_histo_%i'%n, self.histogram_titles[n], len(x_vals)-1, array.array('d', x_vals) )
        for i, v in enumerate(self.histogram_data[n]):
            x, y, y_err = v
            h.SetBinContent( i+1, y)
            h.SetBinError  ( i+1, y_err)

        return h

    @property
    def histos( self ):
        return self.__histos
