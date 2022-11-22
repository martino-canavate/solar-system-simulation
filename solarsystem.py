import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math
import matplotlib
matplotlib.use('TKAgg')

class planet(object):
	def __init__(self, x, y, mass, velocitx, velocity, radius, col, name):
		self.positi  = np.array([x ,y])
		self.previouspositi = np.array([0.0, 0.0])
		self.mass = mass
		self.velocit = np.array([velocitx, velocity])
		self.col = col
		self.force = np.array([0.0, 0.0])
		self.acceleration = np.array([0.0, 0.0])
		self.accelerationt = np.array([0.0, 0.0])
		self.radius = radius
		self.g = (6.67408 * 10**(-11))
		self.kinetic = 0.0
		self.potential = 0.0	
		self.daycount = 0
		self.planetname = name



class universe(object):
	def __init__(self, t, T, planets, width):
		self.planets = planets
		self.t = t
		self.T = T
		self.width = width
		self.g = (6.67408 * 10**(-11))
		self.patches = []
		self.totalenergy = 0

	def magnitude(self, planet):
		total = math.sqrt(planet[0]**2 + planet[1]**2)
		return total

	def unitvector(self, planet):
		total = planet/self.magnitude(planet)
		return total


	def positionupdate(self):
		self.totalenergy = 0
		for planet in self.planets:
			planet.previouspositi = planet.positi
			for otherplanet in self.planets:
				if (planet.mass != otherplanet.mass):
					a = self.g*planet.mass*otherplanet.mass/(self.magnitude(otherplanet.positi-planet.positi)**2)
					planet.force += (a*self.unitvector(otherplanet.positi-planet.positi))
					planet.potential = -(1/2)*(a)
			at = planet.force/planet.mass
			planet.velocit += (1/6)*(2*at + 5*planet.accelerationt - planet.acceleration)*self.T
			planet.positi += planet.velocit*self.T +(1/6)*(4*planet.accelerationt - planet.acceleration)*self.T**2
			planet.force = 0
			planet.acceleration = planet.accelerationt
			planet.accelerationt = at
			planet.kinetic = (1/2)*planet.mass*(self.magnitude(planet.velocit))**2
			self.totalenergy += planet.potential + planet.kinetic
			self.daycycle(planet)
			print(str(planet.acceleration[0]) + "###" + str(planet.accelerationt[0]))

	def daycycle(self, planet):
		if ((planet.previouspositi[0] > 0) and (planet.positi[0] < 0)):
			planet.daycount += 1
			print("---------------- " + planet.name + "has passed " + planet.daycount + "days")
		else: print(str(planet.previouspositi[0]) + "-----" + str(planet.positi[0]))

	def init(self):
		return self.patches

	def animate(self, i):
		self.i = i
		self.positionupdate()
		print("The energy in the system is: " + str(self.totalenergy))
		for c in range(0, len(self.planets)):
			self.patches[c].center = (self.planets[c].positi[0], self.planets[c].positi[1])
		return self.patches


	def run(self):
		fig = plt.figure()
		ax = plt.axes()
		ax.axis('scaled')
		ax.set_xlim(-self.width, self.width)
		ax.set_ylim(-self.width, self.width)

		for i in range(0, len(self.planets)):
			self.patches.append(plt.Circle((self.planets[i].positi[0], self.planets[i].positi[1]), self.planets[i].radius, color = self.planets[i].col , animated = True))
		for i in range(0, len(self.patches)):
			ax.add_patch(self.patches[i])

		anim = FuncAnimation(fig, self.animate, init_func = self.init, frames = int(self.t) , interval = 60, blit = True)
		plt.show()

