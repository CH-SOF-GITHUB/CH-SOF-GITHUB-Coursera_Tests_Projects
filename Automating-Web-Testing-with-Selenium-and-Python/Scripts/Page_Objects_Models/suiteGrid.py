import time
import unittest
from multiprocessing.pool import Pool

from allTestsChromeLambdaTest import TestCasesChrome001002003
from allTestsChromeLambdaTest import TestCasesChrome004005
from allTestsFirefoxLambdaTest import TestCasesFirefox001002003
from allTestsFirefoxLambdaTest import TestCasesFirefox004005

# exécuter des tests en parallèle sur plusieurs machines et navigateurs, ce qui est utile pour des tests à grande échelle.

"""
def suiteGrid():
    suite__grid = unittest.TestSuite()
    suite__grid.addTest(suite_chrome())
    suite__grid.addTest(suite_firefox())
    return suite__grid


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    suite = suiteGrid()
    runner.run(suite)
"""


# exécuter des tests en parallèle sur plusieurs machines et navigateurs, ce qui est utile pour des tests à grande échelle.

def run_test(test_to_run):
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_to_run)


if __name__ == '__main__':
    start_time = time.time()

    # Préparer les tests avec le runner
    tests = [
        TestCasesChrome001002003("test_TC0O1"),
        TestCasesChrome001002003("test_TC002"),
        TestCasesChrome001002003("test_TC003"),
        TestCasesChrome004005("test_TC004"),
        TestCasesChrome004005("test_TC005"),
        TestCasesFirefox001002003("test_TC0O1"),
        TestCasesFirefox001002003("test_TC002"),
        TestCasesFirefox001002003("test_TC003"),
        TestCasesFirefox004005("test_TC004"),
        TestCasesFirefox004005("test_TC005")
    ]

    # multiprocessing — Process-based parallelism
    with Pool(10) as pool:
        pool.map(run_test, tests)

    runtime_in_s = time.time() - start_time
    print('\n----------------------------------------------------------------------')
    print('Total run time: {:.2f}s'.format(runtime_in_s))
    print('\n----------------------------------------------------------------------')
