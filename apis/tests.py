from rest_framework.test import APITestCase
from products.models import Product, Category
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status


# Create your tests here.
class ProductTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(name='test')
        cls.user = get_user_model().objects.create_user(
            'testuser@gmail.com', 'username', 'firstname', 'password'
        )
        cls.product = Product.objects.create(
            category=cls.category,
            title='test_title',
            description='test_content',
            slug='test-title',
            author=cls.user,
            status='Published'
        )

    def test_create_product(self):
        object = {
            'category': 'test_cat',
            'title': 'test_title',
            'description': 'test_content',
            'slug': 'test-slug',
        }
        self.client.login(username=self.user.user_name, password=self.user.password)
        response = self.client.post(reverse('Product_List'), object, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_product(self):
        """ Will try to update some product with different user. """
        client = APIClient()
        user2 = get_user_model().objects.create_user(
            'testuser2@gmail.com', 'username2', 'firstname2', 'password2'
        )

        # Login User2
        client.login(username=user2.user_name, password=user2.password)

        # Object to update
        object = {
            'category': 'udpate',
            'title': 'update',
            'description': 'update',
            'slug': 'update',
        }
        response = client.put(reverse('Product_Detail', kwargs={'pk': self.product.id}), object, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_product_list(self):
        response = self.client.get(reverse('Product_List'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_product_detail(self):
        response = self.client.get(reverse('Product_Detail', kwargs={'pk': self.product.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)