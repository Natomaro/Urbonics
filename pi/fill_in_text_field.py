# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# driver = webdriver.Firefox(executable_path=r'C:\Users\Class2018\Desktop\geckodriver-v0.24.0-win64\geckodriver.exe')
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')
driver = webdriver.Firefox(firefox_binary=binary)

driver.get('http://127.0.0.1:8000/users/')

username = driver.find_element_by_id("Username")
password = driver.find_element_by_id("Email address")

username.send_keys("nick_test_march12")
password.send_keys("dick@gmail.com")

driver.find_element_by_name("POST").click()