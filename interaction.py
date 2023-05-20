# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 22:49:39 2023

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

from Module_cc import CC_Class
from class_fichier import C_Fichier


class SpotifyGenerator:
    def __init__(self, password="yourPassword"):
        self.driver = ""
        self.email = ""
        self.password = password
        self.extenstion = "xk-en"
        self.cc_file_name = "cc.txt"
        self.regected_cc_file_name = "cc_regected.txt"
        self.data_file = "data.txt"

    def get_driver(self):
        
        #self.extenstion = input("Enter Your Country :")
        '''
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
        driver = webdriver.Firefox(firefox_profile=firefox_profile)
        '''
        '''
        
        chromedriver_path = 'chromedriver.exe'
        brave_path = '/usr/bin/brave-browser'
        option = webdriver.ChromeOptions()
        option.binary_location = brave_path
        driver = webdriver.Chrome(executable_path=chromedriver_path, options=option)
        '''
        driver = webdriver.Chrome()
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get("https://www.spotify.com/signup")
        print("NOTE: DRIVER CONNECTED")
        return

    def get_Email_from_yopmail(self):

        yopmail_url = 'https://yopmail.com/email-generator'
        response = requests.get(yopmail_url)
        html_content = response.content

        soup = BeautifulSoup(html_content, 'html.parser')

        email_element_container = soup.find(id="geny")
        email = email_element_container.get_text()
        self.email = email
        print("NOTE: EMAIL DONE")
        return

    def go_to_signup(self):
        try:
            WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".Button-sc-1dqy6lx-0.jjtmnk.sibxBMlr_oxWTfBrEz2G"))
            )
        finally:
            go_signup = self.driver.find_elements(
                By.CSS_SELECTOR, ".Button-sc-1dqy6lx-0.jjtmnk.sibxBMlr_oxWTfBrEz2G")
            if len(go_signup) != 0:
                go_signup[0].click()
                
        return
    
    
    def remove_descrections(self):

        policy_close_button = self.driver.find_elements(
            By.CSS_SELECTOR, ".onetrust-close-btn-handler.onetrust-close-btn-ui.banner-close-button.ot-close-icon")
        if len(policy_close_button) != 0:
            policy_close_button[0].click()
            print("NOTE: REMOVED POLICY")

        try:
            cookies_button = self.driver.find_element(
                By.ID, "onetrust-accept-btn-handler")
        except:
            print('NOTE: No cookies there')
        else:
            cookies_button.click()
            print("REMOVE COOKIES")

        return

    def fill_displayed_name(self):
        display_name_field = self.driver.find_element(By.ID, "displayname")
        display_name_field.send_keys("your display name")
        return

    def fill_password(self):
        password = "yourPassword"
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(password)
        self.password = password
        return

    def fill_date_of_birth(self):
        day_field = self.driver.find_element(By.ID, "day")
        day_field.send_keys("01")

        year_field = self.driver.find_element(By.ID, "year")
        year_field.send_keys("1990")

        month_dropdown = Select(self.driver.find_element(By.ID, "month"))
        month_dropdown.select_by_index(2)
        return

    def fill_email_and_confrm(self):
        try:
            WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located((By.ID, "email"))
            )
        finally:
            email_field = self.driver.find_element(By.ID, "email")
            email_field.send_keys(self.email)

        try:
            confirm_email_field = self.driver.find_element(By.ID, "confirm")
        except:
            print('NOTE: No confirm email there')
        else:
            confirm_email_field.send_keys(self.email)
        return

    def fill_gender(self):
        gender_radiobutton = self.driver.find_elements(By.CSS_SELECTOR, ".Indicator-sc-hjfusp-0.benotq")
        if len(gender_radiobutton) != 0:
            gender_radiobutton[0].click()
        else:
            gender_radiobutton2 = self.driver.find_elements(By.CSS_SELECTOR, ".Indicator-sc-hjfusp-0.dFGMcY")
            gender_radiobutton2[0].click()

    def submit_form(self):
        # submit the form
        submit_button = self.driver.find_elements(
            By.CSS_SELECTOR, ".ButtonInner-sc-14ud5tc-0.dqLIWu.encore-bright-accent-set.SignupButton___StyledButtonPrimary-cjcq5h-1.jazsmO")
        submit_button[0].click()
        print("NOTE: FORM SUBMITED")
        return

    def cc_premium_activator(self):
        try:
            WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".mh-header-primary.svelte-vf0pv9"))
            )
        finally:
            go_premium = self.driver.find_elements(
                By.CSS_SELECTOR, ".mh-header-primary.svelte-vf0pv9")
            if len(go_premium) != 0:
                go_premium[0].click()
                try:
                    WebDriverWait(self.driver, 100).until(
                        EC.presence_of_element_located(
                            (By.CSS_SELECTOR, ".ButtonInner-sc-14ud5tc-0.eUyfdq.sc-jrsJWt.gNCnmw.sc-kEqXSa.exRBIa"))
                    )
                finally:
                    go_to_plan_page = self.driver.find_elements(
                        By.CSS_SELECTOR, ".ButtonInner-sc-14ud5tc-0.eUyfdq.sc-jrsJWt.gNCnmw.sc-kEqXSa.exRBIa")
                    if len(go_to_plan_page) != 0:
                        go_to_plan_page[0].click()
                        try:
                            WebDriverWait(self.driver, 100).until(
                                EC.presence_of_element_located(
                                    (By.CSS_SELECTOR, ".Indicator-hjfusp-0.hJZAEs"))
                            )
                        finally:
                            self.remove_descrections()
                            try:
                                go_to_cc_form = self.driver.find_elements(
                                    By.CSS_SELECTOR, ".Indicator-hjfusp-0.hJZAEs")
                            except:  
                                self.try_ccs()
                            else:
                                if len(go_to_cc_form) > 2:
                                    go_to_cc_form[1].click()
                                elif len(go_to_cc_form) == 2:
                                    go_to_cc_form[0].click()
    
                                self.try_ccs()

            # driver.quit()
            print("NOTE: ACCOUNT IS CREATED")
        return

    def try_ccs(self):
        cc_file = C_Fichier(self.cc_file_name)
        regected_cc_file = C_Fichier(self.regected_cc_file_name)
        ccs = cc_file.Fichier_to_Liste()
        regected_ccs = regected_cc_file.Fichier_to_str()
        for cc in ccs:
            cc_splited = cc.split("|")
            print(cc_splited)
            if cc_splited[0] not in regected_ccs:
                credit_card = CC_Class(self.driver, cc_splited)
                credit_card.fill_cc_input()
                try:
                    WebDriverWait(self.driver, 100).until(
                        EC.invisibility_of_element_located((By.CSS_SELECTOR, 'div[data-testid="loading-indicator"]'))
                    )
                finally:
                    try:
                        self.driver.find_element(
                            By.CSS_SELECTOR, "Wrapper-sc-62m9tu-0.jieDxt.encore-negative-set")
                    except:
                        print("NOTE: CC REGECTED")
                        regected_cc_file.str_to_fichier(cc)
                    else:
                        self.export_account_data()
                        print("NOTE: ACCOUNT IS CREATED, CHECK THE FILE {}".format(
                            self.data_file))
                        return
            else:
                continue

    def export_data(self):
        return [self.email, self.password]

    def close_tab(self):
        self.driver.quit()

    def main_spotify(self):
        self.get_driver()
        self.get_Email_from_yopmail()
        self.remove_descrections()
        self.fill_email_and_confrm()
        self.fill_password()
        self.fill_displayed_name()
        self.fill_date_of_birth()
        self.fill_gender()
        self.submit_form()
        self.cc_premium_activator()
    pass
