import numpy
import matplotlib.pyplot


backLegSensorValues = numpy.load('data/backLegSensorValues.npy')
frontLegSensorValues = numpy.load('data/frontLegSensorValues.npy')

matplotlib.pyplot.plot(backLegSensorValues, label='BackLeg', linewidth=5)
matplotlib.pyplot.plot(frontLegSensorValues, label='FrontLeg', linewidth=2)
matplotlib.pyplot.legend()
matplotlib.pyplot.show()