from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings


app_name = "ProductsApp"
urlpatterns = [
    path("", home, name="home"),
    path("user/", user, name='user'),
    path("product/", products, name="products"),
    path("product/create/", createProduct, name="createProduct"),
    path("product/update/<str:pk>/", updateProduct, name="updateProduct"),
    path("product/delete/<str:pk>/", deleteProduct, name="deleteProduct"),
    path('category/', category, name="category"),
    path("category/create/", createCategory, name="createCategory"),
    path("category/update/<str:pk>/", updateCategory, name="updateCategory"),
    path("category/delete/<str:pk>/", deleteCategory, name="deleteCategory"),
    path("customer/", customer, name="customer"),
    path("customer/create/", createCustomer, name="createCustomer"),
    path("customer/update/<str:pk>/", updateCustomer, name="updateCustomer"),
    path("customer/delete/<str:pk>/", deleteCustomer, name="deleteCustomer"),
    path("order/", order, name="order"),
    path("order/create/", createOrder, name="createOrder"),
    path("order/update/<str:pk>/", updateOrder, name="updateOrder"),
    path("order/delete/<str:pk>/", deleteOrder, name="deleteOrder"),
    path("status/", status, name="status"),
    path("status/create/", createStatus, name="createStatus"),
    path("status/update/<str:pk>/", updateStatus, name="updateStatus"),
    path("status/delete/<str:pk>/", deleteStatus, name="deleteStatus"),
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", logoutUser, name="logout"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
