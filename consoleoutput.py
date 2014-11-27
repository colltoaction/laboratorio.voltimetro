import time

class ConsoleOutput:
	def __init__(self):
		pass

	def __enter__(self):
		return self

	def __exit__(self, type, value, traceback):
		pass

	def __call__(self, value):
		print("{:.6f} {}".format(time.time(), value))

