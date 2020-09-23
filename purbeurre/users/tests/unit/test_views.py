from django.test import TestCase
from django.urls import reverse

class IndexViewTest(TestCase):

    def test_index_view_return_index_template(self):
        response = self.client.get(reverse('users:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Du gras oui, mais de qualité.")