from django.urls import path
from .user_views.create_account import CreateAccount
from .user_views.view_account import ViewAccount
from .user_views.profile_view import ProfileView
from django.contrib.auth import views as auth_views


app_name = 'user'
urlpatterns = [
    path('register/', CreateAccount.as_view(), name='register'),
    path('user/', ViewAccount.as_view(), name='user'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name="logout"),
    path('profile/', ProfileView.as_view(), name='profile'),
]
