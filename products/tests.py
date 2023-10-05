from django.contrib.auth import get_user_model
from . models import Category, Product
from django.test import TestCase


# Create your tests here.
class TestProduct(TestCase):
    def setUp(self) -> None:
        self.db = get_user_model()

    def test_category(self):
        category = Category.objects.create(
            name='test'
        )
        self.assertEqual(category.name, 'test')
        self.assertEqual(str(category), 'test')

    def test_product(self):
        user = self.db.objects.create_user(
            'testuser@gmail.com', 'username', 'firstname', 'password'
        )
        category = Category.objects.create(
            name='test'
        )
        product = Product.objects.create(
            category=category,
            title='test_title',
            description='test_content',
            slug='test-title',
            author=user,
            status='Published'
        )

        self.assertEqual(str(product), 'test_title')