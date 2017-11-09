import os
import subprocess

'''
Read events from allEvents.txt file.
Each line of the file has to be of the structure:
run:lumi:event
'''

eventList = []
with open("allEvents.txt","r") as f:
    while True:
        l = f.readline()
        if l =='': break
        eventList.append(l.replace('\n',''))

runsAndEras = {\
    '2016B':    {'range': (272007,   275376), 'dataset':'/SingleElectron/Run2016B-03Feb2017_ver2-v2/MINIAOD'},
    '2016C':    {'range': (275657,   276283), 'dataset':'/SingleElectron/Run2016C-03Feb2017-v1/MINIAOD'},
    '2016D':    {'range': (276315,   276811), 'dataset':'/SingleElectron/Run2016D-03Feb2017-v1/MINIAOD'},
    '2016E':    {'range': (276831,   277420), 'dataset':'/SingleElectron/Run2016E-03Feb2017-v1/MINIAOD'},
    '2016F':    {'range': (277772,   278808), 'dataset':'/SingleElectron/Run2016F-03Feb2017-v1/MINIAOD'},
    '2016G':    {'range': (278820,   280385), 'dataset':'/SingleElectron/Run2016G-03Feb2017-v1/MINIAOD'},
    '2016Hv2':  {'range': (280919,   284037), 'dataset':'/SingleElectron/Run2016H-03Feb2017_ver2-v1/MINIAOD'},   
    '2016Hv3':  {'range': (284037,   284044), 'dataset':'/SingleElectron/Run2016H-03Feb2017_ver3-v1/MINIAOD'},
    }


for i,ev in enumerate(sorted(eventList)):
    run_str = ev.replace(':','_')
    run = int(ev.split(':')[0])
    dataset = False
    for era in runsAndEras:
        if run >= runsAndEras[era]['range'][0] and run <= runsAndEras[era]['range'][1]:
            dataset = runsAndEras[era]['dataset']
    if dataset:
        print "Event %s should be in datset %s"%(ev, dataset)
    else: print ":("
    oFile = "picks/event_%s"%i
    cmd = ["edmPickEvents.py", dataset, ev, "--output", oFile, "--runInteractive"]
    print ' '.join(cmd)
    subprocess.call(cmd)

