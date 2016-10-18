import numpy

def anovaKernelFunction(x,z,m,s):
    dim = numpy.size(x,0)
    if (dim <= m):
        return anovaKernelFunction(x,z,m-1,s)
    if (((s==0) and (m>=0)) or (m==0)):
            return 1
    if m<s:
        return 0
    return numpy.dot(x[m], z[m]) * anovaKernelFunction(x,z,m-1,s-1) + anovaKernelFunction(x,z,m-1,s)
           
def demo():
    x = numpy.array([[1, 2, 3, 4, 5.3, 6, 7.1],[1, 2, 3, 4, 5.3, 6, 7.1]])
    z = numpy.array([[2, 3, 2, 1, 3.2, 2, 3.4],[2, 3, 2, 1, 3.2, 2, 3.4]])
    print anovaKernelFunction(x,z,3,0.1)

if __name__ == '__main__': 
    demo()
