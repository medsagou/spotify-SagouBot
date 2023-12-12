# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 23:52:00 2023

@author: HP
"""
import requests
from bs4 import BeautifulSoup

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.support.ui import WebDriverWait as wait


class CC_Class:
    def __init__(self, driver="", list_info_cc=["", "", "", ""]):
        self.driver = driver
        self.number = list_info_cc[0]
        self.date = list_info_cc[1] + "/" + list_info_cc[2][2:]
        self.code = list_info_cc[-1].replace("\n", "")

    def fill_cc_input(self):
        iframe = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "iframe[data-testid='pci-frame']")
            )
        )
        self.driver.switch_to.frame(iframe)
        print("NOTE: SWITCH TO IFRAME PAYMENT")
        # time.sleep(2)
        # Retrieve the credit card number input field and fill in the value
        try:
            cc_number = self.driver.find_element(
                By.CSS_SELECTOR, "input[id='cardnumber']"
            )
        except:
            print("ERROR: CARDNUMBER NOTE FOUND")
        else:
            cc_number.send_keys(Keys.CONTROL + "a")
            cc_number.send_keys(Keys.DELETE)
            print("NOTE: CARDNUMBER INSERD")
            cc_number.send_keys(self.number)

        try:
            cc_date = self.driver.find_element(
                By.CSS_SELECTOR, "input[id='expiry-date']"
            )
        except:
            print("ERROR: EXPIRYDATE NOTE FOUND")
        else:
            cc_date.send_keys(Keys.CONTROL + "a")
            cc_date.send_keys(Keys.DELETE)
            print("NOTE: EXPIRYDATE INSERD")
            cc_date.send_keys(self.date)

        try:
            cc_v_code = self.driver.find_element(
                By.CSS_SELECTOR, "input[id='security-code']"
            )
        except:
            print("ERROR: SECURITYCODE NOTE FOUND")
        else:
            cc_v_code.send_keys(Keys.CONTROL + "a")
            cc_v_code.send_keys(Keys.DELETE)
            print("NOTE: SECURITYCODE INSERD")
            cc_v_code.send_keys(self.code)
        self.driver.switch_to.default_content()
        # print("try to sumbit")
        submit_button = self.driver.find_elements(
            By.CSS_SELECTOR,
            ".ButtonInner-sc-14ud5tc-0.bYgzuF.encore-bright-accent-set"
            # ".ButtonInner-sc-14ud5tc-0.bYgzuF.encore-bright-accent-set.sc-ksdxAp.fdYigH",
        )
        if len(submit_button) != 0:
            submit_button[0].click()
        else:
            print("NOTE: ERROR IN THE BY BUTTON")
        print("NOTE: CC FORM SUBMITED")
