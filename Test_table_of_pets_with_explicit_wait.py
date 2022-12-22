import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('C:/chromedriver1/chromedriver1.exe')

   # Переходим на страницу авторизации
   pytest.driver.get('https://petfriends.skillfactory.ru/login')
   yield
   pytest.driver.quit()

def test_show_my_pets():
   '''Проверяем, что мы перешли на страницу "Мои питомцы"'''

   # Устанавливаем явное ожидание
   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
   # Вводим email
   pytest.driver.find_element(By.ID, 'email').send_keys('egunova-o@mail.ru')

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))
   # Вводим пароль
   pytest.driver.find_element(By.ID, 'pass').send_keys('Anna-Maria.2020')

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Мои питомцы")))
   # Нажимаем на ссылку "Мои питомцы"
   pytest.driver.find_element(By.LINK_TEXT, "Мои питомцы").click()


   # Проверяем что мы перешли на страницу "Мои питомцы"
   assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'