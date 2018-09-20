def getNorms(dirName='',normsToExtract=[]):

    combineOutputFile   = dirName + "/output.txt"
    scaleFactorFile     = dirName + "/SF.txt"

    norms = {r:1 for r in normsToExtract}

    with open(combineOutputFile) as combineOutput:
        for line in combineOutput:
            for norm in normsToExtract:
                if line.startswith(norm):
                    #line
                    norms[norm] = line.split('=')[-1].replace('(limited)','').replace('\t','').replace('\n','')[1:]
                    #print line

    scaleFactors = open(scaleFactorFile, 'w')

    scaleFactors.write("Scalefactors\n\n")
    for norm in norms:
        scaleFactors.write("{:30}{:30}\n".format(norm,norms[norm]))

    scaleFactors.close()
