from multiprocessing import context
from django.shortcuts import render
from .forms import DataForm
from .models import Data
from django.views.generic import CreateView, ListView, DetailView

class IndexView(CreateView):
    template_name = 'index.html'
    form_class = DataForm
    queryset = Data.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

class PredictionsView(ListView):
    template_name = 'predictions.html'
    queryset = Data.objects.all()

class DetailsView(DetailView):
    template_name = 'details.html'
    queryset = Data.objects.all()
