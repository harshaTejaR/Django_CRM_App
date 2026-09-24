from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record


# Create your views here.
def home(request):
    records = Record.objects.all()
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
    else:
        return render(request, 'home.html', {'records': records})    
    return render(request, 'home.html', {})

def login_user(request):
    # return render(request, 'login.html', {})
    pass
def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and log in the user after successful registration
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('home')  # Redirect to the home page or any other page
        else:
            messages.error(request, 'Unsuccessful registration. Invalid information.')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    return render(request, 'register.html', {'form': form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look up the record
        try:
            customer_record = Record.objects.get(id=pk)
        except Record.DoesNotExist:
            messages.success(request, 'Record not found.')
            return redirect('home')
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, 'You must be logged in to view that page.')
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        try:
            customer_record = Record.objects.get(id=pk)
            customer_record.delete()
            messages.success(request, 'Record deleted successfully.')
        except Record.DoesNotExist:
            messages.success(request, 'Record not found.')
    else:
        messages.success(request, 'You must be logged in to delete a record.')
    return redirect('home')

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                add_record = form.save()
                messages.success(request, 'Record added successfully.')
                return redirect('home')  # Redirect to the home page or any other page
        return render(request, 'add_record.html', {'form': form})
    else:
            messages.success(request, 'You must be logged in to add a record.')
            return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        try:
            customer_record = Record.objects.get(id=pk)
        except Record.DoesNotExist:
            messages.success(request, 'Record not found.')
            return redirect('home')
        
        form = AddRecordForm(request.POST or None, instance=customer_record)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Record updated successfully.')
                return redirect('home')  # Redirect to the home page or any other page
        return render(request, 'update_record.html', {'form': form, 'customer_record': customer_record})
    else:
        messages.success(request, 'You must be logged in to update a record.')
        return redirect('home')