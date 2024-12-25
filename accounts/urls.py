# /notekeeper/accounts/urls.py

from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import IndividualSignUpView, OrganizationSignUpView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='accounts:login'), name='logout'),
    path('signup/', IndividualSignUpView.as_view(), name='individual_signup'),
    path('signup/organization/', OrganizationSignUpView.as_view(), name='org_signup'),
]