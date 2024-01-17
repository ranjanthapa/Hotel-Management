from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def staff_login(request):
    
    error_message = 'Error!'
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('staff_dashboard')
        
        error_message = 'Invalid credentials. Please try again.'
    else:
        
        form = AuthenticationForm()

    return render(request, 'staff/login.html', {'form': form, 'error_message': error_message})

@login_required
def staff_dashboard(request):
    return render(request, 'staff/staff_dashboard.html')

def staff_logout(request):
    logout(request)
    return redirect('staff_login')
