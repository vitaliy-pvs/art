from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://195.58.54.98")
assert "МШК-01" in driver.title
driver.get("http://195.58.54.98/art04/")
assert "МШК-04" in driver.title
driver.get("http://195.58.54.98/art06/")
assert "МШК-06" in driver.title
driver.quit()
print("Test successful!")
