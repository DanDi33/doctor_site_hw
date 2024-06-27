from django.urls import path
from .views import profile
from .views import (MessagesView,
                    UpdateMessageView,
                    MyAboutView, 
                    MyEdAndWorkView, 
                    CreatePostEdAndWorkView, 
                    UpdatePostEdAndWorkView, 
                    DeletePostEdAndWorkView,
                    MyCaseView,
                    CreateCaseView,
                    UpdateCaseView,
                    DeleteCaseView,
                    UpdateMenuView,
                    UpdateParalaxView
                    )

urlpatterns = [
    path('adminPanel/messages/', MessagesView.as_view(), name="messages"),
    path('adminPanel/message/update/<int:pk>', UpdateMessageView.as_view(), name="update-message"),

    path('adminPanel/about/', MyAboutView.as_view(), name="about"),
   
    path('adminPanel/ed_and_work/', MyEdAndWorkView.as_view(), name="ed-and-work"),
    path('adminPanel/ed_and_work/create/', CreatePostEdAndWorkView.as_view(), name="create-post-ed-and-work"),
    path('adminPanel/ed_and_work/update/<int:pk>', UpdatePostEdAndWorkView.as_view(), name="update-post-ed-and-work"),
    path('adminPanel/ed_and_work/delete/<int:pk>', DeletePostEdAndWorkView.as_view(), name="delete-post-ed-and-work"),

    path('adminPanel/cases/', MyCaseView.as_view(), name="cases"),
    path('adminPanel/case/create/', CreateCaseView.as_view(), name="create-case"),
    path('adminPanel/case/update/<int:pk>', UpdateCaseView.as_view(), name="update-case"),
    path('adminPanel/case/delete/<int:pk>', DeleteCaseView.as_view(), name="delete-case"),
  
    path('adminPanel/settings/menu/', UpdateMenuView.as_view(), name="settings-menu"),
    path('adminPanel/settings/paralax/', UpdateParalaxView.as_view(), name="settings-paralax"),

    path("admin-panel/profile/",profile , name="profile"),
    # path('profile/', MyProfileView.as_view(), name="profile")
]