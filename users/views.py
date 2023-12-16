from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.views import PasswordResetView


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



# class CustomPasswordResetView(PasswordResetView):
#     template_name = 'password_reset_form.html'  # Custom template for the password reset form
#     success_url = '/custom_reset_done/'  # Redirect URL after a successful password reset request
#     email_template_name = 'custom_password_reset_email.html'  # Custom email template

#     # You can override other methods or add custom logic as needed
#     def form_valid(self, form):
#         # Add your custom logic here
#         # For example, you can log something or perform additional actions
#         return super().form_valid(form)