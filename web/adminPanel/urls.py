from django.urls import path
from .views import (MessagesView,
                    UpdateMessageView, 
                    DeleteMessageView,
                    MyAboutView, 
                    ServiceView,
                    CreateServiceView,
                    UpdateServiceView,
                    DeleteServiceView,
                    MyEdAndWorkView, 
                    CreatePostEdAndWorkView, 
                    UpdatePostEdAndWorkView, 
                    DeletePostEdAndWorkView,
                    MyCaseView,
                    CreateCaseView,
                    UpdateCaseView,
                    DeleteCaseView,
                    FeedbackView,
                    CreateFeedbackView,
                    UpdateFeedbackView,
                    DeleteFeedbackView,
                    ContactView,
                    CreateContactView,
                    UpdateContactView,
                    DeleteContactView,
                    UpdateMenuView,
                    UpdateParalaxView,
                    LogsView,
                    ProfileView,
                    UserPasswordChange,
                    RegisterView
                    )
from django.contrib.auth.views import PasswordChangeDoneView

urlpatterns = [
    path('adminPanel/messages/', MessagesView.as_view(), name="messages"),
    path('adminPanel/message/update/<int:pk>', UpdateMessageView.as_view(), name="update-message"),
    path('adminPanel/message/delete/<int:pk>', DeleteMessageView.as_view(), name="delete-message"),

    path('adminPanel/about/', MyAboutView.as_view(), name="about"),

    path('adminPanel/services/', ServiceView.as_view(), name="services"),
    path('adminPanel/service/create/', CreateServiceView.as_view(), name="create-service"),
    path('adminPanel/service/update/<int:pk>', UpdateServiceView.as_view(), name="update-service"),
    path('adminPanel/service/delete/<int:pk>', DeleteServiceView.as_view(), name="delete-service"),

    path('adminPanel/ed_and_work/', MyEdAndWorkView.as_view(), name="ed-and-work"),
    path('adminPanel/ed_and_work/create/', CreatePostEdAndWorkView.as_view(), name="create-post-ed-and-work"),
    path('adminPanel/ed_and_work/update/<int:pk>', UpdatePostEdAndWorkView.as_view(), name="update-post-ed-and-work"),
    path('adminPanel/ed_and_work/delete/<int:pk>', DeletePostEdAndWorkView.as_view(), name="delete-post-ed-and-work"),

    path('adminPanel/cases/', MyCaseView.as_view(), name="cases"),
    path('adminPanel/case/create/', CreateCaseView.as_view(), name="create-case"),
    path('adminPanel/case/update/<int:pk>', UpdateCaseView.as_view(), name="update-case"),
    path('adminPanel/case/delete/<int:pk>', DeleteCaseView.as_view(), name="delete-case"),

    path('adminPanel/feedbacks/', FeedbackView.as_view(), name="feedbacks"),
    path('adminPanel/feedback/create/', CreateFeedbackView.as_view(), name="create-feedback"),
    path('adminPanel/feedback/update/<int:pk>', UpdateFeedbackView.as_view(), name="update-feedback"),
    path('adminPanel/feedback/delete/<int:pk>', DeleteFeedbackView.as_view(), name="delete-feedback"),

    path('adminPanel/contacts/', ContactView.as_view(), name="contacts"),
    path('adminPanel/contact/create/', CreateContactView.as_view(), name="create-contact"),
    path('adminPanel/contact/update/<int:pk>', UpdateContactView.as_view(), name="update-contact"),
    path('adminPanel/contact/delete/<int:pk>', DeleteContactView.as_view(), name="delete-contact"),
  
    path('adminPanel/settings/menu/', UpdateMenuView.as_view(), name="settings-menu"),
    path('adminPanel/settings/paralax/', UpdateParalaxView.as_view(), name="settings-paralax"),
    path('adminPanel/settings/logs/', LogsView.as_view(), name="settings-logs"),

    path("adminPanel/profile/",ProfileView.as_view() , name="profile"),
    path('adminPanel/password-change/', UserPasswordChange.as_view(), name='password_change'),
    path('adminPanel/password-change/done/', PasswordChangeDoneView.as_view(template_name="adminPanel/password_change_done.html"), name="password_change_done"),
    path('adminPanel/register/',RegisterView.as_view(),name='register'),
]