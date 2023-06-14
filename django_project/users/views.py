from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already registered.')
                return redirect('register')
            form.save()
            messages.success(request, f'Account created success!')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

class MyLoginView(LoginView):
    template_name = 'login.html'

    def form_invalid(self,form):
        messages.error(self.request,'Login failed!')
        return super().form_invalid(form)

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your profile has been update!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(request, 'users/profile.html', context)

