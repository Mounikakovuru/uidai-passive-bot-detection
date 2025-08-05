from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://localhost:3000")
time.sleep(10)  # simulate user browsing
