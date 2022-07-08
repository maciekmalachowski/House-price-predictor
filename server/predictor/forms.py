from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Data

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['LotArea', 'LotShape', 'BldgType', 'HouseStyle',
                'Neighborhood', 'Street', 'FirstFlrSF', 'SecondFlrSF',
                'BedroomAbvGr', 'KitchenAbvGr', 'TotRmsAbvGrd', 'FullBath',
                'BsmtQual', 'TotalBsmtSF', 'BsmtFullBath', 'GarageType', 
                'GarageArea', 'RoofStyle', 'RoofMatl', 'Foundation', 
                'PavedDrive', 'OpenPorchSF', 'PoolArea', 'HeatingQC',
                'CentralAir', 'Electrical']
        labels = {
            'LotArea' : '<h5> Lot size in square feet </h5>', 
            'LotShape' : '</br><h5> General shape of property </h5>', 
            'BldgType' : '</br><h5> Type of dwelling </h5>', 
            'HouseStyle' : '</br><h5> Style of dwelling</h5>',
            'Neighborhood' : '</br><h5> Physical locations within Ames city limits </h5>', 
            'Street' : '</br><h5> Type of road access </h5>', 
            'FirstFlrSF' : '</br><h5> First Floor square feet </h5>', 
            'SecondFlrSF' : '</br><h5> Second floor square feet </h5>',
            'BedroomAbvGr' : '</br><h5> Number of bedrooms above basement level </h5>', 
            'KitchenAbvGr' : '</br><h5> Number of kitchens </h5>', 
            'TotRmsAbvGrd' : '</br><h5> Total rooms above grade (does not include bathrooms) </h5>', 
            'FullBath' : '</br><h5> Full bathrooms above grade </h5>',
            'BsmtQual' : '</br><h5> Basement quality </h5>', 
            'TotalBsmtSF' : '</br><h5> Total square feet of basement area </h5>', 
            'BsmtFullBath' : '</br><h5> Basement full bathrooms </h5>', 
            'GarageType' : '</br><h5> Garage type </h5>', 
            'GarageArea' : '</br><h5> Size of garage in square feet </h5>', 
            'RoofStyle' : '</br><h5> Type of roof </h5>', 
            'RoofMatl' : '</br><h5> Roof material </h5>', 
            'Foundation' : '</br><h5> Type of foundation </h5>', 
            'PavedDrive' : '</br><h5> Paved driveway </h5>', 
            'OpenPorchSF' : '</br><h5> Open porch area in square feet </h5>', 
            'PoolArea' : '</br><h5> Pool area in square feet </h5>', 
            'HeatingQC' : '</br><h5> Heating quality and condition </h5>',
            'CentralAir' : '</br><h5> Central air conditioning </h5>', 
            'Electrical' : '</br><h5> Electrical system </h5>',
        }