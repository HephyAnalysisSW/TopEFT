from TopEFT.Tools.TopazWrapper import Topaz
import TopEFT.Tools.logger as logger

logger = logger.get_logger("DEBUG", logFile = None)


#t=Topaz('DC1AZ=0.6','DC1VZ=-0.24')
t=Topaz('DC2AZ=-0.2','DC2VZ=0.2')
t.run()

