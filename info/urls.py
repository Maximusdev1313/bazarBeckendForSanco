from .views import * 
from django.urls import path , include
from rest_framework import routers

router = routers.DefaultRouter()

router.register('category', Category__ViewSet)
router.register('products', Products__ViewSet)
router.register('users', Users__ViewSet)
router.register('orders', Orders__ViewSet)

urlpatterns = [
    path('',include(router.urls)),
]