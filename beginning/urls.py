from django.urls import path
from . import views

app_name = 'beginning'
urlpatterns = [
    path('', views.index, name='index'),
    path('logs', views.LogListView.as_view(), name='logs')
]
