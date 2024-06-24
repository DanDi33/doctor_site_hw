from django.urls import path
from .views import home, about, profile
from .views import MyAboutView

urlpatterns = [
    path("",home , name="home"),
    path("admin-panel/about/", MyAboutView.as_view(), name="about"),
    path("admin-panel/profile/",profile , name="profile"),

    # path('profile/', MyProfileView.as_view(), name="profile")
]