from iterator import get_pins_status, toint, to5vrange, DiscardRepeated
from diskpersistance import DiskPersistance
from consoleoutput import ConsoleOutput
from consolebaroutput import ConsoleBarOutput
from contextlib import ExitStack

class Pipeline:
	def __init__(self):
		self.middlewares = []
		self.handlers = []

	def middleware(self, middleware):
		self.middlewares.append(middleware)
		return self

	def handler(self, handler):
		self.handlers.append(handler)
		return self

	def read(self, stream):
		with ExitStack() as stack:
			for handler in self.handlers:
				stack.enter_context(handler)
			
			for value in stream():
				pipedvalue = self.apply_middlewares(value)
				if pipedvalue is None:
					continue
				for handler in self.handlers:
					handler(pipedvalue)

	def apply_middlewares(self, value):
		pipedvalue = value
		for middleware in self.middlewares:
			pipedvalue = middleware(pipedvalue)
			if pipedvalue is None:
				return None
		return pipedvalue

Pipeline() \
	.middleware(toint) \
	.middleware(to5vrange) \
	.handler(DiskPersistance()) \
	.handler(ConsoleOutput()) \
	.read(get_pins_status)

