import numpy as np
import matplotlib.pyplot as plt


# backLegSensorValues = np.load('data/backLegSensorValues.npy')
# frontLegSensorValues = np.load('data/frontLegSensorValues.npy')
#
# plt.plot(backLegSensorValues, label='BackLeg', linewidth=5)
# plt.plot(frontLegSensorValues, label='FrontLeg', linewidth=2)
# plt.legend()
# plt.show()

targetAngles = np.load('data/targetAngles.npy')

plt.plot(targetAngles)
plt.show()