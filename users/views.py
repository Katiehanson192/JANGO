'''
-we want the register() view function to display a blank registration form when
registration page is 1st requested,

-process completed registration forms when they're submitted,

-if registration = successful, user should be automatically logged in
'''

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request): 
    """Register a new user"""
    if request.method != 'POST':
        #display blank registration form.
        form = UserCreationForm()
    else:
        form =UserCreationForm(data=request.POST) #saving information to the DB
            #username has appropriate characters, passwords match (w/username),
            #& user isn't trying to do anything malicious in their submission
        if form.is_valid():
        #the save() method returns the newly created user object,which we assign to new_user
            new_user = form.save()
            #log the user in and then redirect to the home page
            login(request, new_user)
            return redirect('MainApp:index')

    #display a blank or invalid form
    context = { 'form': form}
    return render(request,'registration/register.html', context)