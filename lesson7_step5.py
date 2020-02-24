from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

if __name__ == '__main__':
    try:
        driver = webdriver.Chrome()
        driver.get("http://suninjuly.github.io/math.html")

        element_x = driver.find_element_by_id("input_value")
        x = element_x.text
        y = calc(x)

        input_field = driver.find_element_by_id("answer")
        input_field.send_keys(y)

        checkbox_im_not_robot = driver.find_element_by_css_selector("[for='robotCheckbox']")
        checkbox_im_not_robot.click()

        radioboton_robots_rule = driver.find_element_by_css_selector("[for='robotsRule']")
        radioboton_robots_rule.click()

        submit_button = driver.find_element_by_css_selector(".container button")
        submit_button.click()
    finally:
        time.sleep(5)
        driver.quit()

