from django.views.generic import CreateView, ListView, DetailView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import DataForm, CreateUserForm
from .models import Data

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
    queryset = Data.objects.all()

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class DetailsView(DetailView):
    template_name = 'details.html'
    queryset = Data.objects.all()

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)