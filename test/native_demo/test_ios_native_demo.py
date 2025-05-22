from test import base_test
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.options.common import AppiumOptions


class IosDemoTest(base_test.BaseTest):

    testName = 'iOS Native Demo'
    driver = None
    options = AppiumOptions()

    def setUp(self):
        super().setUp()
        self.options.set_capability('testName', self.testName)
        self.options.set_capability('app', 'cloud:com.experitest.ExperiBank')
        self.options.set_capability('bundleId', 'com.experitest.ExperiBank')
        self.options.set_capability('platformName', 'ios')
        self.options.set_capability('deviceQuery', "@os='ios' and contains(@name, 'Pro')")
        self.options.set_capability('appiumVersion', "1.22.3")
        self.driver = webdriver.Remote(self.getUrl(), options=self.options)

    def testIosNativeDemo(self):
        self.driver.find_element(By.XPATH, "//*[@name='usernameTextField']").send_keys('company')
        self.driver.find_element(By.XPATH, "//*[@name='passwordTextField']").send_keys('company')
        self.driver.find_element(By.XPATH, "//*[@name='loginButton']").click()
        self.driver.find_element(By.XPATH, "//*[@name='makePaymentButton']").click()
        self.driver.find_element(By.XPATH, "//*[@name='phoneTextField']").send_keys('1234567')
        self.driver.find_element(By.XPATH, "//*[@name='nameTextField']").send_keys('Jon Snow')
        self.driver.find_element(By.XPATH, "//*[@name='amountTextField']").send_keys('50')
        self.driver.find_element(By.XPATH, "//*[@name='countryButton']").click()
        self.driver.find_element(By.XPATH, "//*[@name='Switzerland']").click()
        self.driver.find_element(By.XPATH, "//*[@name='sendPaymentButton']").click()
        self.driver.find_element(By.XPATH, "//*[@name='Yes']").click()

    def tearDown(self):
        print ('Report URL: ' + self.driver.capabilities["digitalai:reportUrl"])
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
