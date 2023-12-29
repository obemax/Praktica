from django.urls import path

from orders.views import OrderCreateView, OrderListView, OrderDetailView

app_name = 'orders'
urlpatterns = [
    path('order-create/', OrderCreateView.as_view(), name='order-create'),
    path('', OrderListView.as_view(), name='orders-list'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order'),
]
