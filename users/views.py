from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, CustomAuthenticationForm

# Create your views here.

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account Created For {username}!')
			return redirect('shop')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form2 = CustomAuthenticationForm(request.POST)
        if form2.is_valid():
            form2.save()
            return redirect('shop')
    else:
        form2 = CustomAuthenticationForm()
    return render(request, 'users/login.html', context={'form': form2})