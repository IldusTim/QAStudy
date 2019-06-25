# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import math
from selenium.webdriver.support.ui import Select
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


link = "http://suninjuly.github.io/explicit_wait2.html"
opt = webdriver.ChromeOptions()
opt.add_experimental_option('w3c', False)
browser = webdriver.Chrome(chrome_options=opt)
browser.implicitly_wait(5, 0.5)
browser.get(link)

button = browser.find_element_by_id("book")
price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"10000 RUR"))
button.click()

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser.find_element_by_class_name("btn-primary").click()

# new_window = browser.window_handles[1]
# browser.switch_to.window(new_window)

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)
browser.find_element_by_id("answer").click()
browser.find_element_by_id("answer").send_keys(y)
browser.find_element_by_id("solve").click()