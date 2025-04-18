import unittest

from concurrencytest import ConcurrentTestSuite, fork_for_tests

from TestCasesPOM import TestCases001002003
from TestCasesPOM import TestTC004005


def suite():
    allSuite = unittest.TestSuite()
    allSuite.addTest(TestCases001002003('test_TC0O1'))
    allSuite.addTest(TestCases001002003('test_TC002'))
    allSuite.addTest(TestCases001002003('test_TC003'))
    #
    allSuite.addTest(TestTC004005('test_TC004'))
    allSuite.addTest(TestTC004005('test_TC005'))

    return allSuite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    suite = suite()
    concurrent_suite = ConcurrentTestSuite(suite, fork_for_tests(2))
    runner.run(suite)
