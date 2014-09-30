import numpy
import matplotlib.pyplot as plt


class TP:
	def fetch(self, inputdata):
		data = numpy.array(list(inputdata))
		plt.plot(data[:,0], data[:,1])

	def write(self, path):
		plt.savefig(path)
