# 🛒 E2E Test for Saucedemo.com

[![Selenium](https://img.shields.io/badge/selenium-3.x-brightgreen)](https://www.selenium.dev/)
[![Python](https://img.shields.io/badge/python-3.x-blue)](https://www.python.org/)

Этот проект содержит автоматический E2E тест для проверки сценария покупки товара на сайте [Saucedemo.com](https://www.saucedemo.com/) с использованием **Python** и **Selenium**.

## 📋 Описание

Тест выполняет следующие шаги:

1. Авторизуется на сайте.
2. Выбирает товар ("Sauce Labs Backpack").
3. Добавляет товар в корзину.
4. Переходит в корзину и проверяет наличие товара.
5. Оформляет покупку, заполняя форму.
6. Подтверждает успешное завершение покупки.

## 🚀 Установка и запуск

### Шаг 1: Установите Python 3.x

Убедитесь, что на вашем компьютере установлен Python версии 3.x.

### Шаг 2: Клонируйте репозиторий

Склонируйте этот репозиторий на свой компьютер с помощью Git:

```
git clone https://github.com/xalinac/saucedemo-e2e-test.git
```
```
cd saucedemo-e2e-test
```

### Шаг 3: Установите зависимости

Установите необходимые библиотеки, используя команду:

```
pip install -r requirements.txt
```

### Шаг 4: Установите ChromeDriver

1.	Скачайте [ChromeDriver](https://developer.chrome.com/docs/chromedriver/downloads) подходящей версии для вашего браузера Chrome.
2.	Добавьте его в PATH, чтобы Selenium мог его использовать.

### Шаг 5: Запуск теста

Для запуска теста выполните следующую команду:

```
python test_purchase.py
```

После выполнения команда выполнит тест, который включает авторизацию, добавление товара в корзину, оформление покупки и проверку успешного завершения.
