import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver_url = "/usr/bin/chromedriver"

driver = webdriver.Chrome(executable_path=driver_url)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("http://secure-retreat-92358.herokuapp.com/")
# data = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div[5]/div[1]/div[1]/div/div[3]/a[1]")
# data = driver.find_element_by_css_selector('a[title="Special:Statistics"]')
# print(data.tag_name)
# # data.click()

# alloport = driver.find_element_by_link_text("All portals")
# alloport.click()
name = driver.find_element_by_name("fName")
l_name = driver.find_element_by_name("lName")
email = driver.find_element_by_name("email")
name.send_keys("Sardar Badar")
l_name.send_keys("Saghir")
email.send_keys("badardani11@gmail.com")
email.send_keys(Keys.ENTER)
time.sleep(300)

driver.close()
driver.quit()
