from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.handlelogin, name='login'),
    path('signup/', views.handlesignup, name='signup'),
    path('logout/', views.handlelogout, name='logout'),
    path('form/<str:category_name>/<contest_name>', views.handleform, name='form'),
]
