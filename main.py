import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# базовый url
base_url = "https://www.saucedemo.com/"

# добавить опции
options = webdriver.ChromeOptions()

# оставить браузер открытым
options.add_experimental_option("detach", True)

# автоматическая загрузка драйвера
service = ChromeService(ChromeDriverManager().install())

# открытие браузера с параметрами
driver_chrome = webdriver.Chrome(
    options=options,
    service=service
)

# переход по url в браузере
driver_chrome.get(base_url)

# команда для открытия окна в максимальном для монитора разрешении
driver_chrome.maximize_window()

# пауза 1 секунда
time.sleep(1)

# найти на странице элемент под id "user-name"
user_name = driver_chrome.find_element(By.ID, "user-name")
# установить в поле значение "standard_user"
user_name.send_keys("standard_user")
print("Ввод логина.")

# пауза 1 секунда
time.sleep(1)

# найти на странице элемент под id "password"
password = driver_chrome.find_element(By.ID, "password")
# установить в поле значение "secret_sauce"
password.send_keys("secret_sauce")
print("Ввод пароля.")

# пауза 1 секунда
time.sleep(1)

# найти на странице элемент под id "login-button"
login_button = driver_chrome.find_element(By.ID, "login-button")
# нажать на кнопку
login_button.click()
print("Нажатие на кнопку Login.")

# пауза 1 секунда
time.sleep(1)

# найти 6 элементов и добавить их в корзину
driver_chrome.find_element(
    By.ID, "add-to-cart-sauce-labs-backpack"
).click()

time.sleep(1)

driver_chrome.find_element(
    By.ID, "add-to-cart-sauce-labs-bike-light"
).click()

time.sleep(1)

# скролл 700 вниз
driver_chrome.execute_script("window/scrollTo(0,700)")
time.sleep(1)

driver_chrome.find_element(
    By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
).click()

time.sleep(1)

driver_chrome.find_element(
    By.ID, "add-to-cart-sauce-labs-fleece-jacket"
).click()

time.sleep(1)

driver_chrome.find_element(
    By.ID, "add-to-cart-sauce-labs-onesie"
).click()

time.sleep(1)

driver_chrome.find_element(
    By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)"
).click()

time.sleep(1)

# вернуть обратно
driver_chrome.execute_script("window/scrollTo(0,0)")
time.sleep(1)
print("Добавлено 6 элементов в корзину.")

# перейти в корзину
driver_chrome.find_element(
    By.XPATH, "//a[@data-test='shopping-cart-link']"
).click()
print("Осуществлен переход в корзину.")

# пауза 1 секунда
time.sleep(1)

# расширить возможности для действий драйвера
actions = ActionChains(driver_chrome)

# найти последний элемент в списке
element = driver_chrome.find_element(
    By.XPATH, "//a[@data-test='item-3-title-link']"
)

# перейти к последнему элементу
actions.move_to_element(element).perform()
print("Осуществлен переход к последнему элементу корзины.")

# пауза 2 секунды
time.sleep(2)

# закрыть окно браузера
driver_chrome.close()
print("Окно закрыто.")
