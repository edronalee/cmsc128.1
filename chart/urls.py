from django.urls import path
from . import views

from django.contrib.auth import views as auth_views

from account.views import docregistration_view, lguregistration_view, login_view, logout_view

from account.forms import UserPasswordResetForm

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
    path('referred/', views.referred, name="referred"),
    path('hospital/', views.hospital, name="hospital"),
    path('isolationfacility/', views.isolationfacility, name="isolationfacility"),
    path('patientinfo/<str:pk_test>/', views.patientinfo, name="patientinfo"),
    path('doctorsnotes/<str:pk_test>/', views.doctorsnotes, name="doctorsnotes"),
    path('doctorsnotesdetails/<str:pk>/<str:pk_test>/', views.doctorsnotesdetails, name="doctorsnotesdetails"),
    path('vitalsign/<str:pk_test>/', views.vitalsign, name="vitalsign"),
    path('vitalsigndetails/<str:pk>/<str:pk_test>/', views.vitalsigndetails, name="vitalsigndetails"),
    path('healthtrackerdetails/<str:pk>/<str:pk_test>/', views.healthtrackerdetails, name="healthtrackerdetails"),
    path('transfer/', views.transfer, name="transfer"),
    path('statistics/', views.statistics, name="statistics"),

    path('listtransferred/', views.listtransferred, name="listtransferred"),
    path('listreferred/', views.listreferred, name="listreferred"),
    path('listrtpcr/', views.listrtpcr, name="listrtpcr"),
    path('listantigen/', views.listantigen, name="listantigen"),

    #forgot password views
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "chart/password_reset.html", form_class= UserPasswordResetForm), name = "reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "chart/password_reset_sent.html"), name = "password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = "chart/password_reset_form.html"), name = "password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "chart/password_reset_done.html"), name = "password_reset_complete"),
]