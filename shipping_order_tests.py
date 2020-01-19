from django.test import Client, TestCase
from django.urls import resolve, reverse
from .models import Order, ShippingOrder, Dish, User, InstanceDish


class TestShippingForm(TestCase):

    def setUp(self):
        pass

    def test_view_success_status_code_shipping_form(self):
        url = reverse('shipping_form')
        self.assertEquals(url, '/order/shipping_form')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)




