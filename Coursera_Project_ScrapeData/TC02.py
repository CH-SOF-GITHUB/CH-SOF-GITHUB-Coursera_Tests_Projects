import csv
import re
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def scrapeOlympedia():
    # create a new Chrome browser instance
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    try:
        # navigate to the Olympedia website
        driver.get("https://www.olympedia.org/statistics/medal/country")
        # make the browser window full screen
        driver.maximize_window()
        # wait for 3 seconds for loading page
        time.sleep(3)
        # declare a web elements By Games "years"
        year_dd = driver.find_element(By.ID, "edition_select")
        # declare a web element By athlete gender "gender"
        gender_dd = driver.find_element(By.ID, "athlete_gender")
        # collect all the years in the dropdown
        year_options = year_dd.find_elements(By.TAG_NAME, "option")
        # collect all the gender in the dropdown
        gender_options = gender_dd.find_elements(By.TAG_NAME, "option")
        # Array to store the data
        usa_lst = []
        # loop through gender options and years
        for gender in gender_options[1:]:
            gender.click()
            time.sleep(2)
            # print gender value
            gender_val = gender.get_attribute("text")
            for year in year_options[2:]:
                year.click()
                time.sleep(1)
                the_soup = BeautifulSoup(driver.page_source, 'html.parser')
                year_val = year.get_attribute('text')
                try:
                    head = the_soup.find(href=re.compile('USA'))
                    medal_values = head.find_all_next('td', limit=5)
                    # the first index is the link with the country abbreviation and flag
                    val_lst = [x.string for x in medal_values[1:]]
                except:
                    # we address years team USA did not compete with this option
                    val_lst = ['0' for x in range(4)]
                # append the values to the list
                val_lst.append(gender_val)
                val_lst.append(year_val)
                usa_lst.append(val_lst)
        # close the driver
        driver.quit()
        # print the data
        print("usa_lst[30]: ", usa_lst[30])
        print("usa_lst[40]: ", usa_lst[40])
        # loop through all of our compiled data, usa_lst, and write it out to a CSV
        output_f = open('output.csv', 'w', newline='')
        try:
            output_writer = csv.writer(output_f)
            # write the header
            output_writer.writerow(["Gold", "Silver", "Bronze", "Total", "Gender", "Year"])
            for row in usa_lst:
                output_writer.writerow(row)
        except:
            pass
        finally:
            output_f.close()
    except Exception as e:
        print(e)
        driver.quit()


if __name__ == '__main__':
    scrapeOlympedia()
