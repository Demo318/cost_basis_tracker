from django.urls import path
from cost_basis_tracker import views

app_name = 'cost_basis_tracker'

urlpatterns =[
    path('', views.index, name='index'),
]