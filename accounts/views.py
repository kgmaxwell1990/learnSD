from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView

from .forms import UserLoginForm, UserRegistrationForm
from .mixins import AjaxTemplateMixin

def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect('home')
    
class CustomLoginView(AjaxTemplateMixin, LoginView):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm
    
def profile(request):
    return render(request, 'accounts/profile.html')

def register(request):
    redirect_to = request.GET.get('next', 'profile')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            user = auth.authenticate(username=request.POST.get('username'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect('home')

        else:
            messages.error(request, "unable to register you at this time!")

    else:
        form = UserRegistrationForm()


    return redirect('home')

