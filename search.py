import os
from hillclimber import HILLCLIMBER

# for i in range(5):
#     os.system('"C:\\Users\\Jared Krogsrud\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" generate.py')
#     os.system('"C:\\Users\\Jared Krogsrud\\AppData\\Local\\Programs\\Python\\Python310\\python.exe" simulate.py')

hc = HILLCLIMBER()

hc.Evolve()
