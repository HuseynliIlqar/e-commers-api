from django.urls import path
from .views import (RegisterView, LoginView,
                            LogoutView, PasswordChangeView,
                            ActivateAccountView)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('password-change/', PasswordChangeView.as_view(), name='password-change'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('activate/<uidb64>/<token>/', ActivateAccountView.as_view(), name='activate'),

]
