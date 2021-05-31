from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('login', views.login),
    path('register', views.register),
    path('success', views.success),
    path('logout',views.logout),
    path('add_post', views.add_post),
    path('delete/<int:id>', views.delete),
    path('thoughts/<int:id>', views.thoughts),
    path('like/<int:id>', views.like),
    path('un_like/<int:id>', views.un_like),
]
