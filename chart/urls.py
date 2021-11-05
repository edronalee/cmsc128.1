from django.urls import path
from . import views

from account.views import docregistration_view, lguregistration_view, login_view, logout_view

urlpatterns = [
    path('', login_view, name="login"),
    path('', logout_view, name ="logout"), #just a call to the logout function, redirects to login.html
    path('register/', views.register, name="register"),
    path('docregister/', docregistration_view, name="docregister"),
    path('lguregister/', lguregistration_view, name="lguregister"),
    path('brgyregistry/', views.brgyregistry, name="brgyregistry"),
    path('communityboard/', views.communityboard, name="communityboard"),
    path('docinfo/', views.docinfo, name = "docinfo"),
    path('lguinfo/', views.lguinfo, name = "lguinfo"),
    path('healthtracker/<str:pk_test>/', views.healthtracker, name="healthtracker"),
    path('monitor/', views.monitor, name="monitor"),
    path('patientinfo/<str:pk_test>/', views.patientinfo, name="patientinfo"),
    path('vitalsign/<str:pk_test>/', views.vitalsign, name="vitalsign"),
    path('transfer/', views.transfer, name="transfer"),
    path('statistics/', views.statistics, name="statistics"),
]