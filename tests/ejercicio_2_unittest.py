import unittest
from ejercicio_2 import get_least_common_multiple

TEST_EJERCICIO_2 = True
DISABLE_MESSAGE = "Test {} disable"
TEST_NUMBERS = [
    {"ab": (60, 48), "result": 240},
    {"ab": (12, 18), "result": 36},
    {"ab": (24, 36), "result": 72},
    {"ab": (17, 23), "result": 391},
    {"ab": (6, 2), "result": 6}
]

class Ejercicio1Test(unittest.TestCase):
    @unittest.skipUnless(TEST_EJERCICIO_2, DISABLE_MESSAGE.format("Ejercicio 2"))
    def test_get_least_common_multiple(self):
        for numbers in TEST_NUMBERS:
            number_a, number_b = numbers["ab"]
            result = numbers["result"]
            greatest_common_divisor = get_least_common_multiple(number_a=number_a, number_b=number_b)
            self.assertEqual(greatest_common_divisor, result)