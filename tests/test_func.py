import time
import unittest
from selenium import webdriver
from selenium.webdriver import FirefoxOptions, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class UiTestMhk01(unittest.TestCase):

    def setUp(self):
        opts = FirefoxOptions()
        opts.add_argument("--headless")
        self.driver = webdriver.Firefox(options=opts)
        self.driver.get("http://localhost:8000")

    def test_title(self):
        assert self.driver.title == "МШК-01"

    def test_h2(self):
        assert self.driver.find_element(By.TAG_NAME, "h2").text == "Конфигуратор МШК-01"

    def test_condition_1(self):
        select_os_el = self.driver.find_element(By.ID, "os")
        select_os = Select(select_os_el)
        select_os.select_by_visible_text("НЕТ")

        select_td_el = self.driver.find_element(By.ID, "td")
        select_td = Select(select_td_el)
        selected_options_td = select_td.all_selected_options

        for option in selected_options_td:
            print(option.text)

        warning_container = self.driver.find_element(By.ID, "warning_container")
        assert warning_container.find_element(By.TAG_NAME, "p").text == "Замечаний нет."

    def test_condition_2(self):
        select_td_el = self.driver.find_element(By.ID, "td")

        # The second method
        # select_td = Select(select_td_el)
        # select_td.select_by_visible_text("НЕТ")
        select_td_el.click()
        select_opt_os = select_td_el.find_element(By.XPATH, "//option[@value='2']")
        select_opt_os.click()

        warning_container = self.driver.find_element(By.ID, "warning_container")
        # print(warning_container.find_element(By.TAG_NAME, "p").text)
        # time.sleep(5)
        # print(warning_container.find_element(By.TAG_NAME, "p").text)
        assert warning_container.find_element(By.TAG_NAME, "p").text == "- Отдельно стоящий механизм (ОС) должен иметь диван."

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
