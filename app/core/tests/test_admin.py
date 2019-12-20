from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth import get_user_model


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@gmail.com',
            password='password123'
        )

        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@gmail.com',
            password='password123',
            name='Test User full name'
        )

    def test_users_listed(self):
        "test that users are listed on user page"
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        # check out the response return 200
        self.assertContains(res, self.user.email)

    def test_use_change_page(self):
        "test that the user edit page works"
        url = reverse('admin:core_user_change', args=[self.user.id])
        # the reverse function will generate the URL
        # /admin/core/user/ assign here  <-- agrument works in above function
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
