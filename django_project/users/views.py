from django.dispatch.dispatcher import receiver
from django.shortcuts import redirect, render
from django.contrib import messages
from .form import UserProfileForm, UserRegisterFrom, UserUpdateForm
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



@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been Updated ')
            redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'users/profile.html', context)