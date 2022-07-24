
#Главная страница
MAIN_LOCATORS = {
    'login_button': "//*[@id='root']/div/main/section[2]/div/button[text()='Войти в аккаунт']", #кнопка "Войти в аккаунт"
    'button_submit_order': "//*[@id='root']/div/main/section[2]/div/button[text()='Оформить заказ']", #кнопка "Оформить заказ"
    'button_my_profile': "//*[@id='root']/div/header/nav/a/p[text()='Личный Кабинет']",#кнопка "Личный кабинет"
    'logo': "//*[@id='root']/div/header/nav/div/a[@href='/']", #логотип Stellar Burgers
    'button_constructor': "//*[@id='root']/div/header/nav/ul/li[1]/a/p[text()='Конструктор']", #кнопка "Конструктор"
    'button_menu_sauсes': "//*[@id='root']/div/main/section[1]/div[1]/div[2]/span[text()='Соусы']", #кнопка "Соусы"
    'title_bread': "//*[@id='root']/div/main/section[1]/div[2]/h2[1][text()='Булки']", #заголовок "Булки"
    'button_menu_toppings': "//*[@id='root']/div/main/section[1]/div[1]/div[3]/span[text()='Начинки']", #кнопка "Начинки"
    'title_sauces': "//*[@id='root']/div/main/section[1]/div[2]/h2[2][text()='Соусы']", #заголовок "Соусы"
    'button_menu_bread': "//*[@id='root']/div/main/section[1]/div[1]/div[1]/span[text()='Булки']" #кнопка "Булки"
}

#Страница регистрации
REG_LOCATORS = {
    'field_name': "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input", #поле "Имя"
    'field_email': "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input", #поле "Email"
    'field_password': "//*[@id='root']/div/main/div/form/fieldset[3]/div/div/input", #поле "Пароль"
    'button_submit_sign_up': "//*[@id='root']/div/main/div/form/button[text()='Зарегистрироваться']", #кнопка "Зарегистрироваться"
    'input_sign_up_password_error': "//*[@id='root']/div/main/div/form/fieldset[3]/div/p[text()='Некорректный пароль']", #'элемент с ошибкой "Некорректный пароль"
    'button_sign_in': "//*[@id='root']/div/main/div/div/p/a[@href='/login']", #кнопка перехода на страницу авторизации
}

#Страница авторизации
AUTH_LOCATORS = {
    'button_sign_up': "//*[@id='root']/div/main/div/div/p[1]/a[@href='/register']", #кнопка перехода на страницу регистрации
    'button_forgot_password': "//*[@id='root']//div/main/div/div/p[2]/a[@href='/forgot-password']",#кнопка перехода на страницу восстановления пароля
    'field_email': "//*[@id='root']/div/main/div/form/fieldset[1]/div/div/input", #поле "Email"
    'field_password': "//*[@id='root']/div/main/div/form/fieldset[2]/div/div/input", #поле "Пароль"
    'button_submit_sign_in': "//*[@id='root']/div/main/div/form/button[text()='Войти']" #кнопка "Войти"
}

#Страница восстановления пароля
FORGOT_PASSWORD_LOCATORS = {
    'button_sign_in': "//*[@id='root']/div/main/div/div/p/a[@href='/login']" #кнопка перехода на страницу авторизации
}

#Страница личный кабинет
MY_ACCOUNT_LOCATORS = {
    'field_name': "//*[@id='root']/div/main/div/div/div/ul/li[1]/div/div/input", #поле "Имя"
    'field_email': "//*[@id='root']/div/main/div/div/div/ul/li[2]/div/div/input", #поле "Email"
    'button_logout': "//*[@id='root']/div/main/div/nav/ul/li[3]/button[text()='Выход']" #кнопка "Выход"
}

