from django.urls import path
from . import views

urlpatterns = [

    path('',views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>/', views.details, name='details'),
    path('testing/', views.testing, name='testing'),

    path('members/add/', views.add_member, name='add_member'),

    path('delete/<int:id>/', views.delete_member, name='delete_member'),
]
