from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

browser=webdriver.Chrome("/Users/Suat KIR/Desktop/chromedriver")
browser.get("https://www.linkedin.com/home")
browser.fullscreen_window()
time.sleep(2)

login=browser.find_element_by_xpath("/html/body/nav/div/a[2]")
login.click()
time.sleep(2)

email=browser.find_element_by_xpath("//*[@id='username']")
password=browser.find_element_by_xpath("//*[@id='password']")
email.send_keys("ahmetsuat4128@gmail.com")
password.send_keys("2205492314228")
login=browser.find_element_by_xpath("//*[@id='organic-div']/form/div[3]/button")
login.click()
time.sleep(5)

contact=browser.find_element_by_xpath("//*[@id='ember21']")
contact.click()
time.sleep(7)
kisiler=browser.find_element_by_class_name("mn-community-summary__entity-info")
kisiler.click()
time.sleep(10)

for i in range(1,3):
    browser.execute_script("window.scrollTo(0,document.bodyscrollHeight)")
    time.sleep(3)

followers=browser.find_elements_by_class_name("mn-connection-card__details")
followerlist=[]

for follower in followers:
    followerlist.append(follower.text)

with open("follower.text","w",encoding="utf-8") as file:
    for follower in followerlist:
        file.write(follower+"/n")


time.sleep(3)




browser.close()

