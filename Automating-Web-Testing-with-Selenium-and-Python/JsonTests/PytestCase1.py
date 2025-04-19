import pytest

from TestCase1 import execute_test_case
from TestCase1 import test_data


@pytest.mark.parametrize("test_case", test_data["testCases"])
def test_Json_Login(test_case):
    execute_test_case(test_case)
