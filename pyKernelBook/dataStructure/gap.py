#from set import *
import string
import sets
from subString import *

def getAllString(mString):
    tmpString = {}
    for i in mString:
        tmpString[i]=1
    return tmpString.keys()

def getMismatchSubString(mString, allString, mismatch, mer):
    tmpList = []
    mString = string.lower(mString)
    if (mismatch == 0):
        return getSubSequence(mString, mer)
    elif (mismatch == 1):
        tmpString = []
        for i in allString:
            res = getSubSequence(mString + i, mer)
            for j in res:
                tmpString.append(j)
        return tmpString
    
def searchSubSequence(mString1, mString2, gap):
    len1 = len(mString1)
    len2 = len(mString2)
    allString = getAllString(mString1 + mString2)
    print allString
    if (len1 > len2):
        searchStr = mString2
        motherStr = mString1
        searchLen = len2
    else:
        searchStr = mString1
        motherStr = mString2
        searchLen = len1
    kernel = 0
    if (gap == 0):
        t = getSubString(motherStr, searchLen)
        print t
        for i in t:
            if (i == searchStr):
                kernel += 1
    elif (gap == 1):
#        missString = intersectComplement(allString, getAllString(searchStr))
        allString=sets.Set(allString)
#        missString = sets.difference(allString, getAllString(searchStr))
        missString = allString.difference(getAllString(searchStr))        
        print 'M',missString, motherStr, searchStr, allString
        s = getSubSequence(motherStr, searchLen+1)
        s2 = gapCount(s, searchStr)
        t = getMismatchSubString(motherStr, allString, 1, searchLen+1)
        t=sets.Set(t)
        t = t.union(t)
        print s,t,s2
        for i in t:
            for j in s2:
                if (i == j):
                    kernel += 1
    return kernel

def gapCount(stringList, searchStr):
    length = len(searchStr)
    tmpList = []
    gapList = []
    for i in stringList:
        loc = 0
        gap = 0
        for j in i:
            if (loc < length+1):
                if (j == searchStr[loc]):
                    loc += 1
                    if (loc == length):
                        tmpList.append(i)
                        loc = length+1
                        gapList.append(gap)
                else:
                    gap += 1
    print tmpList, gapList
    return tmpList, gapList

def demo():
    mString1 = 'gon'
    mString2 = 'gone'
    mString3 = 'going'
    mString4 = 'galleon'
    print searchSubSequence(mString1, mString2, 0)
    print searchSubSequence(mString1, mString3, 1)

    print getAllString(mString1)
    print getAllString(mString2)
    all = getAllString(mString1 + mString2)
    print all
    all = sets.Set(all)
    
#    print intersectComplement(all,getAllString(mString1))
    print all.difference(getAllString(mString1))
    b=sets.Set(getAllString(mString1))
    c=sets.Set(getAllString(mString2))
    print b.intersection(c)
#    print intersect(getAllString(mString1),getAllString(mString2))
#    print union(getAllString(mString1),getAllString(mString2))
    print b.union(c)
    print gapCount([mString2], mString1)
    print gapCount([mString3], mString1)
    print gapCount([mString4], mString1)

if __name__ == '__main__':
    demo()
