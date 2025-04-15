from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CartViewSet, ProductCategoryViewSet, register, login

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('categories', ProductCategoryViewSet)
router.register('cart', CartViewSet)

urlpatterns = [
    path('auth/register/', register),
    path('auth/login/', login),
    path('', include(router.urls)),
]
