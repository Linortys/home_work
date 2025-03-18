from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

def open_url():
    driver.get("https://www.saucedemo.com/")


open_url()
username_find = driver.find_element(By.ID, 'user-name')
pass_find = driver.find_element(By.ID, 'password')
submit_find = driver.find_element(By.ID, 'login-button')


if submit_find is None:
    print("Один из элементов не найден")
elif username_find is None:
    print("Один из элементов не найден")
elif pass_find is None:
    print("Один из элементов не найден")
else:
    print('Элементы найдены')