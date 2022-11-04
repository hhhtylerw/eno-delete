from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Change this for your machine
s = Service(r"C:\Users\hhhtylerw\chromedriver.exe")

# Change this to the name of the cards you want to delete
# Leave blank for all cards
keyword = "uber"

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging','enable-automation'])

driver = webdriver.Chrome(service=s, options=options)
driver.get("https://myaccounts.capitalone.com/VirtualCards")

input("Ready?")

while True:
    try:
        driver.get("https://myaccounts.capitalone.com/VirtualCards")
        time.sleep(10)
        driver.find_element('xpath', '//*[@id="gng-input-0"]').send_keys(keyword)
        time.sleep(2)
        driver.find_element('xpath', '/html/body/div[1]/div/div/div/c1-ease-root/c1-ease-commerce-virtual-cards-manager-toggle-container/c1-ease-commerce-virtual-cards-manager-container/div/c1-ease-commerce-virtual-cards-manager/div/c1-ease-commerce-virtual-cards-manager-table-view/div/div/c1-ease-table/div[2]/c1-ease-row[1]').click()
        time.sleep(4)
        driver.find_element('css selector', '#cdk-step-content-0-0 > c1-ease-commerce-edit-screen > div > button').click()
        time.sleep(2)
        driver.find_element('css selector', '#cdk-step-content-0-1 > c1-ease-commerce-delete-confirm-screen > div > button.deleteButton.c1-ease-button--full-width.c1-ease-button.c1-ease-button--destructive').click()
    except:
        print('error, continuing...')
    time.sleep(1)