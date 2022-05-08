from django.shortcuts import render

def IndexView(request):
    return render(request, 'index.html')

def PredictionsView(request):
    return render(request, 'predictions.html')
