import unittest
import tests.ejercicio_1_unittest as EJ1_test
import tests.ejercicio_2_unittest as EJ2_test
import tests.ejercicio_3_unittest as EJ3_test

if __name__ == '__main__':
    loader = unittest.TestLoader()
    tests = [
        loader.loadTestsFromModule(EJ1_test),
        loader.loadTestsFromModule(EJ2_test),
        loader.loadTestsFromModule(EJ3_test)
    ]
    suite = unittest.TestSuite()
    suite.addTests(tests)
    
    runner = unittest.TextTestRunner(verbosity=3)
    results = runner.run(suite)