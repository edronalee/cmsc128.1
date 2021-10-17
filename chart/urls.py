from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('docregister/', views.docregister, name="docregister"),
    path('lguregister/', views.lguregister, name="lguregister"),

    path('brgyregistry/', views.brgyregistry, name="brgyregistry"),
    path('communityboard/', views.communityboard, name="communityboard"),
    path('healthtracker/', views.healthtracker, name="healthtracker"),
    path('monitor/', views.monitor, name="monitor"),
    path('patientinfo/', views.patientinfo, name="patientinfo"),
    path('vitalsign/', views.vitalsign, name="vitalsign"),
]