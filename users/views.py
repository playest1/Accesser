from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profession
from django.views.generic import DetailView
from .models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST)
        p_form = ProfileUpdateForm(request.POST, request.FILES)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been created! You are now able to login')
            return redirect('login')
    else:
        u_form = UserUpdateForm()
        p_form = ProfileUpdateForm()

    #     form = UserRegisterForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         messages.success(request, f'Your account has been created! You are now able to login')
    #         return redirect('login')
    # else:
    #     form = UserRegisterForm()
    return render(request, 'users/register.html', {'u_form': u_form, 'p_form': p_form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {
        'u_form': u_form,
        'p_form': p_form
    }


    return render(request, 'users/profile.html', context)


def users_by_profession(request, profession):
    profession = get_object_or_404(Profession, name=profession)
    context = {"profession":profession}
    return render(request, 'users/user_profession.html',context)


class UserDetailView(DetailView):
    model = User
    template_name = 'users/user_details.html'
    context_object_name = "user"