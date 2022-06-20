import unittest
from django.test import TestCase
from django.urls import reverse, resolve
from .views import IndexView, PredictionsView, DetailsView
from .models import Data
import joblib


class TestUrl(TestCase):
    def test_index_response(self):
        response = self.client.get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code, 200)

    def test_predictions_response(self):
        response = self.client.get('http://127.0.0.1:8000/predictions')
        self.assertEqual(response.status_code, 200)

    # def test_details_response(self):                                      ----------------------------- To Do
    #     response = self.client.get('http://127.0.0.1:8000/details/<int:pk>')  
    #     self.assertEqual(response.status_code, 200)

    def test_index_url_resolve(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func.view_class, IndexView)

    def test_predictions_url_resolve(self):
        url = reverse('predictions')
        self.assertEquals(resolve(url).func.view_class, PredictionsView)

    def test_details_url_resolve(self):
        url = reverse('details', args=[3,])
        self.assertEquals(resolve(url).func.view_class, DetailsView)

# class TestPrediction(TestCase):                                            ----------------------------- To Do
    # def test_prediction(self):  
        # ml_model = joblib.load('ml_model/ml_model1.joblib')
        # self.SalePrice = ml_model.predict(
        #     [[LotArea=8450,Street=0,LotShape=3,Neighborhood=5,BldgType=0,
        #         HouseStyle=5,RoofStyle=1,RoofMatl=1,Foundation=2,BsmtQual=2,
        #         TotalBsmtSF=856,HeatingQC=0,CentralAir=1,Electrical=4,FirstFlrSF=856,
        #         SecondFlrSF=854,BsmtFullBath=1,FullBath=2,BedroomAbvGr=3,KitchenAbvGr=1,
        #         TotRmsAbvGrd=8,GarageType=1,GarageArea=548,PavedDrive=2,OpenPorchSF=61,PoolArea=0]])

if __name__ == '__main__':
    unittest.main()