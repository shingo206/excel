from django.urls import path
from . import views

app_name = 'beginning'
urlpatterns = [
    path('', views.SalesListView.as_view(), name='sales'),
    path('update/<int:pk>', views.SalesUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.SalesDeleteView.as_view(), name='delete'),
    path('create', views.create, name='create'),
]
