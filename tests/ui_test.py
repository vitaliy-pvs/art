from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://localhost:8000")
assert "МШК-01" in driver.title
driver.quit()
