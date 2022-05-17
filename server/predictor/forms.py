from django import forms
from .models import Data

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
