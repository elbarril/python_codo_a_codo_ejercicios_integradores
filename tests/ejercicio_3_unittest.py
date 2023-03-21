import unittest
from ejercicio_3 import count_words

TEST_EJERCICIO_3 = True
DISABLE_MESSAGE = "Test {} disable"
TEST_SENTENCE = "Hola mundo. Esto es Codo a Codo, aprendiendo Python."
TEST_WORDS_RESULT = {
    "hola": 1,
    "mundo": 1,
    "esto": 1,
    "es": 1,
    "codo": 2,
    "a": 1,
    "aprendiendo": 1,
    "python": 1
}

class Ejercicio3Test(unittest.TestCase):
    @unittest.skipUnless(TEST_EJERCICIO_3, DISABLE_MESSAGE.format("Ejercicio 3"))
    def test_count_words(self):
        frequency_words = count_words(TEST_SENTENCE)
        self.assertEqual(frequency_words, TEST_WORDS_RESULT)