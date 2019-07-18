from django.urls import path
from .views import UserDetailView
from . import views

urlpatterns = [
    path('<int:pk>/', UserDetailView.as_view(), name='user-details'),
]