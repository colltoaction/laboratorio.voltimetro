from unittest import TestCase
import math
import numpy
import os
from tp import TP
import filecmp

class SinusoidalWaveTestCase(TestCase):
    def tearDown(self):
        os.remove('test/perfect_sinusoidal_result.png')

    def test_perfect_sinusoidal(self):
        tp = TP()
        tp.fetch(((t, 5 * math.sin(t)) for t in numpy.arange(0, 2 * math.pi, math.pi / 20)))
        tp.write('test/perfect_sinusoidal_result.png')
        self.assertTrue(filecmp.cmp('test/perfect_sinusoidal.png', 'test/perfect_sinusoidal_result.png'))