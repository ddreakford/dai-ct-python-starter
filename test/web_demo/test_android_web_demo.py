from test import base_test
from appium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from appium.options.common import AppiumOptions


class LocalAndroidTest(base_test.BaseTest):

    testName = 'Android Web Demo'
    driver = None
    options = AppiumOptions()

    def setUp(self):
        super().setUp()
        self.options.set_capability('testName', self.testName)
        self.options.set_capability('platformName', 'android')
        self.options.set_capability('deviceQuery', "@os='android' and contains(@name, 'Galaxy S2')")
        self.options.set_capability('appiumVersion', '1.22.3')
        self.options.set_capability('browserName', 'chrome')

        self.driver = webdriver.Remote(self.getUrl(), options=self.options)

    def testAndroidWebDemo(self):
        self.driver.get('https://demo-bank.ct.digital.ai')

        WebDriverWait(self.driver, 10)\
            .until(expected_conditions.presence_of_element_located((By.XPATH, "//*[@data-auto='login']")))

        self.driver.find_element(By.XPATH, "//*[@data-auto='username']//input").send_keys('company')
        self.driver.find_element(By.XPATH, "//*[@data-auto='password']//input").send_keys('company')
        self.driver.find_element(By.XPATH, "//*[@data-auto='login']").click()

        self.driver.find_element(By.XPATH, "//*[@data-auto='transfer-funds']").click()

        self.driver.find_element(By.XPATH, "//input[@name='NAME']").send_keys('John')
        self.driver.find_element(By.XPATH, "//input[@name='PHONE']").send_keys('1-234-5678')
        self.driver.find_element(By.XPATH, "//input[@name='AMOUNT']").send_keys('1000')
        self.driver.find_element(By.XPATH, "//*[@data-auto='country']").click()
        self.driver.find_element(By.XPATH, "//*[string-length() > 0]").click()
        self.driver.find_element(By.XPATH, "//*[@data-auto='transfer-button']").click()


    def tearDown(self):
        print ('Report URL: ' + self.driver.capabilities["digitalai:reportUrl"])
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
