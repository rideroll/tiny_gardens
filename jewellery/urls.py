from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.JewelleryList.as_view(), name='jewellery')
]