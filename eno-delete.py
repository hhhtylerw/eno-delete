from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Change this for your machine
s = Service(r"C:\Users\hhhtylerw\chromedriver.exe")

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging','enable-automation'])

driver = webdriver.Chrome(service=s, options=options)
driver.get("https://myaccounts.capitalone.com/VirtualCards")

input("Ready?")

while True:
    try:
        driver.get("https://myaccounts.capitalone.com/VirtualCards")
        time.sleep(5)
        driver.find_element("xpath", '//*[@id="page-content"]/div/div/div/c1-ease-root/c1-ease-commerce-virtual-cards-manager-toggle-container/c1-ease-commerce-virtual-numbers-container/c1-ease-commerce-virtual-numbers/div/div/div[1]/c1-ease-commerce-card-row/div/div[2]/div[1]/div[1]/c1-ease-commerce-virtual-number-tile/div[2]/div').click()
        time.sleep(2)
        driver.find_element("xpath", '//*[@id="cdk-step-content-0-0"]/c1-ease-commerce-edit-screen/div/button').click()
        time.sleep(2)
        driver.find_element("xpath", '//*[@id="cdk-step-content-0-1"]/c1-ease-commerce-delete-confirm-screen/div/button[1]').click()
        time.sleep(2)
    except:
        print('error, continuing...')
    time.sleep(1)