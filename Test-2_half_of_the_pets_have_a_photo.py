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

@pytest.fixture()
def go_to_my_pets():

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

def test_half_of_the_pets_have_a_photo(go_to_my_pets):
   '''Поверяем, что на странице со списком моих питомцев хотя бы половина питомцев имеет фото'''

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))

   # Сохраняем в переменную ststist элементы статистики
   statist = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

   # Сохраняем в переменную images элементы с атрибутом img
   images = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')

   # Получаем количество питомцев из данных статистики
   num = statist[0].text.split('\n')
   num = num[1].split(' ')
   num = int(num[1])

   # Находим половину от количества питомцев
   half = num // 2

   # Находим количество питомцев с фотографией
   num_а_photos = 0
   for i in range(len(images)):
      if images[i].get_attribute('src') != '':
         num_а_photos += 1

   # Проверяем что количество питомцев с фотографией больше или равно половине количества питомцев
   assert num_а_photos >= half
