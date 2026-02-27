from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse

class ProductAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_product(self):
        url = reverse("product-list", kwargs={"version": "v1"})
        payload = {"name": "Sample", "price": "10.00", "stock": 3}
        response = self.client.post(url, payload, format="json")
        self.assertEqual(response.status_code, 201)