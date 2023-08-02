from server.settings.components import config
from server.settings.components.common import TIME_ZONE

CELERY_TASK_DEFAULT_QUEUE = 'default'
CELERY_BROKER_URL = config('CELERY_BROKER_URL', default='redis://redis:6379/')
CELERY_TIMEZONE = TIME_ZONE
BROKER_POOL_LIMIT = 1000

# for django-celery-results
CELERY_RESULT_BACKEND = 'django-db'
