from django.urls import path 
from .import views

urlpatterns = [
    path('', views.index),
    path('process', views.process),
    path('success', views.success),
    path('login', views.login),
    path('logout', views.logout),
    path('process_message', views.post_mess),
    path('profile/<int:id>', views.profile),
    path('post_comment/<int:id>', views.post_comment),
    path('like/<int:id>', views.like),
    path('delete/<int:id>', views.delete_comment),
    path('edit/<int:id>', views.edit)
]