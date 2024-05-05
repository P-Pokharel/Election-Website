from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('results/', views.results, name='results'),
    path('login/', views.login, name='login'),
    path('candidate_list/', views.candidate_list, name='candidate-list'),
    path('candidate_detail/', views.candidate_detail, name='candidate-detail'),
]