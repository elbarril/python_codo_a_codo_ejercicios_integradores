from unittest import skipUnless
from unittest.mock import patch
from unittest import TestCase
from io import StringIO

from ejercicio_6 import Person

TEST_EJERCICIO_6 = True
DISABLE_MESSAGE = "Test {} disabled"

TEST_EMPTY_VALUE = ''
TEST_NONE_MASSAGE = str(None)+'\n'

TEST_VALID_NAME = "Emi"
TEST_VALID_AGE = 12
TEST_VALID_UID = 12345678

TEST_INVALID_NAME = 123
TEST_INVALID_AGE = 123
TEST_INVALID_UID = 123

TEST_SHOW_PERSON_ALL_FIELDS = f"name: {TEST_VALID_NAME}\nage: {TEST_VALID_AGE}\nuid: {TEST_VALID_UID}\n"
TEST_SHOW_PERSON_ALL_FIELDS_EMPTY = "name: None\nage: None\nuid: None\n"
TEST_SHOW_PERSON_AGE_UID_FIELDS_EMPTY = f"name: {TEST_VALID_NAME}\nage: None\nuid: None\n"
TEST_SHOW_PERSON_NAME_UID_FIELDS_EMPTY = f"name: None\nage: {TEST_VALID_AGE}\nuid: None\n"
TEST_SHOW_PERSON_NAME_AGE_FIELDS_EMPTY = f"name: None\nage: None\nuid: {TEST_VALID_UID}\n"
TEST_SHOW_PERSON_NAME_FIELD_EMPTY = f"name: None\nage: {TEST_VALID_AGE}\nuid: {TEST_VALID_UID}\n"
TEST_SHOW_PERSON_UID_FIELD_EMPTY = f"name: {TEST_VALID_NAME}\nage: {TEST_VALID_AGE}\nuid: None\n"
TEST_SHOW_PERSON_AGE_FIELD_EMPTY = f"name: {TEST_VALID_NAME}\nage: None\nuid: {TEST_VALID_UID}\n"

TEST_VALUE_ERROR_MESSAGE = "Wrong type parameters."
TEST_INVALID_NAME_MESSAGE = "The name is not a valid name.\n"
TEST_INVALID_AGE_MESSAGE = "The age is not a valid number.\n"
TEST_INVALID_UID_MESSAGE = "The unique ID is not a valid number.\n"

class Ejercicio6Test(TestCase):
    @skipUnless(TEST_EJERCICIO_6, DISABLE_MESSAGE.format("Ejercicio 6"))
    def test_person_with_errors(self):
        self.assertRaises(Exception,Person,TEST_INVALID_NAME)
        self.assertRaises(Exception,Person,TEST_VALID_NAME, TEST_INVALID_AGE)
        self.assertRaises(Exception,Person,TEST_VALID_NAME, TEST_VALID_AGE, TEST_INVALID_UID)
        self.assertRaises(Exception,Person,TEST_EMPTY_VALUE, TEST_INVALID_AGE)
        self.assertRaises(Exception,Person,TEST_EMPTY_VALUE, TEST_VALID_AGE, TEST_INVALID_UID)
        self.assertRaises(Exception,Person,TEST_EMPTY_VALUE, TEST_EMPTY_VALUE, TEST_INVALID_UID)
        self.assertRaises(Exception,Person,TEST_VALID_NAME, TEST_INVALID_AGE, TEST_VALID_UID)
        person = Person()
        with patch('sys.stdout', new = StringIO()) as output:
            person.name = TEST_INVALID_NAME
            self.assertEqual(output.getvalue(), TEST_INVALID_NAME_MESSAGE)
        with patch('sys.stdout', new = StringIO()) as output:
            person.age = TEST_INVALID_AGE
            self.assertEqual(output.getvalue(), TEST_INVALID_AGE_MESSAGE)
        with patch('sys.stdout', new = StringIO()) as output:
            person.uid = TEST_INVALID_UID
            self.assertEqual(output.getvalue(), TEST_INVALID_UID_MESSAGE)
        with patch('sys.stdout', new = StringIO()) as output:
            print(person.name)
            self.assertEqual(output.getvalue(), TEST_NONE_MASSAGE)
        with patch('sys.stdout', new = StringIO()) as output:
            print(person.age)
            self.assertEqual(output.getvalue(), TEST_NONE_MASSAGE)
        with patch('sys.stdout', new = StringIO()) as output:
            print(person.uid)
            self.assertEqual(output.getvalue(), TEST_NONE_MASSAGE)
        
    @skipUnless(TEST_EJERCICIO_6, DISABLE_MESSAGE.format("Ejercicio 6"))
    def test_person_without_errors(self):
        with patch('sys.stdout', new = StringIO()) as output:
            person = Person()
            with patch('sys.stdout', new = StringIO()) as output:
                person.show()
            self.assertEqual(output.getvalue(), TEST_SHOW_PERSON_ALL_FIELDS_EMPTY)

            person.name = TEST_VALID_NAME
            self.assertEqual(person.name, TEST_VALID_NAME)
            person.age = TEST_VALID_AGE
            self.assertEqual(person.age, TEST_VALID_AGE)
            person.uid = TEST_VALID_UID
            self.assertEqual(person.uid, TEST_VALID_UID)
            self.assertEqual(person.is_adult(), False)

            person = Person(name=TEST_VALID_NAME, uid=TEST_VALID_UID)
            with patch('sys.stdout', new = StringIO()) as output:
                person.show()
            self.assertEqual(output.getvalue(), TEST_SHOW_PERSON_AGE_FIELD_EMPTY)

            person = Person(name=TEST_VALID_NAME, age=TEST_VALID_AGE)
            with patch('sys.stdout', new = StringIO()) as output:
                person.show()
            self.assertEqual(output.getvalue(), TEST_SHOW_PERSON_UID_FIELD_EMPTY)

            person = Person(age=TEST_VALID_AGE, uid=TEST_VALID_UID)
            with patch('sys.stdout', new = StringIO()) as output:
                person.show()
            self.assertEqual(output.getvalue(), TEST_SHOW_PERSON_NAME_FIELD_EMPTY)

            person = Person(age=TEST_VALID_AGE)
            with patch('sys.stdout', new = StringIO()) as output:
                person.show()
            self.assertEqual(output.getvalue(), TEST_SHOW_PERSON_NAME_UID_FIELDS_EMPTY)

            person = Person(uid=TEST_VALID_UID)
            with patch('sys.stdout', new = StringIO()) as output:
                person.show()
            self.assertEqual(output.getvalue(), TEST_SHOW_PERSON_NAME_AGE_FIELDS_EMPTY)

            person = Person(name=TEST_VALID_NAME)
            with patch('sys.stdout', new = StringIO()) as output:
                person.show()
            self.assertEqual(output.getvalue(), TEST_SHOW_PERSON_AGE_UID_FIELDS_EMPTY)

            person = Person(name=TEST_VALID_NAME, age=TEST_VALID_AGE, uid=TEST_VALID_UID)
            with patch('sys.stdout', new = StringIO()) as output:
                person.show()
            self.assertEqual(output.getvalue(), TEST_SHOW_PERSON_ALL_FIELDS)