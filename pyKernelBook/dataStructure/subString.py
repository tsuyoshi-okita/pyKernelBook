import string

def getSubString(mString, spectrum):
    tmpList = []
    mString = string.lower(mString)
    if (spectrum == 0):
        tmpList = ['']
    else:
        for i in range(len(mString)-spectrum+1):
            mStringRes = ''
            for j in range(spectrum):
                mStringRes += mString[i+j]
            tmpList.append(mStringRes)
    return tmpList

def getSubSequence(mString, mers):
    tmpList = []
    mString = string.lower(mString)
    if (mers == 0):
        tmpList= ['']
    elif (mers == 1):
        for i in range(len(mString)):
            tmpList.append(mString[i])
    elif (mers == 2):
        for i in range(len(mString)):
            for j in range(i+1,len(mString)):
                tmpList.append(mString[i]+mString[j])
    elif (mers > 2):
        for i in range(len(mString)):
            mStringTmp = mString[i:]
            list = getSubSequence(mStringTmp[1:],mers-1)        
            for j in list:
                tmpList.append(mStringTmp[0] + j)
    return tmpList

def demo():
    mString = 'Kernels'
    print getSubString(mString,0)
    print getSubString(mString,1)
    print getSubString(mString,2)
    print getSubString(mString,3)
    print getSubString(mString,4)
    print getSubSequence(mString, 0)
    print getSubSequence(mString, 1)
    print getSubSequence(mString, 2)
    print getSubSequence(mString, 3)
    print getSubSequence(mString, 4)

    mString = 'statistics'
    print getSubString(mString,3)
    mString = 'computation'
    print getSubString(mString,3)
    mString = 'gatta'
    print getSubSequence(mString,2)
    print getSubSequence(mString,3)
    mString = 'cata'
    print getSubSequence(mString,2)
    print getSubSequence(mString,3)

if __name__ == '__main__':
    demo()
