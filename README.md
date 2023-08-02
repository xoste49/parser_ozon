# Parser Ozon
Django приложение с REST API для парсинга информации о товарах магазина по ссылке с сайта Ozon 
и сохранения полученных данных о товарах в базу данных, с оповещением о завершении парсинга через Telegram бота.

### Команды  
`docker compose up --build  # Запуск проекта`

Создание суперпользователя (в отдельном окне командной строки)
```bash
docker compose exec -u root web bash
python manage.py createsuperuser
```
