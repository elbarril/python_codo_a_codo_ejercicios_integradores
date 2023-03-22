from unittest import TestCase, skipUnless
from ejercicio_3 import count_words
from ejercicio_4 import get_most_frequent_word

TEST_EJERCICIO_4 = True
DISABLE_MESSAGE = "Test {} disable"
TEST_SENTENCE = "Hola mundo. Esto es Codo a Codo, aprendiendo Python."
TEST_WORD_RESULT = ("codo", 2)

class Ejercicio4Test(TestCase):
    @skipUnless(TEST_EJERCICIO_4, DISABLE_MESSAGE.format("Ejercicio 4"))
    def test_get_most_frequent_word(self):
        frequency_words = count_words(TEST_SENTENCE)
        most_frequent_word = get_most_frequent_word(frequency_words)
        self.assertEqual(most_frequent_word, TEST_WORD_RESULT)