from numpy import *
import operator
from os import listdir
def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX,(dataSetSize,1)) - dataSet
    distances = ((diffMat**2).sum(axis=1))**0.5
    sortedIndex = distances.argsort()
    classCount = {}
    for i in range(k):
        label = labels[sortedIndex[i]]
        classCount[label] = classCount.get(label,0) + 1
    sortedClassCount = sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]


# group,labels = createDataSet()
# print classify0([0,0],group,labels ,3)

def file2matrix(filename):
    f = open(filename)
    lines = f.readlines()
    numberOfLines = len(lines)
    resultMat = zeros((numberOfLines,3))
    labels=[]
    row = 0

    for line in lines:
        lineList = line.strip().split('\t')
        resultMat[row,:]=lineList[0:3]
        labels.append(int(lineList[-1]))
        row = row +1
    return resultMat,labels

dating_data, datingLabels = file2matrix('datingTestSet2.txt')
# print datingLabels[0:20]
# print dating_data[0:5]

import matplotlib
import matplotlib.pyplot as plt

# fig = plt.figure()
# sub1 = fig.add_subplot(111)
# sub1.scatter(dating_data[:,0],dating_data[:,1],array(datingLabels)*15.0,array(datingLabels)*15.0)
# fig.show()

def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    print minVals, maxVals
    ranges = maxVals-minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet=(dataSet-tile(minVals,(m,1)))/tile(ranges,(m,1))
    return normDataSet, ranges, minVals


# normMat, ranges, minVals = autoNorm(dating_data)

def datingClassTest():
    hoRatio = 0.10
    dating_data, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(dating_data)
    m = normMat.shape[0]
    testSetNum = int(m*hoRatio)
    errorCount = 0.0
    for i in range(testSetNum):
        classifierResult = classify0(normMat[i,:],normMat[testSetNum:m,:],\
                                     datingLabels[testSetNum:m],3)
        print "the classify result is: %d, the real answer is %d" %(classifierResult, datingLabels[i])
        if(classifierResult != datingLabels[i]):
            errorCount += 1.0
    print "the total error rate is: %f" %(errorCount/float(testSetNum))

# datingClassTest()

def classifyPerson():
    resultList = ['not at all','in small doses','in large doses']
    percentTats = float(raw_input("percentage of time spent playing video games:"))
    ffMiles = float(raw_input("frequent flier miles earned per year:"))
    iceCream = float(raw_input("liters of ice cream consumed per year:"))
    dating_data,datingLabels = file2matrix("datingTestSet2.txt")
    normMat,ranges,minVals = autoNorm(dating_data)
    inArr = array([ffMiles,percentTats,iceCream])
    classifierResult = classify0((inArr-minVals)/ranges,normMat,datingLabels,3)
    print "You will probably like this person: ", resultList[classifierResult-1]

# classifyPerson()


def img2vector(filename):
    Vect = zeros((1,1024))
    f = open(filename)
    for i in range(32):
        line = f.readline()
        for j in range(32):
            Vect[0,32*i+j]=int(line[j])
    return Vect

# testVector = img2vector('testDigits/0_13.txt')
# print testVector[0,0:31]


def handwritingClassTest():
    Labels = []
    trainingFileList = listdir('trainingDigits')
    m = len(trainingFileList)
    trainingMat = zeros((m,1024))
    for i in range(m):
        fileName = trainingFileList[i]
        classNum = int(fileName.split('_')[0])
        Labels.append(classNum)
        trainingMat[i,:]=img2vector('trainingDigits/%s' %fileName)
    testFileList = listdir('testDigits')
    errorCount = 0.0
    # size of testset
    m_test = len(testFileList)
    for i in range(m_test):
        fileName = testFileList[i]
        classNum = int(fileName.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' %fileName)
        classifierResult = classify0(vectorUnderTest,trainingMat,Labels,3)
        print "the classify result is %d, the real answer is: %d" %(classifierResult,classNum)
        if(classifierResult!=classNum):
            errorCount+=1.0

    print "\nthe total number of errors is %d" %errorCount
    print "\nerror rate is %f" %(errorCount/float(m_test))

handwritingClassTest()