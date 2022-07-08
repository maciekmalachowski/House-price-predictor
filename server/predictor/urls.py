from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('predictions', PredictionsView.as_view(), name='predictions'),
    path('details/<int:pk>', DetailsView.as_view(), name='details'),

    path('accounts/login/', loginPage, name='login'),
    path('accounts/register/', registerPage, name='register'),
    path('logout/', userLogout, name='logout'),
]