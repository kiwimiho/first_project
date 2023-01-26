
from django.urls import path
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users/',views.users,name='users'),
    path('showusers/',views.showusers,name='showusers'),
    path('formpage/',views.form_name_view,name='formpage'),
]
