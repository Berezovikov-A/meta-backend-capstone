from django.test import TestCase
from restaurant.models import Menu


class MenuViewTest(TestCase):
    items = [
        {'title': 'Ice cream', 'price': 50.45, 'inventory': 10},
        {'title': 'Pizza', 'price': 40.54, 'inventory': 20},
        {'title': 'Pasta', 'price': 30.99, 'inventory': 30},
    ]

    def setUp(self):
        for item in self.items:
            instance = Menu.objects.create(**item)
            print(instance)
            instance.save()

    def test_getall(self):
        query_set = Menu.objects.all()
        items = [f"{item['title']} : {item['price']}" for item in self.items]
        self.assertQuerysetEqual(
            query_set, items, ordered=False, transform=lambda x: x.__str__())
