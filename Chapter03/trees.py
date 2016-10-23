from math import log

def calcShannonEnt(dataSet):
    data_size = len(dataSet)
    labelCounts = {}
    for vec in dataSet:
        label = vec[-1]
        if label not in labelCounts.keys():
            labelCounts[label]=0
        labelCounts[label]+=1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/data_size
        shannonEnt = shannonEnt+(-prob*log(prob,2))
    return shannonEnt


def splitDataSet(dataSet,axis,value):
    retDataSet=[]
    for vec in dataSet:
        if vec[axis] = value:
            