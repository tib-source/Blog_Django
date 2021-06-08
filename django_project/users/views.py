from django.shortcuts import redirect, render
from django.contrib import messages
from .form import UserRegisterFrom
from django.contrib.auth.decorators import login_required
def register(request):

    if request.method == "POST":
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('login')
        else:
            form = UserRegisterFrom()
    else:
        form = UserRegisterFrom()
    context = {'form':form}
    return render(request, 'users/register.html', context )

def login(request):
    pass

@login_required
def profile(request):
    context = {}
    return render(request, 'users/profile.html', context)