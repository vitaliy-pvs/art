from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://195.58.54.98/")
assert "МШК-01" in driver.title
driver.quit()
