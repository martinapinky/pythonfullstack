from django.shortcuts import render, redirect
from .models import Painting, Category
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm  # For user registration and login forms
from django.contrib.auth import login, logout  # For handling user login and logout
from django.contrib import messages  # For showing messages like error or success

# Create your views here.
def painting_list(request):
    paintings = Painting.objects.all()
    return render(request, 'painting_list.html', {'paintings': paintings})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def home(request):
    return render(request , 'home.html')

# User registration view
def register(request):
    # Check if the HTTP method is POST (form submission)
    if request.method == 'POST':
        # Create an instance of the UserCreationForm with the data from the request
        form = UserCreationForm(request.POST)
       
        # Check if the form is valid
        if form.is_valid():
            # If the form is valid, save the new user and create an instance of the user
            user = form.save()
           
            # Automatically log the user in after successful registration
            login(request, user)
           
            # Redirect to the 'home' page after successful login
            return redirect('home')
        else:
            # If the form is not valid, show an error message
            messages.error(request, "Registration failed. Please try again.")
    else:
        # If the request method is GET (form load), instantiate an empty form
        form = UserCreationForm()

    # Render the registration page with the form
    return render(request, 'register.html', {'form': form})

# User login view
def loginview(request):
    # Check if the HTTP method is POST (form submission)
    if request.method == 'POST':
        # Create an instance of the AuthenticationForm with data from the POST request
        form = AuthenticationForm(data=request.POST)
       
        # Check if the form is valid
        if form.is_valid():
            # If valid, get the user object from the form
            user = form.get_user()
           
            # Log the user in
            login(request, user)
           
            # Redirect to the 'home' page after successful login
            return redirect('home')
        else:
            # If the form is not valid, display an error message
            messages.error(request, "Invalid credentials. Please try again.")
            # Re-render the login form with the error messages
            return render(request, 'login.html', {'form': form})
    else:
        # If the request method is GET (form load), create an empty AuthenticationForm instance
        form = AuthenticationForm()

    # Render the login page with the form
    return render(request, 'login.html', {'form': form})

# User logout view
def logoutview(request):
    logout(request)  # Log the user out
    return redirect('home')  # Redirect to home page after logout