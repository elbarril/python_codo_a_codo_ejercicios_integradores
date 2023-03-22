from unittest import skipUnless
from unittest.mock import patch
from unittest import TestCase
from io import StringIO

from ejercicio_5 import get_int_iteratively, get_int_recursively

TEST_EJERCICIO_5 = True
DISABLE_MESSAGE = "Test {} disabled"
TEST_WRONG_INPUT_VALUE = "a"
TEST_RIGHT_INPUT_VALUE = "1"
TEST_VALUE_ERROR_MESSAGE = "The value is not a number. Try again.\n"

class Ejercicio5Test(TestCase):
    @skipUnless(TEST_EJERCICIO_5, DISABLE_MESSAGE.format("Ejercicio 5"))
    def test_get_int_iteratively(self):
        with patch('builtins.input', side_effect=[TEST_WRONG_INPUT_VALUE, TEST_RIGHT_INPUT_VALUE]):
            with patch('sys.stdout', new = StringIO()) as output:
                self.assertEqual(get_int_iteratively(), int(TEST_RIGHT_INPUT_VALUE))
                self.assertEqual(output.getvalue(), TEST_VALUE_ERROR_MESSAGE)
        
    @skipUnless(TEST_EJERCICIO_5, DISABLE_MESSAGE.format("Ejercicio 5"))
    def test_get_int_recursively(self):
        with patch('builtins.input', side_effect=[TEST_WRONG_INPUT_VALUE, TEST_RIGHT_INPUT_VALUE]):
            with patch('sys.stdout', new = StringIO()) as output:
                self.assertEqual(get_int_recursively(), int(TEST_RIGHT_INPUT_VALUE))
                self.assertEqual(output.getvalue(), TEST_VALUE_ERROR_MESSAGE)