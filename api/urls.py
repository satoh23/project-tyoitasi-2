from django.urls import path

from api.views.accounts import (LoginView, LogoutView, get_refresh_view,
                                EditUserView, EditUserNotIconView)

from api.views.article import (CreateView, CreateNotThumbnailView,
                               ListCategoryView, ListDetailView, GetDetailArticleView)

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('token-refresh/', get_refresh_view().as_view()),
    path('edit-user/', EditUserView.as_view()),
    path('edit-user-not-icon/', EditUserNotIconView.as_view()),

    path('create-article/', CreateView.as_view()),
    path('create-article-not-thumbnail/', CreateNotThumbnailView.as_view()),
    path('get-list-article/', ListDetailView.as_view()),
    path('get-list-category/', ListCategoryView.as_view()),
    path('get-detail-article/<str:pk>/', GetDetailArticleView.as_view()),
]
