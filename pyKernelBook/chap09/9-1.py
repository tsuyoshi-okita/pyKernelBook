import numpy

def polynomialKernelFunction(x,z,d,R):
    if not(len(x) == len(z)):
        return -1
    return numpy.power(numpy.dot(x,z) + R, d)

def demo():
    x = numpy.array([1, 2, 3, 4, 5.3, 6, 7.1])
    y = numpy.array([2, 3, 2, 1, 3.2, 2, 3.4])
    print polynomialKernelFunction(x,y,1.,1.)

if __name__ == '__main__': 
    demo()
