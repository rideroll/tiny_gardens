from django.shortcuts import render
from django.views import generic

from .models import Jewellery

class JewelleryList(generic.ListView):
    model = Jewellery
    template_name = 'jewellery_list.html'
    context_object_name = 'jewellery'