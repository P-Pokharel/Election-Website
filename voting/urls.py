from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('results/', views.results, name='results'),
    path('login/', views.loginPage, name='login'),
    path('registration', views.registrationPage, name='registration'),
    path('candidate_list/', views.candidate_list, name='candidate_list'),
    path('candidate_detail/', views.candidate_detail, name='candidate_detail'),
    path('guidelines/', views.guidelines, name='guidelines'),
    path('voter_info/<int:candidate_id>/', views.voter_info, name='voter_info'),
]