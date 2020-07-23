from __future__ import print_function
from sklearn import svm
import numpy as np
from sklearn.model_selection import train_test_split


#TODO #1: change directory. Replace "/" with "\" for Windows
x = np.load("lteX.npy")
y = np.load("lteY.npy")
y = y.astype(int)
print(y)
print(np.shape(x))
print(np.shape(y))
sampleSize = np.shape(x)[1]
ySize = np.size(y)
maxValue = max(y) + 1
averageRange = 1 #How much on average
#Loss and RBF size information
loss =38
rbfSize = 0.35
avgAccuracy = 0
for ind2 in range(averageRange):
    xTrain, xTest, yTrain, yTest= train_test_split(x,y,test_size=0.33, stratify=y)
    clf = svm.LinearSVC()
    # clf = svm.SVC(kernel='linear', C=4, gamma=1)
    # clf = svm.SVC(kernel='rbf', C=loss, gamma=rbfSize)


    clf.fit(xTrain,yTrain)
    accuracy = clf.score(xTest, yTest)
    avgAccuracy += accuracy
print("{0:.5} loss: {1} | rbfSize: {2}".format(avgAccuracy/float(averageRange), loss, rbfSize))