from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import time
import ctypes
driver = webdriver.Chrome()
#Change Website SEC Site Accordingly
driver.get("https://www.sec.gov/rules/sro/cboebzx.htm")
input_element = driver.find_element_by_name("UserName")
input_element.send_keys("Michael.Forbes@ihsmarkit.com")
input_element = driver.find_element_by_name("Password")
input_element.send_keys("@#@Hciv223@#@")
driver.find_element_by_class_name("submit").click()
driver.minimize_window()
i = 0
while i == 0:
    RESULTS_LOCATOR = "(//*[@id='chronlist']/tbody/tr[4]/td[2])"
    dates = driver.find_elements(By.XPATH, RESULTS_LOCATOR)
    RESULTS_LOCATOR0 = "(//*[@id='chronlist']/tbody/tr[4]/td[3]/b[1])"
    bodies = driver.find_elements(By.XPATH, RESULTS_LOCATOR0)
    results = []
    for date in dates:
        current_pub = date.text
        today = datetime.datetime.now()
        now = today.strftime("%b. %d, %Y")
        results.append(current_pub)
    resultz = results[0]

    def f(resultz):
        if resultz == now:
            return("New Publication")
        else:
            return("No New Publication")

    for body in bodies:
        sum_text = body.text
        if sum_text.find("VanEck") >= 0 and f(resultz) == "New Publication":
            action = "Review!!!"
            print(action)
            print(datetime.datetime.now())
            ctypes.windll.user32.MessageBoxW(0, "CHECK BTC!!! on SEC https://www.sec.gov/rules/sro/nysearca.htm", "Review!!!", 1)
            i = 1
        else:
            print("No New Updates")
            i = 0
            print(datetime.datetime.now())
            time.sleep(15)
            driver.refresh()


