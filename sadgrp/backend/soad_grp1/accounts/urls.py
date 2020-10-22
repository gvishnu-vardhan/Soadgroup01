from django.urls import path
from .views import   CurrentUserView, RegisterView,LogoutAPIView,SetNewPasswordAPIView,LoginAPIView,PasswordTokenCheckAPI,RequestPasswordResetEmail

urlpatterns = [
   path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginAPIView.as_view(), name="login"),
    path('logout/', LogoutAPIView.as_view(), name="logout"),
    path('user/<slug:slug>/',CurrentUserView.as_view(),name="user"),
    path('request-reset-email/', RequestPasswordResetEmail.as_view(), name="request-reset-email"),
    path('password-reset/<uidb64>/<token>/',PasswordTokenCheckAPI.as_view(),name="password-reset-confirm"),
    path('password-reset-complete', SetNewPasswordAPIView.as_view(),name='password-reset-complete')
]