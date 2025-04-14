from selenium import webdriver

from section4class import *

# setup web driver
driver = webdriver.Chrome()
url = "https://techstepacademy.com/training-ground"
script = "window.open('https://techstepacademy.com/training-ground', '_blank');"
text = "Hello, world!"


def test_training_ground():
    status = "failed"
    try:
        # create an instance of the Training_ground class
        training_ground = Training_ground(driver, url)
        # open the page
        training_ground.open()
        # execute the script to open a new tab
        training_ground.execute_script(script)
        # input a text
        training_ground.saisir_text_input(text)
        # get the value of the input field
        input_value = training_ground.get_input_value()
        print("Input value: " + input_value)

        # if all methods pass, update status
        status = "passed"
        print(f"Test {status}")
    except Exception as e:
        print(f"An error occurred: {e} and Test {status}")
    finally:
        # close the browser
        driver.quit()
        print("Browser closed.")


# execute the test function in the main block
if __name__ == "__main__":
    test_training_ground()
