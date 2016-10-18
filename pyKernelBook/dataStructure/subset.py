#    For more info, see www.kernel-methods.net
import numpy

def getAllSubset(elements):
    tmp = []
    tmp.append([])
    for i in range(len(elements)):
        tmp.extend(getSubset(elements,i))
    return tmp

def getSubset(elements, length):
    tmp = []
    for i in range(len(elements)):
        k = elements[i:i+1]
        if length == 1:
            tmp.append(k)
        else:
            rest = elements[i+1:]
            for j in getSubset(rest, length-1):
                tmp.append(k + j)
    return tmp

def demo():
    A = [1, 8, 2, 3, 2, 9, 2, 4]
    print getSubset(A,0)
    print getSubset(A,1)
    print getSubset(A,2)
    print getSubset(A,3)
    print getSubset(A,4)
    print getSubset(A,5)
    print getSubset(A,6)
    print getSubset(A,7)

if __name__ == '__main__':
    demo()

