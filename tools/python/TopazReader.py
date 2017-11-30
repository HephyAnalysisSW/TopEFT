''' Class to read the output of Topaz. 
'''

# Standard imports
import ROOT
import os
import array
import uuid

# Logging
import logging
logger = logging.getLogger(__name__)

# TopEFT
from TopEFT.tools.u_float import u_float

class TopazReader:

    def __init__( self, *args ):

        self.filenames = args

        # Read all files

        self.histogram_titles = {}
        self.histogram_data   = {}
        self.headers = []

        first_file = True
        for filename in self.filenames:
            if os.path.exists( filename ): 
                self.filename = filename
            else:
                raise IOError( "File does not exist: %s" % filename )

            header = ""
            with open( filename ) as f:
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

                        # protection: Take structure from first file. Any extra bin subsequent files will raise error
                        if first_file:
                            if not self.histogram_data.has_key(n):
                                self.histogram_data[n] = {}
                            if not self.histogram_data[n].has_key(x0):
                                self.histogram_data[n][x0] = u_float(0)

                        self.histogram_data[n][x0]+=u_float(y,y_err)
                         
                    else:
                        if reading_header: header+=line

            self.headers.append( header )

            first_file = False
            logger.info( "Read %i histograms from file %s", len(self.histogram_data.keys()), filename )

        self.__histos = { n: self.__make_histo__( n ) for n in self.histogram_data.keys() }

    def __make_histo__( self, n ):
  
        # x values
        x_vals = list(self.histogram_data[n].keys())
        x_vals.sort()
        # assume equal binning and add last bin
        x_vals.append( x_vals[-1] + (x_vals[-1]-x_vals[-2]))

        h = ROOT.TH1D('topaz_histo_%i_%s'%( n, uuid.uuid4().hex), self.histogram_titles[n], len(x_vals)-1, array.array('d', x_vals) )
        h.GetXaxis().SetTitle(self.histogram_titles[n])
        for i, x_val in enumerate(x_vals[:-1]):
            h.SetBinContent( i+1, self.histogram_data[n][x_val].val)
            h.SetBinError  ( i+1, self.histogram_data[n][x_val].sigma)

        return h

    @property
    def histos( self ):
        return self.__histos

    def drawPlots(self, plot_directory):

      from RootTools.core.standard import Plot, plotting

      for log in [False, True]:
        plot_directory_ = os.path.join(plot_directory, ("log" if log else "lin") )

        for n, histo in self.histos.iteritems():
            plot = Plot.fromHisto(name = self.histogram_titles[n], histos = [[histo]], texX = self.histogram_titles[n], texY="") 

            plotting.draw(plot,
              plot_directory = plot_directory_,
              #ratio = {'yRange':(0.1,1.9)} if not args.noData else None,
              logX = False, logY = log, sorting = True,
              #yRange = (0.03, "auto") if log else (0.001, "auto"),
              #scaling = {},
              #legend = [ (0.15,0.9-0.03*sum(map(len, plot.histos)),0.9,0.9), 2],
              #drawObjects = drawObjects( not args.noData, dataMCScale , lumi_scale )
            )

