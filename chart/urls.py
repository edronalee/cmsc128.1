from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('docregister/', views.docregister, name="docregister"),
    path('lguregister/', views.lguregister, name="lguregister"),

    path('brgyregistry/', views.brgyregistry, name="brgyregistry"),
    path('communityboard/', views.communityboard, name="communityboard"),
    path('healthtracker/<str:pk_test>/', views.healthtracker, name="healthtracker"),
    path('monitor/', views.monitor, name="monitor"),

    path('patientinfo/<str:pk_test>/', views.patientinfo, name="patientinfo"),
    path('vitalsign/<str:pk_test>/', views.vitalsign, name="vitalsign"),
    path('transfer/', views.transfer, name="transfer"),
    path('statistics/', views.statistics, name="statistics"),
]