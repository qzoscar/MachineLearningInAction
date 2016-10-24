# -*- coding:utf-8 -*-
from math import log


# 计算熵的函数
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
        if vec[axis] == value:
            reducedFeatVec = vec[:axis]
            reducedFeatVec.extend(vec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet


def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0])-1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet] # 取出数据集的第i列
        uniqueVals = set(featList) # 第i列数值集合
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)



            