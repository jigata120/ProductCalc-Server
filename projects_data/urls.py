
from . import views
from django.urls import path

from .views import CustomTokenObtainPairView, UserProfileView, UserDetailView, ProjectDetailView
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterView, ProjectListView

urlpatterns = [
     path('users/', views.UserProfileList.as_view(), name='user-list'),
    path('users/<uuid:pk>/', views.UserProfileDetail.as_view(), name='user-detail'),
    path('users/create/', views.UserProfileCreateView.as_view(), name='user-create'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('user/', UserDetailView.as_view(), name='user_detail'),
    path('user-profile/', UserProfileView.as_view(), name='user-profile'),
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),  # Add this line

]