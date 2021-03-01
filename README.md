# Проект "multilang_eshop"

## Описание
Данный репозиторий создан в рамках прохождения курса "Автоматизация тестирования с помощью Selenium и Python", и проверяет наличие кнопки "Добавить в корзину" на сайте интернет-магазина.

## Как запустить

1. Клонирование репозитория. В терминале необходимо ввести команду:
 ```shell
git clone https://github.com/rustfl/multilang_eshop
```

2. Переход в папку с файлами. В терминале введи команду:
```shell
cd multilang_eshop
```

3. Запуск теста. Для запуска теста в терминале необходимо ввести команду:
```shell
pytest --language=fr test_items.py
```
Если у тебя всё правильно настроено, то запустится браузер Chrome и откроется страница интернет магазина. Браузер закроется через 30 секунд после запуска. За это время тебе нужно будет убедиться что на кнопке для добавления товара в корзину отображается надпись "Ajouter au panier".