from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

def getDriver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sanbox")
    options.add_experimental_option("excludeSwitches",
                                    ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")


    driver = webdriver.Chrome(options)
    driver.get("http://automated.pythonanywhere.com/login")
    return driver

def cleanText(text):
    output = text.split(": ")[1]
    return output

def main():
    driver = getDriver()
    time.sleep(1)
    element = driver.find_element(by="id", value="id_username").send_keys("automated")
    time.sleep(1)
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    time.sleep(1)
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    time.sleep(1)
    print(driver.current_url)
    time.sleep(2)
    while True:
        now = datetime.now()
        name = now.strftime("%y-%m-%d.%H-%M-%S") + ".txt"
        tempFile = open(name, "w")
        element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
        text = cleanText(element.text)
        tempFile.write(text)
        tempFile.close()
        time.sleep(2)

    time.sleep(1)
    return cleanText(element.text)

main()