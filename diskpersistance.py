import time

class DiskPersistance:
	def __init__(self):
		self.file = open("export-{:.6f}.txt".format(time.time()), "w")

	def __enter__(self):
		return self

	def __exit__(self, type, value, traceback):
		self.file.close()

	def __call__(self, value):
		self.file.write("{:.6f} {}\n".format(time.time(), value))

