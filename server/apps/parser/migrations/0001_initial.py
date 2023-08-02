# Generated by Django 4.2.3 on 2023-08-02 08:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SessionParsingModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_parse', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата и время парсинга')),
            ],
            options={
                'verbose_name': 'Сессия парсинга',
                'verbose_name_plural': 'Сессии парсинга',
            },
        ),
        migrations.CreateModel(
            name='ProductsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название карточки товара')),
                ('url', models.URLField(verbose_name='Ссылка на карточку товара')),
                ('price', models.FloatField(verbose_name='Стоимость товара')),
                ('session_parsing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='parser.sessionparsingmodel', verbose_name='Сессия парсинга')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]
