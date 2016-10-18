import numpy

def allsubsetKernelFunction(x,z,n):
    if not(len(x) == len(z)):
        return -1
    value = 1
    for i in range(0,n+1):
        value *= (1 + x[i] * z[i])
    return value

def demo():
    x = numpy.array([1, 2, 3, 4, 5.3, 6, 7.1])
    y = numpy.array([2, 3, 2, 1, 3.2, 2, 3.4])
    print allsubsetKernelFunction(x,y,2)

if __name__ == '__main__': 
    demo()
