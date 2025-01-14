from unittest import TestCase, skipUnless
from ejercicio_1 import get_greatest_common_divisor

TEST_EJERCICIO_1 = True
DISABLE_MESSAGE = "Test {} disabled"
TEST_NUMBERS = [
    {"ab": (60, 40), "result": 20},
    {"ab": (70, 36), "result": 2},
    {"ab": (18, 4), "result": 2},
    {"ab": (50, 10), "result": 10},
    {"ab": (6, 2), "result": 2}
]

class Ejercicio1Test(TestCase):
    @skipUnless(TEST_EJERCICIO_1, DISABLE_MESSAGE.format("Ejercicio 1"))
    def test_get_greatest_common_divisor(self):
        for numbers in TEST_NUMBERS:
            number_a, number_b = numbers["ab"]
            result = numbers["result"]
            greatest_common_divisor = get_greatest_common_divisor(number_a=number_a, number_b=number_b)
            self.assertEqual(greatest_common_divisor, result)