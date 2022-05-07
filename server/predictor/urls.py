from django.urls import path
from .views import IndexView, PredictionsView

urlpatterns = [
    path('', IndexView, name='index'),
    path('predictions', PredictionsView, name='predictions'),
]