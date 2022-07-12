from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('predictions', PredictionsView.as_view(), name='predictions'),
    path('details/<int:pk>', DetailsView.as_view(), name='details'),

    path('accounts/login/', Account.loginPage, name='login'),
    path('accounts/register/', Account.registerPage, name='register'),
    path('logout/', Account.userLogout, name='logout'),
]