from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, CustomPasswordResetForm
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
from django.urls import reverse_lazy


def register(request): 
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            course = form.cleaned_data.get('course')
            user.groups.add(course)
            messages.success(request, f'Your account has been created! Now you can login!')
            return redirect('login')
        else:
            messages.warning(request, 'Unable to create account!')

        return redirect('itreporting:home')
    else:
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form , 'title': 'Student Registration'})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if u_form.is_valid and p_form.is_valid:
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been successfully updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)

    context = {'u_form': u_form, 'p_form': p_form, 'title': 'Student Profile'}
    return render(request, 'users/profile.html', context)



class CustomPasswordResetView(PasswordResetView):   
    form_class = CustomPasswordResetForm
    template_name = 'users/password_reset_form.html'  
    success_url = reverse_lazy('itreporting:password_reset_done')  
    email_template_name = 'users/password_reset_email.html'

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'


def custom_password_reset_complete(request):
    return render(request, 'users/password_reset_complete.html')

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'users/password_reset_confirm.html'
    success_url = reverse_lazy('itreporting:password_reset_complete')
