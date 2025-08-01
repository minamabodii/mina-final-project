from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('blog/new/', views.post_new, name='post_new'),
    path('blog/<str:slug>/', views.post_detail, name='post_detail'),
    path('blog/<str:slug>/edit/', views.post_edit, name='post_edit'),
]
