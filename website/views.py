from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    #check to see if user is logged in or not
    if request.method == 'POST':
        #process the form data
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Log the user in
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('home')  # Redirect to the home page or any other page
        else:
            messages.success(request, 'Invalid username or password.')
            return redirect('home')  # Redirect back to the login page
        
    return render(request, 'home.html', {})

def login_user(request):
    # return render(request, 'login.html', {})
    pass
def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {})