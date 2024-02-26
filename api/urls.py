from django.urls import path
from  .import views 
from rest_framework.authtoken import views as auth_view


urlpatterns=[
    #path('users', views.UserRegisterviewEndpoint.as_view(), name='create-users'),
    #path('login', auth_view.ObtainAuthToken.as_view(), name='login-user'),
    path('categories',views.UpgradedCategoryEndpoint.as_view(), name='categories'),
    path('category/<int:pk>', views.SingleCategoryEndpoint.as_view(), name='category-details'),
    path('category/<int:pk>/delete',views.CategoryDeleteEndpoint.as_view(), name='delete-category'),
    path('products', views.UpgradedProductEndpoint.as_view(), name='products'),
    path('products-list', views.ProductListEndpoint.as_view(), name='products-list'),
    path('product/<int:product_id>', views.ProductDetailEndpoint.as_view(), name='product-detail')
]