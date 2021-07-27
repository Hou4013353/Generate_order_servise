from django.contrib import admin
from django.urls import path
from django.urls import include
from creat_order import views

urlpatterns = [
    path('login', views.login.as_view()),
    path('get_card', views.get_card.as_view()),
    path('Initialize_form', views.Initialize_form.as_view()),
    path('put_custom', views.put_custom.as_view()),
    path('session_check', views.session_check.as_view()),
    path('close_reason', views.close_reason.as_view()),
    path('put_close_reason', views.put_close_reason.as_view()),
    path('reopen', views.reopen.as_view()),
    path('head_end_content', views.head_end_content.as_view()),
    path('generate_order', views.generate_order.as_view())



]
