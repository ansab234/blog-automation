from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
import random

def get_driver(headless=True):
    options = Options()
    if headless:
        options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def change_vpn_location():
    locations = ['Argentina', 'Bahamas', 'Bermuda', 'Bolivia', 'Brazil', 'Canada', 'Cayman Islands', 'Chile', 'Colombia', 'Costa Rica', 'Cuba', 'Dominican Republic', 'Ecuador', 'Guatemala', 'Honduras', 'Jamaica', 'Mexico', 'Panama', 'Peru', 'Puerto Rico', 'Trinidad and Tobago', 'United States', 'Uruguay', 'Venezuela', 'Albania', 'Andorra', 'Armenia', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Georgia', 'Germany', 'Greece', 'Hungary', 'Iceland', 'Ireland', 'Isle of Man', 'Italy', 'Jersey', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta', 'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'North Macedonia', 'Norway', 'Poland', 'Portugal', 'Romania', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland', 'Turkey', 'Ukraine', 'United Kingdom', 'Australia', 'Bangladesh', 'Bhutan', 'Brunei Darussalam', 'Cambodia', 'Guam', 'Hong Kong', 'India', 'Indonesia', 'Japan', 'Kazakhstan', 'Laos', 'Macau', 'Malaysia', 'Mongolia', 'Myanmar', 'Nepal', 'New Zealand', 'Philippines', 'Singapore', 'South Korea', 'Sri Lanka', 'Taiwan', 'Thailand', 'Uzbekistan', 'Vietnam', 'Algeria', 'Egypt', 'Ghana', 'Kenya', 'Lebanon', 'Morocco', 'South Africa']
    os.system('expressvpn disconnect')
    os.system(f"expressvpn connect '{random.choice(locations)}'")
    time.sleep(2)

def add_scroll(driver):
    # Set the delay between scrolls (in seconds)
    scroll_delay = 1

    # Get the height of the webpage
    scroll_height = driver.execute_script("return document.body.scrollHeight")

    # Start scrolling from top to bottom
    while True:
        # Scroll down by the height of the window
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait for the specified delay
        time.sleep(scroll_delay)
        # Calculate the new scroll height
        new_scroll_height = driver.execute_script("return document.body.scrollHeight")
        # Break the loop if the scroll height doesn't change (reached the bottom)
        if new_scroll_height == scroll_height:
            break
        scroll_height = new_scroll_height
