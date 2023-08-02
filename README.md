# Parser Ozon
Django приложение с REST API для парсинга информации о товарах магазина по ссылке с сайта Ozon 
и сохранения полученных данных о товарах в базу данных, с оповещением о завершении парсинга через Telegram бота.

### Запуск
```bash
cp config/.env.template config/.env
nano .env  # Редактируем .env файл, вписываем все необходимые для работы переменные
docker compose up --build  # Запускаем
# в отдельном окне
docker compose exec -u root web python manage.py createsuperuser  # Создаем суперпользователя
```

### URLs
```
GET http://127.0.0.1:8000/v1/products/ - Список всех товаров, с информацией о товарах
GET http://127.0.0.1:8000/v1/products/{id}/ - Информация о товаре
POST http://127.0.0.1:8000/v1/products/ - Запуск парсинга товаров
```

### Команды  
`docker compose up --build` Запуск проекта  
`docker compose exec -u root web python manage.py createsuperuser` Создание суперпользователя   


### Debug
GUI Selenium находится по адресу `http://127.0.0.1:7900/?autoconnect=1&resize=scale&password=secret`
Инициализация для IDE (например PyCharm):
```cmd
# Windows
python -m venv venv  # с именем .venv будут проблемы с poetry поэтому название должно быть без точки
venv\Scripts\activate.bat
pip install poetry==1.5.1
poetry install

# Linux or Mac
python3 -m venv venv   # с именем .venv будут проблемы с poetry поэтому название должно быть без точки
. venv/bin/activate
pip install poetry==1.5.1
poetry install
```
