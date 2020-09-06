import time
from appium.webdriver.common.touch_action import TouchAction
from utilities.testdata import *
from LogFeature.LogRecord import LogData
from utilities.access import BaseOne
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestSetOne(BaseOne, LogData):

    def test_login(self):
        self.driver.implicitly_wait(4)
        log = self.getLogger()
        self.driver.find_element_by_id("com.amazon.mShop.android.shopping:id/sign_in_button").click()
        log.info("Clicked on sign in button")
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//android.widget.EditText[@resource-id='ap_email_login']")))
        element.click()
        self.driver.find_element_by_xpath("//android.widget.EditText[@resource-id='ap_email_login']").send_keys(mobile)
        log.info("Mobile number entered in login box")
        self.driver.find_element_by_xpath("//android.widget.Button[@resource-id='continue']").click()
        log.info("Clicked on Continue button")
        self.driver.find_element_by_xpath(
            "//android.widget.CheckBox[@resource-id='auth-signin-show-password-checkbox']").click()
        checkbox = self.driver.find_element_by_xpath(
            "//android.widget.CheckBox[@resource-id='auth-signin-show-password-checkbox']")
        assert checkbox.is_selected() == False
        log.info("Show password check box unselected")
        self.driver.find_element_by_xpath("//android.widget.EditText[@resource-id='ap_password']").click()
        self.driver.find_element_by_xpath("//android.widget.EditText[@resource-id='ap_password']").send_keys(pwd)
        log.info("Password entered in password box")
        self.driver.find_element_by_xpath("//android.widget.Button[@resource-id='signInSubmit']").click()
        log.info("Clicked on Login button")
        element1 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "com.amazon.mShop.android.shopping:id/action_bar_burger_icon")))
        element1.click()
        log.info("clicked on Burger icon")
        time.sleep(1)
        TouchAction(self.driver).press(x=194, y=1752).move_to(x=175, y=1038).release().perform()
        element2 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[@text='Settings']")))
        element2.click()
        log.info("Settings section selected from Menu")
        element3 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[contains(@text, 'Sign out')]")))
        element3.click()
        log.info("Clicked on SignOut button")
        self.driver.find_element_by_xpath("//android.widget.Button[@text='SIGN OUT']").click()
        log.info("SIGN OUT from Confirm Sign Out pop up")
        WebDriverWait(self.driver, 12).until(
            EC.presence_of_element_located((By.ID, "com.amazon.mShop.android.shopping:id/signin_to_yourAccount")))
        signup_page = self.driver.find_element_by_id("com.amazon.mShop.android.shopping:id/signin_to_yourAccount").text
        assert (signup_page == "Sign in to your account")
        log.info("Redirected to Sign Up page")

    def test_search_product(self):
        self.driver.implicitly_wait(4)
        log = self.getLogger()
        self.driver.find_element_by_id("com.amazon.mShop.android.shopping:id/sign_in_button").click()
        log.info("Clicked on sign in button")
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//android.widget.EditText[@resource-id='ap_email_login']")))
        element.click()
        self.driver.find_element_by_xpath("//android.widget.EditText[@resource-id='ap_email_login']").send_keys(
            mobile)
        log.info("Mobile number entered in login box")
        self.driver.find_element_by_xpath("//android.widget.Button[@resource-id='continue']").click()
        log.info("Clicked on Continue button")
        self.driver.find_element_by_xpath(
            "//android.widget.CheckBox[@resource-id='auth-signin-show-password-checkbox']").click()
        checkbox = self.driver.find_element_by_xpath(
            "//android.widget.CheckBox[@resource-id='auth-signin-show-password-checkbox']")
        assert checkbox.is_selected() == False
        log.info("Show password check box unselected")
        self.driver.find_element_by_xpath("//android.widget.EditText[@resource-id='ap_password']").click()
        self.driver.find_element_by_xpath("//android.widget.EditText[@resource-id='ap_password']").send_keys(pwd)
        log.info("Password entered in password box")
        self.driver.find_element_by_xpath("//android.widget.Button[@resource-id='signInSubmit']").click()
        log.info("Clicked on Login button")
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "com.amazon.mShop.android.shopping:id/rs_search_src_text")))
        element.click()
        log.info("Clicked in serach box")
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "com.amazon.mShop.android.shopping:id/rs_search_src_text")))
        self.driver.find_element_by_id("com.amazon.mShop.android.shopping:id/rs_search_src_text").send_keys(
            "65-inch TV")
        log.info("Entering product name[65-inch TV] in search box which we want to purchase")
        search_tv = self.driver.find_elements_by_xpath(
            "//android.widget.TextView[@resource-id='com.amazon.mShop.android.shopping:id/iss_search_dropdown_item_text']")
        log.info("Below are the auto suggestive options")
        for i in search_tv:
            search_prd = i.text
            log.info(search_prd)
        search_tv[3].click()
        log.info("Selecting third suggested option")
        search_results = self.driver.find_elements_by_xpath(
            "//android.widget.TextView[@resource-id='com.amazon.mShop.android.shopping:id/item_title']")
        search_results[2].click()
        log.info("Selecting second TV product")
        TestSetOne.scroll(self)
        log.info("scrolling down for selecting by button")
        self.driver.find_element_by_xpath("//android.view.View[@resource-id='buyNowCheckout']").click()
        log.info("Clicked on By Now button")
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//android.widget.Button[@text='Continue']")))
        log.info("Redirected to Delivery options page")
        delivery_opt_screen = self.driver.find_element_by_xpath(
            "//android.view.View[@text='Choose your delivery options']").text
        assert (delivery_opt_screen == 'Choose your delivery options')
        log.info(" heading on Delivery options page was validated")
        log.info(delivery_opt_screen)
        continue_button = self.driver.find_element_by_xpath("//android.widget.Button[@text='Continue']").text
        assert (continue_button == 'Continue')
        log.info("Continue button on Delivery options page was validated")
        log.info(continue_button)

    def scroll(self):
        time.sleep(3)
        for i in range(15):
            print(i)
            end_y = 1100
            try:
                value = self.driver.find_element_by_xpath(
                    "//android.view.View[@resource-id='buyNowCheckout']").is_displayed()
                if value is True:
                    break
            except:
                self.driver.swipe(470, 1460, 470, end_y, 300)
                self.driver.implicitly_wait(2)
                continue
