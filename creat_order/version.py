from django.contrib import admin
from django.urls import path
from django.urls import include
from creat_order import urls

urlpatterns = [
    path('api/v1.0/', include(urls))

]
