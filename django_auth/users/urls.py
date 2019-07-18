from .views import CreateUserAPIView, authenticate_user, UserRetrieveUpdateAPIView
from django.urls import path
 
urlpatterns = [
    path('create/', CreateUserAPIView.as_view()),
    path('obtain_token/', authenticate_user),
    path('update/', UserRetrieveUpdateAPIView.as_view()),
]