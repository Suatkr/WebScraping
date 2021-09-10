from selenium import webdriver 
import time 
from selenium.webdriver.common.keys  import Keys


browser= webdriver.Chrome("/Users/Suat KIR/Desktop/chromedriver")

browser.get("https://www.linkedin.com/home")

browser.fullscreen_window()
time.sleep(2)

login= browser.find_element_by_xpath("/html/body/nav/div/a[2]")
login.click()
time.sleep(3)

email= browser.find_element_by_xpath("//*[@id='username']")

password=browser.find_element_by_xpath("//*[@id='password']")

email.send_keys("ahmetsuat4128@gmail.com")
password.send_keys("2205492314228")

loginbutton=browser.find_element_by_xpath("//*[@id='organic-div']/form/div[3]/button")
loginbutton.click()
time.sleep(5)
#//*[@id="global-nav-search"]/div/button/li-icon

search_bar=browser.find_element_by_xpath("//*[@id='global-nav-search']/div/button")
search_bar.click()
write=browser.find_element_by_xpath("//*[@id='global-nav-typeahead']/input")
time.sleep(2)
write.send_keys("Birkan karabağ")
write.send_keys(Keys.RETURN)
time.sleep(5)
birkan=browser.find_element_by_xpath("//*[@id='main']/div/div/div[1]/div/div/div/a/div[2]/div[1]/div/span[1]/span/a/span/span[1]")
birkan.click()
birkan.send_keys(Keys.RETURN)
time.sleep(5)

contacts=browser.find_element_by_class_name("class='global-nav__primary-link-text'")
contacts.click()
time.sleep(5)
agım=browser.find_element_by_class_name("mn-community-summary__entity-info")
contacts.click()
time.sleep(5)

time.sleep(5)
browser.close()




