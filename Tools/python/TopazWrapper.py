''' Class to read the output of Topaz. 
'''

# Standard imports
import ROOT
import os
import array
import uuid
import subprocess

# Logging
import logging
logger = logging.getLogger(__name__)

# TopEFT
from TopEFT.Tools.u_float import u_float

class TopazReader:

    def __init__( self, *args ):

        self.filenames = args

        # Hold the data
        self.histogram_titles = {}
        self.histogram_data   = {}

        # Let's keep all the header information
        self.headers = []

        # The first file defines the data structure. We want an error if we combine differently structured files.
        first_file = True

        # Read all files
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
            # Keep headers
            self.headers.append( header )

            first_file = False
            logger.info( "Read %i histograms from file %s", len(self.histogram_data.keys()), filename )

        # Make histograms. Don't make them again.
        self.__histos = { n: self.__make_histo__( n ) for n in self.histogram_data.keys() }

    def __make_histo__( self, n ):
  
        # x values
        x_vals = list(self.histogram_data[n].keys())
        x_vals.sort()
        # assume equal binning and add last bin
        if len(x_vals)>=2:
            x_vals.append( x_vals[-1] + (x_vals[-1]-x_vals[-2]))
        else:
            x_vals.append( x_vals[0]+1)
            

        h = ROOT.TH1D('topaz_histo_%i_%s'%( n, uuid.uuid4().hex), self.histogram_titles[n], len(x_vals)-1, array.array('d', x_vals) )
        h.GetXaxis().SetTitle(self.histogram_titles[n])
        for i, x_val in enumerate(x_vals[:-1]):
            h.SetBinContent( i+1, self.histogram_data[n][x_val].val)
            h.SetBinError  ( i+1, self.histogram_data[n][x_val].sigma)

        return h

    @property
    def histos( self ):
        return self.__histos

    # convinience
    def draw_plots(self, plot_directory):
      ''' Draws all TOPAZ histograms into the directory 
      ''' 
      from RootTools.core.standard import Plot, plotting

      for log in [False, True]:
        plot_directory_ = os.path.join(plot_directory, ("log" if log else "lin") )

        for n, histo in self.histos.iteritems():
            plot = Plot.fromHisto(name = self.histogram_titles[n].replace('/','over'), histos = [[histo]], texX = self.histogram_titles[n], texY="") 

            plotting.draw(plot,
              plot_directory = plot_directory_,
              #ratio = {'yRange':(0.1,1.9)} if not args.noData else None,
              logX = False, logY = log, sorting = True,
              #yRange = (0.03, "auto") if log else (0.001, "auto"),
              #scaling = {},
              #legend = [ (0.15,0.9-0.03*sum(map(len, plot.histos)),0.9,0.9), 2],
              #drawObjects = drawObjects( not args.noData, dataMCScale , lumi_scale )
            )

      with open(os.path.join( plot_directory, 'headers.txt'), 'w') as f:
        for i_header, header in enumerate(self.headers):
            f.write("######### Header %i #########\n\n"%i_header)
            f.write( header )
            f.write( '\n' )

class Topaz:

    def __init__( self, *args ):

        self.processes = filter( lambda arg: arg.startswith('Process='), args)
        if self.processes == ():
            self.processes = ('Process=71', 'Process=72')

        other_args= filter( lambda arg: not arg.startswith('Process='), args)

        default_args        = ( 'Collider=13', 'VegasNc0=50000', 'VegasNc1=500000', 'TopDK=4', 'ZDK=1', 'ObsSet=53', 'Correction=0', 'NLOParam=1' )

        self.args = list(other_args)

        # Fill up with default arguments
        for d_arg in default_args:
            if not any( arg.startswith(d_arg.split('=')[0]) for arg in other_args ):
                self.args.append( d_arg )
                logger.info( "Added default argument %s" , d_arg )

    def run( self ):

        out_file_names = []
        for process in self.processes:
            output_filename = ('to_%s'%(uuid.uuid4().hex))[:25]
            out_file_names.append( os.path.join( os.path.expandvars('$CMSSW_BASE/src/TOPAZ'), output_filename +'.dat') )
            origWD = os.getcwd() 
            os.chdir(os.path.expandvars('$CMSSW_BASE/src/TOPAZ'))
            run_args = [ os.path.expandvars('$CMSSW_BASE/src/TOPAZ/TOPAZ'), process, 'HistoFile=%s'%output_filename] + self.args
            subprocess.call( run_args )
            os.chdir( origWD )

        self.reader = TopazReader( *out_file_names )

        for o_file in out_file_names:
            os.remove( o_file )
