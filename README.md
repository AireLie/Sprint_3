# Sprint_3
# Проект автоматизации тестирования для сервиса Stellar Burgers. Это космический фастфуд: можно собрать и заказать бургер из необычных ингредиентов.
1. Фреймворк selenium.
2. Браузер - Chrome
3. Команда для запуска всех тестов — pytest -v tests

Описание сценариев:
test_registration.py - Регистрация
test_login.py - Вход в аккаунт
test_logout.py - Выход из аккаунта
test_account.py - Личный кабинет
test_constructor.py - Конструктор

Тесты:
test_registration_with_valid_data - корректная регистрация
test_registration_with_empty_user_name - Пустое имя пользователя при регистрации
test_registration_with_invalid_password - некорректный пароль при регистрации

test_login_from_enter_account_button - вход с главной страницы
test_login_from_personal_account - вход по кнопке Личный кабинет
test_login_button_from_registration_form - вход через форму регистрации
test_login_from_recovery_link  - вход через восстановление пароля

test_transition_to_personal_account_logout - Выход

test_transition_to_personal_account - вход в ЛК
test_from_pa_to_contructor_by_button - переход по Кнопке Констуктор
test_from_pa_to_contructor_by_logo - переход по логотипу

test_buns_block_transition - Булки
test_sauses_block_transition - Соусы
test_toppings_block_transition - Начинки
