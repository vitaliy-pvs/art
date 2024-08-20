import unittest
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By

opts = FirefoxOptions()
opts.add_argument("--headless")


class UiTestMhk01(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(options=opts)

    def test_title(self):
        driver = self.driver
        driver.get("http://195.58.54.98")
        # assert "МШК-01" in driver.title
        assert driver.title == "МШК-01"

    def test_h2(self):
        driver = self.driver
        driver.get("http://195.58.54.98")
        assert driver.find_element(By.TAG_NAME, "h2").text == "Конфигуратор МШК-01"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
