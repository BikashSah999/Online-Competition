from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='dashboardhome'),
    path('inactive/', views.inactive, name='dashboardinactive'),
    path('category/', views.handlecategory, name='dashboardcategory'),
    path('delete/<str:type>/<int:id>', views.delete, name='dashboarddelete'),
    path('edit/<str:type>/<int:id>', views.edit, name='dashboardedit'),
    path('update/<int:id>', views.update, name='dashboardupdate'),
    path('addcompetition/', views.addcompetition, name='dashboardaddcompetition'),
    path('logout/', views.logout, name='dashboardlogout')
]
