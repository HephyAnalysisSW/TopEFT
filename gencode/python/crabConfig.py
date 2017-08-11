import os

class crab:
    def __init__(self, release, releasePath):
        self.release = release
        os.system("scram runtime -sh")
        os.system("source ")

    def config(self):
        return

    def launch(self):
        print 'Launching jobs with config:'

        #get the crabDir
        self.crabDir = "" #should be the absolute path

    def status(self, crabDir):
        return
