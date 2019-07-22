from .views import CreateUserAPIView, authenticate_user, UserRetrieveUpdateAPIView, current_user
from django.urls import path
 
urlpatterns = [
    path('create/', CreateUserAPIView.as_view()),
    path('auth/', authenticate_user),
    #path('update/', views.UserRetrieveUpdateAPIView),
    path('get_current/', current_user),
]