from django.urls import path
from .views import IndexView, PredictionsView, DetailsView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('predictions', PredictionsView.as_view(), name='predictions'),
    path('details/<int:pk>', DetailsView.as_view(), name='details')
]