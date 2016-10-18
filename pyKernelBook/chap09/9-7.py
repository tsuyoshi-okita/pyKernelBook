import numpy

def polynomialKernelFunction(x,z,d,R):
    if not(len(x) == len(z)):
        return 0
    if (d == 1):
        return numpy.dot(x,z) + R
    else:
        return polynomialKernelFunction(x,z,d-1,R) * (numpy.dot(x,z) + R)

def demo():
    x = numpy.array([1, 2, 3, 4, 5.3, 6, 7.1])
    y = numpy.array([2, 3, 2, 1, 3.2, 2, 3.4])
    print polynomialKernelFunction(x,y,1,1)

if __name__ == '__main__': 
    demo()
