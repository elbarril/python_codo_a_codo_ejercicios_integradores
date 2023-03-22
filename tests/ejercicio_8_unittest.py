from unittest import skipUnless, skip
from unittest.mock import patch
from unittest import TestCase
from io import StringIO

from ejercicio_8 import YoungAccount
from ejercicio_7 import Person

TEST_EJERCICIO_8 = True
DISABLE_MESSAGE = "Test {} disabled"

TEST_YOUNG_ACCOUNT_MESSAGE = "Young Account"

TEST_TITULAR_NAME = "Emi"
TEST_TITULAR_AGE = 32
TEST_TITULAR_UID = 12345432

TEST_ACCOUNT_INITIAL_AMOUNT = 0
TEST_YOUNG_ACCOUNT_BONIFICATION = .5
TEST_FORMATED_BONIFICATION = "50%"

TEST_AMOUNT_TO_DEPOSIT = 100
TEST_AMOUNT_TO_EXTRACT = 30

TEST_SHOW_TITULAR = f"name: {TEST_TITULAR_NAME}\nage: {TEST_TITULAR_AGE}\nuid: {TEST_TITULAR_UID}\n"
TEST_SHOW_YOUNG_ACCOUNT = f"{TEST_YOUNG_ACCOUNT_MESSAGE}\n{TEST_FORMATED_BONIFICATION}\n"

class Ejercicio8Test(TestCase):
    def setUp(self):
        self.titular = Person(TEST_TITULAR_NAME, TEST_TITULAR_AGE, TEST_TITULAR_UID)

    @skip("Work in progress")
    @skipUnless(TEST_EJERCICIO_8, DISABLE_MESSAGE.format("Ejercicio 8"))
    def test_young_account_with_errors(self):
        pass
        
    @skipUnless(TEST_EJERCICIO_8, DISABLE_MESSAGE.format("Ejercicio 8"))
    def test_young_account_without_errors(self):
        young_account = YoungAccount(titular=self.titular, amount=TEST_ACCOUNT_INITIAL_AMOUNT, bonification=TEST_YOUNG_ACCOUNT_BONIFICATION)
        
        with patch('sys.stdout', new = StringIO()) as output:
            young_account.show()
        self.assertEqual(output.getvalue(), str(TEST_SHOW_YOUNG_ACCOUNT))

        with patch('sys.stdout', new = StringIO()) as output:
            young_account.titular.show()
        self.assertEqual(output.getvalue(), str(TEST_SHOW_TITULAR))

        with patch('sys.stdout', new = StringIO()) as output:
            print(young_account.amount, end="")
        self.assertEqual(output.getvalue(), str(TEST_ACCOUNT_INITIAL_AMOUNT))

        young_account.deposit(TEST_AMOUNT_TO_DEPOSIT)

        with patch('sys.stdout', new = StringIO()) as output:
            print(young_account.amount, end="")
        self.assertEqual(output.getvalue(), str(TEST_AMOUNT_TO_DEPOSIT))
        
        extracted_amount = young_account.extract(TEST_AMOUNT_TO_EXTRACT)
        with patch('sys.stdout', new = StringIO()) as output:
            print(extracted_amount, end="")
        self.assertEqual(output.getvalue(), str(TEST_AMOUNT_TO_EXTRACT))

        with patch('sys.stdout', new = StringIO()) as output:
            print(young_account.amount, end="")
        self.assertEqual(output.getvalue(), str(TEST_AMOUNT_TO_DEPOSIT - TEST_AMOUNT_TO_EXTRACT))