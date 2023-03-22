from unittest import skipUnless, skip
from unittest.mock import patch
from unittest import TestCase
from io import StringIO

from ejercicio_7 import Person, Account
from tests.ejercicio_6_unittest import TEST_SHOW_PERSON_ALL_FIELDS_EMPTY

TEST_EJERCICIO_7 = True
DISABLE_MESSAGE = "Test {} disabled"

TEST_AMOUNT_TO_DEPOSIT = 100
TEST_AMOUNT_TO_EXTRACT = 50

class Ejercicio7Test(TestCase):
    def setUp(self):
        self.person = Person()

    @skip("Work in progress")
    @skipUnless(TEST_EJERCICIO_7, DISABLE_MESSAGE.format("Ejercicio 7"))
    def test_account_with_errors(self):
        pass
        
    @skipUnless(TEST_EJERCICIO_7, DISABLE_MESSAGE.format("Ejercicio 7"))
    def test_account_without_errors(self):
        account = Account(self.person)
        with patch('builtins.input', side_effect=[TEST_AMOUNT_TO_DEPOSIT, TEST_AMOUNT_TO_EXTRACT]):
            with patch('sys.stdout', new = StringIO()) as output:
                account.deposit(input())
                print(account.amount, end="")
            self.assertEqual(output.getvalue(), str(TEST_AMOUNT_TO_DEPOSIT))
            
            amount = account.extract(input())
            
            with patch('sys.stdout', new = StringIO()) as output:
                print(amount, end="")
            self.assertEqual(output.getvalue(), str(TEST_AMOUNT_TO_EXTRACT))
            
            with patch('sys.stdout', new = StringIO()) as output:
                print(account.amount, end="")
            self.assertEqual(output.getvalue(), str(TEST_AMOUNT_TO_DEPOSIT - TEST_AMOUNT_TO_EXTRACT))
            
            with patch('sys.stdout', new = StringIO()) as output:
                titular = account.titular
                titular.show()
            self.assertEqual(output.getvalue(), TEST_SHOW_PERSON_ALL_FIELDS_EMPTY)