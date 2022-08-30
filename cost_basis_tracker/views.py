from django.shortcuts import render, redirect
from cost_basis_tracker.forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.http import HttpResponse

def index(request):
    return render(request, 'cost_basis_tracker/index.html')

def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("cost_basis_tracker:index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request, 'cost_basis_tracker/register.html', context={'register_form':form})
