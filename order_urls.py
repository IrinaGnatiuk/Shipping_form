from django.conf.urls import url, include
from django.urls import path
from . import views
# from order.views import MakeOrder

urlpatterns = [
    path('order/', views.OrderView.as_view(), name='order'),
    path('order/shipping_form', views.MakeShippingOrderForm.as_view(), name='shipping_form'),
    path('del_dish/<int:pk>/', views.OrderView.del_dish_from_order, name='delete_dish_from_order'),
    path('change_count/<int:pk>/', views.EditCountDish.as_view(), name='edit_count_dish'),
]