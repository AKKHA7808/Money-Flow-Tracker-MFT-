
from django.shortcuts import render, redirect
from django.contrib import messages
from .public_password_reset_form import PublicPasswordResetForm
from .models import CustomUser
from django.contrib.auth.hashers import make_password

def public_password_reset(request):
    if request.method == 'POST':
        form = PublicPasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            new_password = form.cleaned_data['new_password1']
            user = CustomUser.objects.get(email=email)
            user.password = make_password(new_password)
            user.save()
            messages.success(request, 'Password changed successfully! You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PublicPasswordResetForm()
    return render(request, 'accounts/public_password_reset.html', {'form': form})
