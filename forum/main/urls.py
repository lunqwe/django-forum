from django.urls import path, include
from . import views
urlpatterns = [
   path('', views.homepage, name='homepage'),
   path('home/', views.homepage, name='homepage'),
   path('sign-up', views.sign_up, name='sign_up'),
   path('create_post', views.create_post, name='create_post'),
]