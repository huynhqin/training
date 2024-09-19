from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewall, name='view all members'),
    path('mem/id=<int:id>', views.detail, name='view detail'),
    path('add/', views.add_member, name='add new member'),
]