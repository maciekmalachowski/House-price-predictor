from django.db import models
from django.core.validators import MinValueValidator
from sklearn.ensemble import RandomForestRegressor
import joblib

GENDER = (
    (0, 'Female'),
    (1, 'Male'),
)


class Data(models.Model):
    name = models.CharField(max_length=100, null=True)
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(13)], null=True)
    height = models.PositiveIntegerField(null=True)
    sex = models.PositiveIntegerField(choices=GENDER, null=True)
    predictions = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/ml_model.joblib')
        self.predictions = ml_model.predict(
            [[self.age, self.height, self.sex]])
        return super().save(*args, *kwargs)


    def __str__(self):
        return self.name