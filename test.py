
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import locators
import test_data
import time
import utils
host = 'https://stellarburgers.nomoreparties.site/'

class TestRegistration:

    def test_registration_with_name_not_empty_success(self):
        driver = webdriver.Chrome()
        driver.get(host)
        driver.find_element(By.XPATH,locators.MAIN_LOCATORS['login_button']).click()
        driver.find_element(By.XPATH, locators.AUTH_LOCATORS['button_sign_up']).click()
        driver.find_element(By.XPATH, locators.REG_LOCATORS['field_name']).send_keys(test_data.AUTH_DATA['name'])
        driver.find_element(By.XPATH, locators.REG_LOCATORS['field_email']).send_keys(utils.generate_email(
            name=test_data.AUTH_DATA['name'],
            surname=test_data.AUTH_DATA['surname'],
            number_stream=test_data.AUTH_DATA['number_stream']))
        driver.find_element(By.XPATH, locators.REG_LOCATORS['field_password']).send_keys(test_data.AUTH_DATA['valid_password'])
        driver.find_element(By.XPATH, locators.REG_LOCATORS['button_submit_sign_up']).click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.AUTH_LOCATORS['button_submit_sign_in'])))
        driver.quit()

    def test_registration_with_no_valid_password_unsuccess(self):
        driver = webdriver.Chrome()
        driver.get(host)
        driver.find_element(By.XPATH, locators.MAIN_LOCATORS['login_button']).click()
        driver.find_element(By.XPATH, locators.AUTH_LOCATORS['button_sign_up']).click()
        driver.find_element(By.XPATH, locators.REG_LOCATORS['field_name']).send_keys(test_data.AUTH_DATA['name'])
        driver.find_element(By.XPATH, locators.REG_LOCATORS['field_email']).send_keys(test_data.AUTH_DATA['email'])
        driver.find_element(By.XPATH, locators.REG_LOCATORS['field_password']).send_keys(test_data.AUTH_DATA['no_valid_password'])
        driver.find_element(By.XPATH, locators.REG_LOCATORS['button_submit_sign_up']).click()
        driver.find_element(By.XPATH, locators.REG_LOCATORS['input_sign_up_password_error'])
        driver.quit()

class TestAuthorization():

    def test_auth_using_login_button_success(self):
        driver = webdriver.Chrome()
        driver.get(host)
        driver.find_element(By.XPATH, locators.MAIN_LOCATORS['login_button']).click()
        driver.find_element(By.XPATH, locators.AUTH_LOCATORS['field_email']).send_keys(test_data.AUTH_DATA['email'])
        driver.find_element(By.XPATH, locators.AUTH_LOCATORS['field_password']).send_keys(test_data.AUTH_DATA['valid_password'])
        driver.find_element(By.XPATH, locators.AUTH_LOCATORS['button_submit_sign_in']).click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.MAIN_LOCATORS['button_submit_order'])))
        driver.quit()

    def test_auth_using_my_account_button_success(self):
        driver = webdriver.Chrome()
        driver.get(host)
        driver.find_element(By.XPATH, locators.MAIN_LOCATORS['button_my_profile']).click()
        driver.find_element(By.XPATH, locators.AUTH_LOCATORS['field_email']).send_keys(test_data.AUTH_DATA['email'])
        driver.find_element(By.XPATH, locators.AUTH_LOCATORS['field_password']).send_keys(test_data.AUTH_DATA['valid_password'])
        driver.find_element(By.XPATH, locators.AUTH_LOCATORS['button_submit_sign_in']).click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.MAIN_LOCATORS['button_submit_order'])))
        driver.quit()

    def test_auth_from_sign_up_page_success(self):
        driver = webdriver.Chrome()
        driver.get(host)
        driver.find_element(By.XPATH, locators.MAIN_LOCATORS['login_button']).click()
        driver.find_element(By.XPATH, locators.AUTH_LOCATORS['button_sign_up']).click()
        driver.find_element(By.XPATH, locators.REG_LOCATORS['button_sign_in']).click()
        driver.find_element(By.XPATH, locators.AUTH_LOCATORS['field_email']).send_keys(test_data.AUTH_DATA['email'])
        driver.find_element(By.XPATH, locators.AUTH_LOCATORS['field_password']).send_keys(test_data.AUTH_DATA['valid_password'])
        driver.find_element(By.XPATH, locators.AUTH_LOCATORS['button_submit_sign_in']).click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.MAIN_LOCATORS['button_submit_order'])))
        driver.quit()

    def test_auth_from_forgot_password_page_succes(self):
        driver = webdriver.Chrome()
        driver.get(host)
        driver.find_element(By.XPATH, locators.MAIN_LOCATORS['login_button']).click()
        driver.find_element(By.XPATH, locators.AUTH_LOCATORS['button_forgot_password']).click()
        driver.find_element(By.XPATH, locators.FORGOT_PASSWORD_LOCATORS['button_sign_in']).click()
        driver.find_element(By.XPATH, locators.AUTH_LOCATORS['field_email']).send_keys(test_data.AUTH_DATA['email'])
        driver.find_element(By.XPATH, locators.AUTH_LOCATORS['field_password']).send_keys(test_data.AUTH_DATA['valid_password'])
        driver.find_element(By.XPATH, locators.AUTH_LOCATORS['button_submit_sign_in']).click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.MAIN_LOCATORS['button_submit_order'])))
        driver.quit()

