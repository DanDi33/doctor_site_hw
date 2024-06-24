from django.urls import path
from .views import home, about, profile
from .views import MyAboutView, MyEdAndWorkView, CreatePostEdAndWorkView

urlpatterns = [
    path("",home , name="home"),
    path("admin-panel/about/", MyAboutView.as_view(), name="about"),
    path("admin-panel/profile/",profile , name="profile"),
    path('adminPanel/ed_and_work/', MyEdAndWorkView.as_view(), name="ed_and_work"),
    path('adminPanel/ed_and_work/create/', CreatePostEdAndWorkView.as_view(), name="create-post-ed-and-work"),

    # path('profile/', MyProfileView.as_view(), name="profile")
]