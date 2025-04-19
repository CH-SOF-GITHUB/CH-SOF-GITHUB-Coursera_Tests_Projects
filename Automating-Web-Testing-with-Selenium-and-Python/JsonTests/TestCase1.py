import json

# Load data from json
with open("test_data.json", "r") as file:
    test_data = json.load(file)
    print(test_data)


def execute_test_case(test_case):
    print(f"Executing f{test_case['description']}")
    input_data = test_case['input']
    expectedOutput = test_case['expectedOutput']
    # actual result
    actualOutput = simulate_test_case(input_data)
    # verify test case
    assert expectedOutput == actualOutput, f"{test_case['id']} failed"
    print(f"{test_case['id']} passed.")


def simulate_test_case(input_data):
    if input_data['username'] == "test_user" and input_data['password'] == "securePass123":
        return {
            "status": "success",
            "message": "Login successful"
        }
    else:
        return {
            "status": "failure",
            "message": "Invalid credentials"
        }


for testCase in test_data['testCases']:
    execute_test_case(testCase)
