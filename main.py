import time
import random
import os

from utils import get_driver, change_vpn_location
from selenium.webdriver.common.by import By

# settings for ranking bot
MIN_DELAY = 3
MAX_DELAY = 7

def add_scroll(driver, scroll_delay=3, up_direcation=True):
    # Get the height of the webpage
    scroll_height = driver.execute_script("return document.body.scrollHeight")

    # Get the current scroll position
    current_position = 0

    while current_position < scroll_height:
        # Calculate the next scroll position
        next_position = min(current_position + 500, scroll_height)
        # Scroll to the next position
        driver.execute_script(f"window.scrollTo(0, {next_position});")
        time.sleep(scroll_delay)
        if up_direcation:
            driver.execute_script(f"window.scrollTo(0, {next_position-200});")
            # Wait for the specified delay
            time.sleep(scroll_delay)
        # Update the current scroll position
        current_position = next_position

if __name__ == '__main__':
     while True:
        try:
            change_vpn_location()
            driver = get_driver(headless=False)
            driver.get('https://devdefenders.com/')
            add_scroll(driver)
            categories = ['development', 'artificial-intelligence']
            pages = [f'https://devdefenders.com/category/{category}/' for category in categories]
            for page in pages:
                driver.get(page)
                add_scroll(driver)
                time.sleep(2)
                blogs = driver.find_elements(By.CSS_SELECTOR, 'h2.is-title > a')
                urls = [blog.get_attribute('href') for blog in blogs]
                for url in urls:
                    driver.get(url)
                    add_scroll(driver,scroll_delay=5, up_direcation=False)
                    time.sleep(random.randint(MIN_DELAY, MAX_DELAY))
            driver.quit()
        except Exception as e:
            print(e)
            os.system("expressvpn disconnect")
