from django.urls import path
from .views import HomeView


urlpatterns = [
    # path("",home , name="home")
    path("",HomeView.as_view() , name="home")
    ]