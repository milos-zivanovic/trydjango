from django.urls import path
# from products.views import product_list, product_detail, product_create, product_update, product_delete
from products.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = 'products'
urlpatterns = [

    # FUNCTION BASED URLS

    # path('', product_list, name='product_list'),
    # path('<int:id>/', product_detail, name='product_detail'),
    # path('create/', product_create, name='product_create'),
    # path('<int:id>/update/', product_update, name='product_update'),
    # path('<int:id>/delete', product_delete, name='product_delete'),

    # CLASS BASED URLS
    path('', ProductListView.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete', ProductDeleteView.as_view(), name='product_delete'),
]
