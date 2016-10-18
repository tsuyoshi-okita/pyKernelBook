import numpy

def anovaKernelFunction(x,z,d):
    value=0;
    if d==0:
        return 1
    for s in range(1,d+1):
        value += numpy.power(-1, s+1) / d * anovaKernelFunction(x,z,d-s)* anovaKernelFunctionComp(x,z,d-s)
    return value

def anovaKernelFunctionComp(x,z,d):
    n = numpy.size(x,1)
    value = 0
    for i in range(n):
        value += numpy.power(x[d-1][i] * z[d-1][i], d)
    return value

def demo():
    x = numpy.array([[1, 2, 3, 4, 5.3, 6, 7.1],[1, 2, 3, 4, 5.3, 6, 7.1]])
    z = numpy.array([[2, 3, 2, 1, 3.2, 2, 3.4],[2, 3, 2, 1, 3.2, 2, 3.4]])
    print anovaKernelFunction(x,z,3)

if __name__ == '__main__': 
    demo()

