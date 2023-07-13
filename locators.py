
from selenium.webdriver.common.by import By

class TestLocators:
    # ФОрма регистрации:
    BUTTON_PERSONAL_ACCOUNT = By.XPATH, '//p[contains(text(), "Личный Кабинет")]'    # Кнопка Личный Кабинет
    LINK_REGISTRATION = By.XPATH, '//a[contains(text(), "Зарегистрироваться")]'    # Ссылка на форму регистации
    INPUT_NAME = By.XPATH, '//label[text()="Имя"]/following-sibling::input'    # Поле ввода имени
    INPUT_EMAIL = By.XPATH, '//label[text()="Email"]/following-sibling::input'    # Поле ввода почты
    INPUT_PASSWORD = By.XPATH, '//label[text()="Пароль"]/following-sibling::input'    # Поле ввода пароля
    BUTTON_REGISTRATION = By.XPATH, '//*[contains(@class, "button_button_type_primary")]'    # Кнопка Зарегистрироваться
    ERROR_REGISTRATION = By.XPATH, '//*[contains(text(), "Некорректный пароль")]'    # Ошибка регистрации
    REGISTRATION_HEADER = By.XPATH, '//*[contains(text(), "Регистрация")]'     # Заголовок формы Регистрации

    LOGIN_HEADER = By.XPATH, '//*[contains(text(), "Вход")]'    # Заголовок формы Вход
    CURRENT_EMAIL = By.XPATH, '//label[text()="Логин"]/following-sibling::input' # Поле с логином, указанным при регистрации

    # Вход в аккаунт
    BUTTON_ENTER_IN_ACCOUNT = By.XPATH, '//*[contains(text(), "Войти в аккаунт")]'    # Кнопка Войти в аккаунт на главной
    INPUT_EMAIL = By.XPATH, '//label[text()="Email"]/following-sibling::input'    #  Поле ввода почты
    INPUT_PASSWORD = By.XPATH, '//label[text()="Пароль"]/following-sibling::input'    # Поле ввода пароля
    BUTTON_LOGIN = By.XPATH, '//*[contains(text(), "Войти")]'    # Кнопка Войти

    BUTTON_PLACE_AN_ORDER = By.XPATH, '//*[contains(text(), "Оформить заказ")]'    # Кнопка Оформить заказ после логина
    LINK_LOGIN_FROM_REGISTRATION = By.XPATH, '//*[contains(text(), "Войти")]'    # Ссылка на логин с формы регистрации
    LINK_RECOVERY_PASSWORD = By.LINK_TEXT, 'Восстановить пароль'    # Ссылка Восстановления пароля
    LINK_LOGIN_FROM_RECOVERY = By.LINK_TEXT, 'Войти'    # Ссылка Войти со страницы "Восстановления пароля"
    BUTTON_SAVE = By.XPATH, '//button[contains(text(), "Сохранить")]'    # Кнопка Сохранить в ЛК

    BUTTON_LOGOUT = By.XPATH, '//button[contains(text(), "Выход")]'    # Кнопка Выхода из аккаунта

    # Переходы между страницами
    LOGO_BUTTON = By.XPATH,'//*[contains(@class,"__logo")]' # Логотип бургерной
    BUTTON_CONSTRUCTOR = By.XPATH, '//p[contains(text(), "Конструктор")]'    # Кнопка перехода в Конструктор
    BLOCK_BUNS = By.XPATH, '//span[contains(text(), "Булки")]'    # Кнопка перехода к Булкам
    HEADER_BUNS = By.XPATH, '//h2[contains(text(), "Булки")]'    # Текст текущего раздела товаров Булки
    BULKA_NAME = By.XPATH, '//*[contains(text(), "Флюоресцентная булка R2-D3")]' #Одна из булок

    BLOCK_SAUSES = By.XPATH, '//span[contains(text(), "Соусы")]'    # Кнопка перехода к Соусам
    HEADER_SAUSES = By.XPATH, '//h2[contains(text(), "Соусы")]'  # Текст текущего раздела товаров Соусы
    SAUSE_NAME = By.XPATH, '//*[contains(text(), "Соус Spicy-X")]'  # Один из соусов

    BLOCK_TOPPINGS = By.XPATH, '//span[contains(text(), "Начинки")]'    # Кнопка перехода к Начинкам
    HEADER_TOPPINGS = By.XPATH, '//h2[contains(text(), "Начинки")]'  # Текст текущего раздела товаров Начинки
    TOPPING_NAME = By.XPATH, '//*[contains(text(), "Мясо бессмертных моллюсков Protostomia")]'  # Одна из начинок
