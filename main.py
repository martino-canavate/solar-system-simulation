from solarsystem import planet
from solarsystem import universe
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
import matplotlib
matplotlib.use('TKAgg')

#define the central star of thwe system
sun = planet(0.0, 0.0, 1.989*10**30, 0.0, 0.0,40000000000, 'y', "Sun")

#function to set the initial velocity of orbiting bodies depending on the distance form the main star
def initvelocity(radius):
	print("initial velocity" + str(-math.sqrt(sun.g*sun.mass/radius)))
	return (-math.sqrt(sun.g*sun.mass/radius))

meteorito = planet(100000000090 , -778.57*10**9, 1.8982*10**32, 0.0, -initvelocity(7.8*10**9), 33895000000, 'b', "Meteorito")
mercury = planet(0.0 , 58*10**9, 3.285*10**23, initvelocity(58*10**9), 0.0, 5389500000, 'r', "Mercury")
venus = planet(0.0 , 108.2*10**9, 4.867*10**24, initvelocity(108.2*10**9), 0.0, 7389500000, 'y', "Venus")
earth = planet(0.0 , 149.6*10**9, 5.972*10**24, initvelocity(149.6*10**9), 0.0, 9389500000, 'b', "Earth")
mars = planet(0.0 , 228*10**9, 6.39*10**23, initvelocity(228*10**9), 0.0, 638950000, 'r', "Mars")
jupiter = planet(0.0 , 778.57*10**9, 1.8982*10**27, initvelocity(778.57*10**9), 0.0, 338950000000, 'b', "Jupiter")
saturn = planet(0.0 , 1.43*10**12, 5.6834*10**26, initvelocity(1.43*10**12), 0.0, 338950000000, 'y', "Saturn")
uranus = planet(0.0 , 2.875*10**12, 8.681*10**25, initvelocity(2.875*10**12), 0.0, 338950000000, 'g', "Uranus")
neptune = planet(0.0 , 4.50*10**12, 1.02413*10**26, initvelocity(4.50*10**12), 0.0, 338950000000, 'b', "Neptune")

planets = [sun, mercury, venus, earth, mars]

def main():
	test = universe(100000, 50000.0, planets, 228*10**9*2.1)
	test.run()

main()