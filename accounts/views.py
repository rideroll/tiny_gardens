from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class SignUp(generic.CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/tiny_gardens/'
    template_name = 'signup.html'