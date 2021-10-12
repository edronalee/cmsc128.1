from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('docregister/', views.docregister, name="docregister"),
    path('lguregister/', views.lguregister, name="lguregister"),
]