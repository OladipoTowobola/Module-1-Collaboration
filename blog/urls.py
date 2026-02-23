from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]

=======
    path('', views.home, name='home'),
]
>>>>>>> de1d1c1ad6305bb82b2bcd3cf6306cb9a3962033
