import time

import pyperclip as pyperclip
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import lesson7_step5 as func


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = browser.find_element_by_id("book")

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    button.click()

    x = browser.find_element_by_id("input_value").text
    y = func.calc(x)

    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(y)

    button_submit = browser.find_element_by_id("solve")
    button_submit.click()

    # Копирование числа из алерта в буфер обмена
    alert = browser.switch_to.alert
    alert_text = alert.text
    addToClipBoard = alert_text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)
finally:
    time.sleep(5)
    browser.quit()

