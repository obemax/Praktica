from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.list import ListView
from django.contrib import messages
from django.views.generic.detail import DetailView

from orders.models import Order

from common.views import TitleMixin
from orders.forms import OrderForm


class OrderCreateView(TitleMixin, SuccessMessageMixin, CreateView):
    template_name = 'orders/order-create.html'
    form_class = OrderForm
    success_message = 'заказ успешно оформлен'
    title = "Store - Оформление заказа"

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        self.object = form.save()  # Сохраняем форму и получаем созданный объект

        # Вызываем метод update_order после сохранения объекта в базе данных
        self.object.update_order()

        self.success_message = 'заказ успешно оформлен, можете посмотреть его во кладке заказы'  # Установите сообщение здесь
        messages.success(self.request, self.success_message)

        self.success_url = reverse_lazy('users:profile', kwargs={'pk': self.request.user.pk})
        return HttpResponseRedirect(self.get_success_url())  # Этот редирект можно оставить


class OrderListView(TitleMixin, ListView):
    template_name = 'orders/orders.html'
    title = 'Store - Заказы'
    queryset = Order.objects.all()
    ordering = '-created'

    def get_queryset(self):
        queryset = super(OrderListView, self).get_queryset()
        if self.request.user.is_superuser:
            self.ordering = '-id'
            return queryset

        return queryset.filter(initiator=self.request.user)


class OrderDetailView(DetailView):
    template_name = 'orders/order.html'
    model = Order

    def get_context_data(self, **kwargs):
        context = super(OrderDetailView, self).get_context_data(**kwargs)
        context['title'] = f'Store - {self.object.id}'
        return context

