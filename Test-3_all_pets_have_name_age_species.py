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

def test_all_pets_have_name_age_species(go_to_my_pets):
   '''Поверяем, что на странице со списком моих питомцев, у всех питомцев есть имя, возраст и порода'''

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
   # Сохраняем в переменную pet_data элементы с данными о питомцах
   pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   # Перебираем данные из pet_data, оставляем имя, возраст, и породу остальное меняем на пустую строку
   # и разделяем по пробелу. Находим количество элементов в получившемся списке и сравниваем их
   # с ожидаемым результатом
   for i in range(len(pet_data)):
      data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
      split_data_pet = data_pet.split(' ')
      result = len(split_data_pet)
      assert result == 3