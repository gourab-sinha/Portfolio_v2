from django.urls import path
from user import views as user_views
app_name = 'user'
urlpatterns = [
    path('user/', user_views.user, name='user')
]
