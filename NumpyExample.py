import numpy

weight = [72, 100, 65, 99, 102]

height = [1.76, 1.78, 1.89, 1.55, 1.86]

numWeight = numpy.array(weight)
numHeight = numpy.array(height)

print numWeight/numHeight**2
