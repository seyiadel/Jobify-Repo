from django.urls import path 
from quikapp import views
urlpatterns = [
   path('logout/', views.loggedout, name='logout'),
    path('', views.LoginView, name='login'),
    path('profile/', views.profile, name= 'profile'),
    path('home/', views.homepage, name='home'),
    path('signup/', views.SignUpView, name='signup')
]