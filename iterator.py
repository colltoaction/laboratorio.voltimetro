from queue import Queue
import RPi.GPIO as GPIO

eoc_pin = 37
pins = {
	0: 3,
	1: 5,
	2: 7,
	3: 11,
	4: 13,
	5: 15,
	6: 19,
	7: 21
}

queue = Queue()

def get_pins_status():
	GPIO.setmode(GPIO.BOARD)
#	GPIO.setup(pins.values(), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	GPIO.setup(eoc_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	for pin in pins.values():
		GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
	
	GPIO.add_event_detect(eoc_pin, GPIO.RISING, callback=read_pins_callback)

	while True:
		yield queue.get()
		queue.task_done()

def read_pins_callback(input_pin):
	queue.put_nowait([GPIO.input(pins[k]) for k in sorted(pins.keys())]) # + [GPIO.input(eoc_pin)])

def toint(values):
	return sum((2 * value) ** i for i, value in enumerate(values))

def to5vrange(value):
	return value / 51

class DiscardRepeated:
	def __init__(self):
		self.last = None

	def __call__(self, value):
		if value == self.last:
			return None
		self.last = value
		return value
