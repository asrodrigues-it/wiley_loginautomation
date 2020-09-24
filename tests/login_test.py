import os
import time
from selenium import webdriver
from page_objects.login_page import login_page
from page_objects.home_page import home_page

project_path = os.path.abspath(os.curdir)
driver = webdriver.Firefox(executable_path=project_path + '/drivers/geckodriver.exe')
driver.implicitly_wait(10)
driver.get('https://teamshift-qa.crossknowledge.com')
driver.find_element_by_xpath(login_page.btn_entrar).click()
driver.find_element_by_id(login_page.txt_email).send_keys('asrodrigues.it@gmail.com')
driver.find_element_by_xpath(login_page.btn_proximo).click()
driver.find_element_by_xpath(login_page.txt_senha).send_keys('WLS2020qa')
driver.find_element_by_xpath(login_page.btn_login).click()
driver.find_element_by_xpath(home_page.lbl_nome_usuario)
time.sleep(5)
driver.quit()