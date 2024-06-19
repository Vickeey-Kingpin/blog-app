from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('mypost/<str:pk>',views.getpost,name='mypost')
]