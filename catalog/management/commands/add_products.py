from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Добавляет тестовые продукты в базу данных'

    def handle(self, *args, **kwargs):
        self.stdout.write('Очистка базы данных...')
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write('Создание новых категорий и продуктов...')
        cat = Category.objects.create(name="Электроника", description="Гаджеты")

        Product.objects.create(name="Смартфон", category=cat, price=50000, description="Хороший")
        Product.objects.create(name="Ноутбук", category=cat, price=80000, description="Мощный")

        self.stdout.write(self.style.SUCCESS('Успешно добавлено 2 продукта и 1 категория!'))