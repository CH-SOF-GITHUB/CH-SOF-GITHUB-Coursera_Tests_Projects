import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def scrapeBooks():
    # create a new chrome browser instance
    driver = webdriver.Chrome()
    try:
        # navigate to the-internet web site login
        driver.get("https://books.toscrape.com/")
        # make the browser window full screen
        driver.maximize_window()
        # wait for 3 seconds
        time.sleep(3)
        # declare two tables titles, prices
        titles = []
        prices = []
        # loop through the first 2 pages
        for page in range(1, 3):
            # find all the book titles and prices on the page
            books = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
            for book in books:
                title = book.find_element(By.CSS_SELECTOR, "h3 > a").get_attribute("title")
                price = book.find_element(By.CSS_SELECTOR, "p.price_color").text
                titles.append(title)
                prices.append(price)
            # click on the next button to go to the next page
            if page < 2:
                next_button = driver.find_element(By.CSS_SELECTOR, "li.next > a")
                next_button.click()
                time.sleep(2)
        # print the titles and prices
        for title, price in zip(titles, prices):
            print(f"Title: {title}, Price: {price}")

        # save the data to a file
        saveContent = "Title, Price\n"
        for title, price in zip(titles, prices):
            saveContent += f'"{title}", "{price}"\n'
        with open(file="Books.csv", mode="w", encoding="UTF-8") as file:
            file.write(saveContent)
    except Exception as e:
        print(e)
    finally:
        # close the browser
        driver.quit()


if __name__ == '__main__':
    scrapeBooks()
