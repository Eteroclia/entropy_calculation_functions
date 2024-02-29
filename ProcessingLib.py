import pandas
import math

def calcTOt(dataSet:pandas.DataFrame):
    """
    calculate the total of data in a dataframe with top and left headers
    :param dataSet: a panda dataframe with top and left headers
    :return: total amount of data
    """
    topHeader=list(dataSet.columns)
    leftHeader=list(dataSet[topHeader[0]])
    tot=0
    for i in topHeader[1:]:
        for j in dataSet[i]:
            tot+=j
    return tot

def calcJoinedEntropy(dataSet:pandas.DataFrame):
    """
    calculate the joined entropy from a matrix with vertical en horizontal headers
    :param dataSet: a panda dataframe with top and left headers
    :return: the joined entropy of the dataset
    """
    topHeader = list(dataSet.columns)
    leftHeader = list(dataSet[topHeader[0]])
    probabilityMatrixTop:list[list]=[]#proba of class by race
    probabilityMatrixDic:dict={}#proba of class by race, dic form
    leftHeaderNumberDic:dict={}#position of each class in the above dic list
    probaTotLeftHeader:dict={}#tot prob of apparition per class
    probaTotRace:dict={}#tot prob of apparition per race
    tot = calcTOt(dataSet)

    for i in topHeader[1:]:#calculate the percentage of apparition of each square
        raceProba=[i]
        for j in dataSet[i]:
            raceProba.append(j/tot)
        probabilityMatrixTop.append(raceProba)
    for i in probabilityMatrixTop:
        probabilityMatrixDic.update({i[0]:i[1:]})

    for i in range(0, len(leftHeader)):
        leftHeaderNumberDic.update({leftHeader[i]:i})

    for i in leftHeader:#calculate tot percentage per left header
        classIndex=leftHeaderNumberDic.get(i)
        totStat=0
        for j in probabilityMatrixTop:
            totStat+=j[classIndex+1]
        probaTotLeftHeader.update({i:totStat})

    for i in probabilityMatrixTop:#calculate tot percentage per top header
        totStat=0
        for j in i[1:]:
            totStat+=j
        probaTotRace.update({i[0]:totStat})

    entropy=0
    for i in leftHeader:#calculate the joined entropy
        classIndex=leftHeaderNumberDic.get(i)
        x=probaTotLeftHeader.get(i)
        for j in probabilityMatrixTop:
            xny=j[classIndex+1]
            pXY=x*xny/probaTotRace.get(j[0])
            entropy-=pXY*math.log10(pXY)
    return entropy

def calcCondEntropy(dataSet:pandas.DataFrame,y:str):
    """
    calculate the conditional entropy from a matrix with vertical en horizontal headers
    :param y: name in left header acting as 'y' in H(X|y)
    :param dataSet: a panda dataframe with top and left headers
    :return: the conditional entropy of the dataset
    """
    topHeader = list(dataSet.columns)
    leftHeader = list(dataSet[topHeader[0]])
    probabilityMatrixTop:list[list]=[]#proba of class by race
    probabilityMatrixDic:dict={}#proba of class by race, dic form
    leftHeaderNumberDic:dict={}#position of each class in the above dic list
    probaTotLeftHeader:dict={}#tot prob of apparition per class
    probaTotRace:dict={}#tot prob of apparition per race
    tot = calcTOt(dataSet)

    for i in topHeader[1:]:#calculate the percentage of apparition of each square
        raceProba=[i]
        for j in dataSet[i]:
            raceProba.append(j/tot)
        probabilityMatrixTop.append(raceProba)
    for i in probabilityMatrixTop:
        probabilityMatrixDic.update({i[0]:i[1:]})

    for i in range(0, len(leftHeader)):
        leftHeaderNumberDic.update({leftHeader[i]:i})

    for i in leftHeader:#calculate tot percentage per left header
        classIndex=leftHeaderNumberDic.get(i)
        totStat=0
        for j in probabilityMatrixTop:
            totStat+=j[classIndex+1]
        probaTotLeftHeader.update({i:totStat})

    for i in probabilityMatrixTop:#calculate tot percentage per top header
        totStat=0
        for j in i[1:]:
            totStat+=j
        probaTotRace.update({i[0]:totStat})

    entropy=0
    leftIndex=leftHeaderNumberDic.get(y)
    for i in probabilityMatrixTop:#calculate the conditional entropy
        xny=i[leftIndex+1]
        pxkny=xny/probaTotLeftHeader.get(y)
        entropy-=pxkny*math.log10(pxkny)
    return entropy

def calcEntropy(proba:list)->float:
    """
    calculate entropy from a list of probability
    :param proba: a list of probability
    :return: the entropy of the list
    """
    entropy=0
    for i in proba:
        entropy-=i*math.log2(i)
    return entropy
def createBenfordsStat()->list:
    """
    Function which return a list of Benford's law probability
    for digit from 1 to 9.

    :return: nine long ordered list.
    """
    probs:list=[]
    for i in range(1,10):
        probs.append(math.log10(i+1)-math.log10(i))
    return probs

def benfords(dataSet:pandas.DataFrame):
    """
    Function calculating variance for a dataset against Benford's law
    :param dataSet: a raw dataframe read from a csv using pandas
    :return: nothing
    """
    probs=createBenfordsStat()#get the probability of occurrence of each digit according to Benford's
    columns=[]
    header=list(dataSet.columns)
    for i in header:
        colStat=[0,0,0,0,0,0,0,0,0,0]#number of apparition of each digit (1 to 9), last cell is tot amount
        tot=0
        for j in dataSet[i].tolist():
            tot+=1
            colStat[int(str(j)[0])-1]+=1
        colStat[9]=tot
        deviation=[] #deviation per digit
        totDev=0 #added total of deviation
        for j in range(0, len(colStat)-1):
            deviation.append(math.pow(colStat[j]/colStat[-1]-probs[j],2)) #(X-xmed)^2
            totDev+=deviation[-1]
        print("deviation for "+i+" is ")
        print(deviation)
        print("with a total deviation of "+str(totDev))



