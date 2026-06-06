from django.urls import path
from user import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
]