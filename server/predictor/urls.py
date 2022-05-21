from django.urls import path
from .views import IndexView, PredictionsView, DetailsView

urlpatterns = [
    path('', IndexView, name='index'),
    path('predictions', PredictionsView, name='predictions'),
    path('details/<int:pk>', DetailsView, name='details')
]