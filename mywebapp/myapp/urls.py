from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name = 'landing page'),
    path('test/', views.test , name ='test'),
    # path('show/',views.show , name='show'),
]