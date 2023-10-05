from django.contrib.auth import get_user_model
from django.test import TestCase


# Create your tests here.
class UserAccountTests(TestCase):
    def setUp(self) -> None:
        self.db = get_user_model()

    def test_new_superuser(self):
        super_user = self.db.objects.create_superuser(
            'testsuser@gmail.com', 'username', 'firstname', 'password'
        )
        self.assertEqual(super_user.email, 'testsuser@gmail.com')
        self.assertEqual(super_user.user_name, 'username')
        self.assertEqual(super_user.first_name, 'firstname')
        self.assertEqual(str(super_user), 'username')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)

        # Testing the raises of !is_superuser
        with self.assertRaises(ValueError):
            self.db.objects.create_superuser(
                email='testuser@gmail.com', user_name='username1', first_name='first_name', password='password',
                is_superuser=False
            )

        # Testing the raises of !is_staff
        with self.assertRaises(ValueError):
            self.db.objects.create_superuser(
                email='testuser@gmail.com', user_name='username1', first_name='first_name', password='password',
                is_staff=False
            )

    def test_new_user(self):
        user = self.db.objects.create_user(
            'testuser@gmail.com', 'username', 'firstname', 'password'
        )
        self.assertEqual(user.email, 'testuser@gmail.com')
        self.assertEqual(user.user_name, 'username')
        self.assertEqual(user.first_name, 'firstname')
        self.assertFalse(user.is_superuser)
        self.assertTrue(user.is_active)

        # Testing the required field which is email
        with self.assertRaises(ValueError):
            self.db.objects.create_user(
                email='', user_name='username', first_name='first_name', password='password'
            )