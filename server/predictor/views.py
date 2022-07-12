from re import template
from django.views.generic import CreateView, ListView, DetailView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# from django.core.mail import EmailMessage
# from django.template.loader import render_to_string
from django.db import models
# from django.conf import settings
from itertools import chain

from .forms import DataForm, CreateUserForm
from .models import Data, PredictionAuthor

class Account(models.Model):
    def loginPage(request):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect('index')
                
                else:
                    messages.info(request, 'Username OR password is incorrect')

            context = {}
            return render(request, 'accounts/login.html', context)

    def registerPage(request):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            form = CreateUserForm()

            if request.method == 'POST':
                form = CreateUserForm(request.POST)
                if form.is_valid():
                    form.save()
                    username = form.cleaned_data.get('username')
                    messages.success(request, 'Account was created for ' + username)
                    ## Google chenged privacy policy and blocked sending emails that easily as it was before
                    # email = EmailMessage( 
                    #     subject='Thanks for registration !',
                    #     body=render_to_string('accounts/email.html', {'username': form.cleaned_data.get('username')}),
                    #     from_email=settings.EMAIL_HOST_USER,
                    #     to=[form.cleaned_data.get('email')]
                    # )
                    # email.send()
                    return redirect('login')

            context = {'form': form}
            return render(request, 'accounts/register.html', context)
            
    def userLogout(request):
        logout(request)
        return redirect('login')


class IndexView(CreateView):
    template_name = 'index.html'
    form_class = DataForm
    queryset = Data.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class PredictionsView(ListView):
    template_name = 'predictions.html'
    queryset = list(chain(Data.objects.all(), PredictionAuthor.objects.all()))


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class DetailsView(DetailView):
    template_name = 'details.html'
    queryset = Data.objects.all()

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)