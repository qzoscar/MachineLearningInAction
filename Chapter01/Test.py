from numpy import *
randMat =  mat(random.rand(4,4))
invRandMat = randMat.I
print randMat, '\n',invRandMat

print randMat*invRandMat