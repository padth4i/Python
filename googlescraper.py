from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="/Users/shiva/Desktop/chromedriver.exe")

driver.get("https://www.google.in")
driver.find_element_by_xpath("""//*[@id="lst-ib"]""").send_keys("FOSS@Amrita\ue007")

links = driver.find_elements_by_class_name("r")

for i in range (10):
    print(links[i].text)
