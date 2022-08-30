from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'cost_basis_tracker/index.html')


