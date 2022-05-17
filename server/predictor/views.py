from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import DataForm
from .models import Data

def IndexView(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('predictions')
    else:
        form = DataForm()
    context = {
        'form' : form
    }
    return render(request, 'index.html', context)

def PredictionsView(request):
    predicted_SalePrice = Data.objects.all()
    context = {
        'predictions' : predicted_SalePrice
    }
    return render(request, 'predictions.html', context)
