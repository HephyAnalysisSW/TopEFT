
from TopEFT.tools.resultsDB import resultsDB
from TopEFT.tools.user import results_directory, tmp_directory
from TopEFT.tools.u_float import u_float



# should get lumi, presel, weightString? from setup
lumi            = 35.9
columns         = ["process", "region", "channel", "presel", "lumi", "weightString"]
presel          = "lep_pt[0]>40&&lep_pt[1]>20&&lep_pt[2]>10&&nGoodLeptons==3&&njet>2&&nBTag>0&&abs(Z_mass-91.2)<10"
weightString    = "weight*%s"%lumi


def getEstimate(sample, region, channel, overwrite=False):
    ''' to be extended '''
    res = resultsDB(results_directory+"resultsCache.db", "TopEFT", columns)
    key = {"process":sample.name, "channel":channel, "region":region.cutString(), "lumi":lumi, "presel":presel, "weightString":weightString}
    if res.contains(key) and not overwrite:
        print "Found estimate for %s in region %s"%(sample.name, region)
        return res.get(key)
    else:
        print "Adding estimate for %s in region %s"%(sample.name, region)
        y = u_float(sample.getYieldFromDraw("&&".join([presel, region.cutString()]), weightString))
        res.add(key, y, overwrite=True)
        #raise NotImplementedError("I can't get a new estimate yet")
        
    
