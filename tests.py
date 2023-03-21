import unittest
import tests.ejercicio_1_unittest as EJ1_test

if __name__ == '__main__':
    loader = unittest.TestLoader()
    tests = [
        loader.loadTestsFromModule(EJ1_test)
    ]
    suite = unittest.TestSuite()
    suite.addTests(tests)
    
    runner = unittest.TextTestRunner(verbosity=3)
    results = runner.run(suite)