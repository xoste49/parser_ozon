# Parser Ozon
Django приложение с REST API для парсинга информации о товарах магазина по ссылке с сайта Ozon 
и сохранения полученных данных о товарах в базу данных, с оповещением о завершении парсинга через Telegram бота.

### Запуск
```bash
cp config/.env.template config/.env
nano .env  # Редактируем .env файл, вписываем все необходимые для работы переменные
docker compose up --build  # Запускаем
# в отдельном окне
docker compose exec -u root web bash  # Заходим в контейнер под root пользователем
python manage.py createsuperuser  # Создаем суперпользователя
```

### Команды  
`docker compose up --build  # Запуск проекта`

Создание суперпользователя (в отдельном окне командной строки)
```bash
docker compose exec -u root web bash
python manage.py createsuperuser
```
