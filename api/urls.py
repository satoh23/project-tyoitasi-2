from django.urls import path

from api.views import (LoginView, LogoutView, get_refresh_view,
                       EditUserView)

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('token-refresh/', get_refresh_view().as_view()),

    path('edit-user/', EditUserView.as_view()),
]
