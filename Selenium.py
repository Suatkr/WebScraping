
"""
from selenium import webdriver 
import time

browser= webdriver.Chrome("/Users/Suat KIR/Desktop/chromedriver")

browser.get("https://www.forbes.com/the-worlds-most-valuable-brands/#25803520119c")
#print(browser.page_source)
#print(browser.title)

browser.fullscreen_window()
time.sleep(2)
browser.get("https://www.forbes.com/companies/apple/?list=powerful-brands/&sh=1d7dd1515355")
time.sleep(2)

browser.set_window_size(1200,1400)
browser.save_screenshot("/Users/Suat KIR/Desktop/selenium.jpeg")
time.sleep(2)
browser.back()
time.sleep(2)

browser.close()
"""