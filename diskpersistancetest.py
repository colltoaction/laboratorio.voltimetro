from iterator import get_pins_status, measure
from diskpersistance import DiskPersistance
from consoleoutput import ConsoleOutput
from contextlib import ExitStack

def read(*handlers):
	with ExitStack() as stack:
		for handler in handlers:
			stack.enter_context(handler)
		
		for value in get_pins_status():
			for handler in handlers:
				handler(value)

read(DiskPersistance(), ConsoleOutput())

