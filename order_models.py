from django.db import models
from dishes.models import Dish, Drink, InstanceDish
from accounts.models import User
from django.core.validators import RegexValidator


class Order(models.Model):
    dishes = models.ManyToManyField(InstanceDish, blank=True)
    full_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    user = models.ForeignKey(User, null=True, max_length=512, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return 'Order № {}  Total price {}'. format(self.id,  self.full_price)

    def get_full_price(self):
        dishes = self.dishes.all()
        full_price = 0
        for dish in dishes:
            full_price += dish.price*dish.count
        self.full_price = full_price
        self.save()
        return full_price


class ShippingOrder(models.Model):
    FILTER_TYPES_payment = (
        ('cash', 'наличными'),
        ('card', 'картой'),
    )
    FILTER_TYPES_address = (
        ('not_delivery', 'Самовывоз'),
        ('delivery', 'Доставка по адресу'),
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    delivery = models.CharField(
        max_length=15, choices=FILTER_TYPES_address, default='Доставка по адресу')
    address = models.CharField(max_length=200, blank=True)
    comment = models.TextField(null=True, blank=True, default=None)
    payment_choice = models.CharField(
        max_length=15, choices=FILTER_TYPES_payment, default='наличными')
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
