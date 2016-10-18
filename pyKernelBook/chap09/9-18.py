import numpy

def anovaKernelFunction(x,z,n,d):
    DP=numpy.zeros((d,n),float)
    for m in range(n):
        DP[0,m]=1
    for s in range(1,d):
        DP[s,s-1]=0
        for m in range(s,n):
            DP[s,m]=DP[s,m-1]+(x[s-1][m]*z[s-1][m]) *DP[s-1,m-1]
    return DP[d-1,n-1]

def demo():
    x = numpy.array([[1, 2, 3, 4, 5.3, 6, 7.1],[1, 2, 3, 4, 5.3, 6, 7.1]])
    z = numpy.array([[2, 3, 2, 1, 3.2, 2, 3.4],[2, 3, 2, 1, 3.2, 2, 3.4]])
    print anovaKernelFunction(x,z,3,2)

if __name__ == '__main__': 
    demo()

