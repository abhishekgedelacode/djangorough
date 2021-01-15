from django.urls import path
from . import views

app_name = "codeapp"

urlpatterns = [
    path('', views.index, name='index_codeapp'),
    path('about/', views.about, name='about_codeapp'),
    path('details/', views.details, name='details_codeapp'),
    path('time/', views.time_view, name='time_codeapp'),
    path('list/', views.list_view, name='list_codeapp'),
    path('login/', views.form_view, name='form_codeapp'),
    path('name/', views.name_view, name='name_codeapp'),
]
