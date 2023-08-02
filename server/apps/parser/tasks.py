from server.apps.parser.models import ProductsModel, SessionParsingModel
from server.apps.parser.utils import parse_products_seller
from server.apps.utils.send_notification_tg import send_notification_tg
from server.celery import celery


@celery.task()
def parse_products_seller_task(products_count: int):
    """Парсинг товаров продавца."""
    # Создаём в базе сессию парсинга
    session_parsing = SessionParsingModel.objects.create()
    products = parse_products_seller(products_count=products_count)
    products_objects = [
        ProductsModel(
            name=product['name'],
            url=product['url'],
            price=product['price'],
            session_parsing=session_parsing,
        )
        for product in products
    ]
    ProductsModel.objects.bulk_create(products_objects)
    send_notification_tg(
        'Задача на парсинг товаров с сайта Ozon завершена.\n'
        f'Сохранено: {len(products)} товаров.',
    )
