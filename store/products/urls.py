from django.urls import path

from products.views import ProductsListView, basket_add, basket_remove, ProductDetailView

app_name = 'products'
urlpatterns = [
    path('', ProductsListView.as_view(), name='index'),
    path('product/<int:pk>/', ProductDetailView.as_view(),name='product'),
    path('category/<int:category_id>/', ProductsListView.as_view(), name='category'),
    path('search/', ProductsListView.as_view(), name='search'),
    path('category/<int:category_id>/page/<int:page>/', ProductsListView.as_view(), name='category_page'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
