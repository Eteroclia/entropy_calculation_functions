import ProcessingLib,pandas

if __name__ == '__main__':
    varAll={}
    proba=[0.0815,0.0097,0.0315,0.0373,0.1739,0.0112,0.0097,0.0085,0.0731,0.0045,0.0002,0.0569,0.0287,
        0.0712,0.0528,0.0280,0.0121,0.0664,0.0814,0.0722,0.0638,0.0164,0.0003,0.0041,0.0028,0.0015]
    dataSet=pandas.read_csv("lab02-classe-race-tableau.csv")
    print(ProcessingLib.calcJoinedEntropy(dataSet))
    dataSet=pandas.read_csv("lab02-classe-race-tableau-equi.csv")
    print(ProcessingLib.calcJoinedEntropy(dataSet))
    dataSet=pandas.read_csv("lab02-classe-race-tableau.csv")
    print(ProcessingLib.calcCondEntropy(dataSet,"Guerrier·e"))
    #ProcessingLib.benfords(dataSet)
    #print(ProcessingLib.calcEntropy(proba))




