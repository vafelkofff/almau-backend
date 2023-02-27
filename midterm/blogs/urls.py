from django.urls import path
from . import views

urlpatterns = [
    path('/', views.blogs_handler),
    path('/<int:pk>', views.blog_handler),
]

