# /notekeeper/accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, FormView
from django.urls import reverse_lazy
from .forms import UserRegistrationForm, OrganizationRegistrationForm

class IndividualSignUpView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_individual = True
        user.save()
        return super().form_valid(form)

class OrganizationSignUpView(CreateView):
    form_class = OrganizationRegistrationForm
    template_name = 'accounts/org_signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        organization = form.save()
        user = form.save_user(commit=False)
        user.organization = organization
        user.is_individual = False
        user.save()
        return super().form_valid(form)