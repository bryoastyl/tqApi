from django.urls import path, include
from knox import views as knox_views
from .Views.api import RegisterAPI, LoginAPI, UserAPI, ChangePasswordAPI


urlpatterns = [
    path('auth', include('knox.urls')),
    path('auth/register', RegisterAPI.as_view()),
    path('auth/login', LoginAPI.as_view()),
    path('auth/user', UserAPI.as_view()),
    path('auth/user/password/change', ChangePasswordAPI.as_view()),
    path('auth/logout', knox_views.LogoutView.as_view(), name="knox_logout")
]
