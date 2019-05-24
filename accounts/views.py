from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponseRedirect


def redirect_user(request):
    url = f'/jewellery/'
    return HttpResponseRedirect(url)



class SignUp(generic.CreateView):
    model = User
    form_class = UserCreationForm
    success_url = '/jewellery/'
    template_name = 'signup.html'



# class UserDetail(generic.DetailView):
#     model = ProfileUser
#     template_name = 'user_profile.html'
#     context_object_name = 'user' 