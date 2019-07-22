from . import views
from django.urls import path
 
urlpatterns = [
    path('create/', views.CreateUserAPIView),
    path('auth/', views.authenticate_user),
    #path('update/', views.UserRetrieveUpdateAPIView),
    path('get_current/', views.current_user),
]