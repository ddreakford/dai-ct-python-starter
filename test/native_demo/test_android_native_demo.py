from test import base_test
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from appium.options.common import AppiumOptions


class AndroidDemoTest(base_test.BaseTest):

    testName = 'Android Native Demo'
    driver = None
    options = AppiumOptions()

    def setUp(self):
        super().setUp()
        self.options.set_capability('testName', self.testName)
        self.options.set_capability('appPackage', 'com.experitest.ExperiBank')
        self.options.set_capability('appActivity', '.LoginActivity')
        self.options.set_capability('platformName', 'android')
        self.options.set_capability('deviceQuery', "@os='android' and contains(@name, 'Galaxy S2')")
        # self.options.set_capability('appiumVersion', '1.22.3')
        self.driver = webdriver.Remote(self.getUrl(), options=self.options)

    def testAndroidNativeDemo(self):
        self.driver.find_element(By.ID, 'com.experitest.ExperiBank:id/usernameTextField').send_keys('company')
        self.driver.find_element(By.ID, 'com.experitest.ExperiBank:id/passwordTextField').send_keys('company')
        self.driver.find_element(By.ID, 'com.experitest.ExperiBank:id/loginButton').click()

        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.ID, 'com.experitest.ExperiBank:id/makePaymentButton')))

        self.driver.find_element(By.ID, 'com.experitest.ExperiBank:id/makePaymentButton').click()
        self.driver.find_element(By.ID, 'com.experitest.ExperiBank:id/phoneTextField').send_keys('1234567')
        self.driver.find_element(By.ID, 'com.experitest.ExperiBank:id/nameTextField').send_keys('Jon Snow')
        self.driver.find_element(By.ID, 'com.experitest.ExperiBank:id/amountTextField').send_keys('50')
        self.driver.find_element(By.ID, 'com.experitest.ExperiBank:id/countryTextField').send_keys('Switzerland')
        self.driver.find_element(By.ID, 'com.experitest.ExperiBank:id/sendPaymentButton').click()
        self.driver.find_element(By.ID, 'android:id/button1').click()

    def tearDown(self):
        print ('Report URL: ' + self.driver.capabilities["digitalai:reportUrl"])
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
