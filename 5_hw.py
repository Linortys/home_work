from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

def open_url():
    driver.get("https://www.saucedemo.com/")
    a = driver.find_element(By.ID, 'user-name')
    b = driver.find_element(By.ID, 'password')
    c = driver.find_element(By.ID, 'login-button')

    if a is None:
        print("Один из элементов не найден")
    elif b is None:
        print("Один из элементов не найден")
    elif c is None:
        print("Один из элементов не найден")
    else:
        print('Элементы найдены')

open_url()