class TestMyAccount():

    def test_opening_my_account_page(self):
        driver = webdriver.Chrome()
        driver.get(host)
        driver.find_element(By.XPATH, locators.MAIN_LOCATORS['login_button']).click()
        driver.find_element(By.XPATH, locators.AUTH_LOCATORS['field_email']).send_keys(test_data.AUTH_DATA['email'])
        driver.find_element(By.XPATH, locators.AUTH_LOCATORS['field_password']).send_keys(test_data.AUTH_DATA['valid_password'])
        driver.find_element(By.XPATH, locators.AUTH_LOCATORS['button_submit_sign_in']).click()
        driver.find_element(By.XPATH, locators.MAIN_LOCATORS['button_my_profile']).click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.MY_ACCOUNT_LOCATORS['field_name'])))
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.MY_ACCOUNT_LOCATORS['field_email'])))
        assert driver.find_element(By.XPATH, locators.MY_ACCOUNT_LOCATORS['field_name']).get_attribute('value') == test_data.AUTH_DATA['name']
        assert driver.find_element(By.XPATH, locators.MY_ACCOUNT_LOCATORS['field_email']).get_attribute('value') == test_data.AUTH_DATA['email']
        driver.quit()

    def test_opening_main_page_using_click_on_logo(self):
        driver = webdriver.Chrome()
        driver.get(host)
        driver.find_element(By.XPATH, locators.MAIN_LOCATORS['login_button']).click()
        driver.find_element(By.XPATH, locators.AUTH_LOCATORS['field_email']).send_keys(test_data.AUTH_DATA['email'])
        driver.find_element(By.XPATH, locators.AUTH_LOCATORS['field_password']).send_keys(test_data.AUTH_DATA['valid_password'])
        driver.find_element(By.XPATH, locators.AUTH_LOCATORS['button_submit_sign_in']).click()
        driver.find_element(By.XPATH, locators.MAIN_LOCATORS['button_my_profile']).click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.MY_ACCOUNT_LOCATORS['field_name'])))
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.MY_ACCOUNT_LOCATORS['field_email'])))
        driver.find_element(By.XPATH, locators.MAIN_LOCATORS['logo']).click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.MAIN_LOCATORS['button_submit_order'])))
        driver.quit()

    def test_opening_main_page_using_click_constructor_button(self):
        driver = webdriver.Chrome()
        driver.get(host)
        driver.find_element(By.XPATH, locators.MAIN_LOCATORS['login_button']).click()
        driver.find_element(By.XPATH, locators.AUTH_LOCATORS['field_email']).send_keys(test_data.AUTH_DATA['email'])
        driver.find_element(By.XPATH, locators.AUTH_LOCATORS['field_password']).send_keys(test_data.AUTH_DATA['valid_password'])
        driver.find_element(By.XPATH, locators.AUTH_LOCATORS['button_submit_sign_in']).click()
        driver.find_element(By.XPATH, locators.MAIN_LOCATORS['button_my_profile']).click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.MY_ACCOUNT_LOCATORS['field_name'])))
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.MY_ACCOUNT_LOCATORS['field_email'])))
        driver.find_element(By.XPATH, locators.MAIN_LOCATORS['button_constructor']).click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.MAIN_LOCATORS['button_submit_order'])))
        driver.quit()

    def test_logout(self):
        driver = webdriver.Chrome()
        driver.get(host)
        driver.find_element(By.XPATH, locators.MAIN_LOCATORS['login_button']).click()
        driver.find_element(By.XPATH, locators.AUTH_LOCATORS['field_email']).send_keys(test_data.AUTH_DATA['email'])
        driver.find_element(By.XPATH, locators.AUTH_LOCATORS['field_password']).send_keys(test_data.AUTH_DATA['valid_password'])
        driver.find_element(By.XPATH, locators.AUTH_LOCATORS['button_submit_sign_in']).click()
        driver.find_element(By.XPATH, locators.MAIN_LOCATORS['button_my_profile']).click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.MY_ACCOUNT_LOCATORS['field_name'])))
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.MY_ACCOUNT_LOCATORS['field_email'])))
        driver.find_element(By.XPATH, locators.MY_ACCOUNT_LOCATORS['button_logout']).click()
        WebDriverWait(driver, 1).until(expected_conditions.visibility_of_element_located((By.XPATH, locators.AUTH_LOCATORS['button_submit_sign_in'])))
        driver.quit()


class TestMenuConstructor():

    def test_choosing_section_sauсes(self):
        driver = webdriver.Chrome()
        driver.get(host)
        driver.find_element(By.XPATH, locators.MAIN_LOCATORS['button_menu_sauсes']).click()
        time.sleep(1)
        assert driver.find_element(By.XPATH, locators.MAIN_LOCATORS['title_bread']).is_displayed()
        driver.quit()

    def test_choosing_section_toppings(self):
        driver = webdriver.Chrome()
        driver.get(host)
        driver.find_element(By.XPATH, locators.MAIN_LOCATORS['button_menu_toppings']).click()
        time.sleep(1)
        assert driver.find_element(By.XPATH, locators.MAIN_LOCATORS['title_bread']).is_displayed()
        assert driver.find_element(By.XPATH, locators.MAIN_LOCATORS['title_sauces']).is_displayed()
        driver.quit()

    def test_choosing_section_bread(self):
        driver = webdriver.Chrome()
        driver.get(host)
        driver.find_element(By.XPATH, locators.MAIN_LOCATORS['button_menu_sauсes']).click()
        time.sleep(1)
        driver.find_element(By.XPATH, locators.MAIN_LOCATORS['button_menu_bread']).click()
        time.sleep(1)
        assert driver.find_element(By.XPATH, locators.MAIN_LOCATORS['title_bread']).is_enabled()
        driver.quit()

