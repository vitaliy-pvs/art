import unittest
from selenium import webdriver
from selenium.webdriver import FirefoxOptions

opts = FirefoxOptions()
opts.add_argument("--headless")


class UiTestMhk01(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(options=opts)

    def test_page(self):
        driver = self.driver
        driver.get("http://195.58.54.98")
        assert "МШК-01" in driver.title

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
