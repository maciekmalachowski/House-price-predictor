from django.db import models
from django.core.validators import MinValueValidator
from sklearn.ensemble import RandomForestRegressor
import joblib


LOTSHAPE_V = (
    (3, 'Regular'),
    (0, 'Slightly irregular'),
    (1, 'Moderately Irregular'),
    (2, 'Irregular'),
)

STREET_V = (
    (0, 'Gravel'),
    (1, 'Paved'),
)

NEIGHBORHOOD_V = (
    (0, 'Bloomington Heights'),
    (1, 'Bluestem'),
    (2, 'Briardale'),
    (3, 'Brookside'),
    (4, 'Clear Creek'),
    (5, 'College Creek'),
    (6, 'Crawford'),
    (7, 'Edwards'),
    (8, 'Gilbert'),
    (9, 'Iowa DOT and Rail Road'),
    (10, 'Meadow Village'),
    (11, 'Mitchell'),
    (12, 'Northwest Ames'),
    (13, 'Northpark Villa'),
    (14, 'North Ames'),
    (15, 'Northridge'),
    (16, 'Northridge Heights'),
    (17, 'Old Town'),
    (18, 'South & West of Iowa State University'),
    (19, 'Sawyer'),
    (20, 'Sawyer West'),
    (21, 'Somerset'),
    (22, 'Stone Brook'),
    (23, 'Timberland'),
    (24, 'Veenker'),
)

BLDGTYPE_V = (
    (0, 'Single-family Detached'),
    (1, 'Two-family Conversion; originally built as one-family dwelling'),
    (2, 'Duplex'),
    (4, 'Townhouse End Unit'),
    (3, 'Townhouse Inside Unit'),
)

HOUSESTYLE_V = (
    (2, 'One story'),
    (0, 'One and one-half story: 2nd level finished'),
    (1, 'One and one-half story: 2nd level unfinished'),
    (5, 'Two story'),
    (3, 'Two and one-half story: 2nd level finished'),
    (4, 'Two and one-half story: 2nd level unfinished'),
    (6, 'Split Foyer'),
    (7, 'Split Level'),
)

ROOFSTYLE_V = (
    (0, 'Flat'),
    (1, 'Gable'),
    (2, 'Gabrel (Barn)'),
    (3, 'Hip'),
    (4, 'Mansard'),
    (5, 'Shed'),

)

ROOFMATL_V = (
    (0, 'Clay or Tile'),
    (1, 'Standard (Composite) Shingle'),
    (2, 'Membrane'),
    (3, 'Metal'),
    (4, 'Roll'),
    (5, 'Gravel & Tar'),
    (6, 'Wood Shakes'),
    (7, 'Wood Shingles'),
)

FOUNDATION_V = (
    (0, 'Brick & Tile'),
    (1, 'Cinder Block'),
    (2, 'Poured Contrete'),
    (3, 'Slab'),
    (4, 'Stone'),
    (5, 'Wood'),
)

BSMTQUAL_V = (
    (0, 'Excellent (100+ inches)'),
    (2, 'Good (90-99 inches)'),
    (3, 'Typical (80-89 inches)'),
    (1, 'Fair (70-79 inches)'),
)

CENTRALAIR_V = (
    (1, 'Yes'),
    (0, 'No'),
)

HEATINGQC_V = (
    (0, 'Excellent'),
    (2, 'Good'),
    (4, 'Average/Typical'),
    (1, 'Fair'),
    (3, 'Poor'),
)

ELECTRICAL_V = (
    (4, 'Standard Circuit Breakers & Romex'),
    (0, 'Fuse Box over 60 AMP and all Romex wiring (Average)'),
    (1, '60 AMP Fuse Box and mostly Romex wiring (Fair)'),
    (2, '60 AMP Fuse Box and mostly knob & tube wiring (poor)'),
    (3, 'Mixed'),
)

GARAGETYPE_V = (
    (1, 'Attached to home'),
    (2, 'Basement Garage'),
    (3, 'Built-In (Garage part of house - typically has room above garage)'),
    (4, 'Car Port'),
    (5, 'Detached from home'),
    (0, 'More than one type of garage'),
)

PAVEDDRIVE_V = (
    (2, 'Paved '),
    (1, 'Partial Pavement'),
    (0, 'Dirt/Gravel'),
)

class Data(models.Model):
    LotArea = models.PositiveIntegerField(validators=[MinValueValidator(0)],null=True)
    LotShape = models.PositiveIntegerField(choices=LOTSHAPE_V, null=True)
    BldgType = models.PositiveIntegerField(choices=BLDGTYPE_V, null=True)
    HouseStyle = models.PositiveIntegerField(choices=HOUSESTYLE_V, null=True)
    Neighborhood = models.PositiveIntegerField(choices=NEIGHBORHOOD_V, null=True)
    Street = models.PositiveIntegerField(choices=STREET_V, null=True)
    FirstFlrSF = models.PositiveIntegerField(validators=[MinValueValidator(0)],null=True)
    SecondFlrSF = models.PositiveIntegerField(validators=[MinValueValidator(0)],null=True)
    BedroomAbvGr = models.PositiveIntegerField(validators=[MinValueValidator(0)],null=True)
    KitchenAbvGr = models.PositiveIntegerField(validators=[MinValueValidator(0)],null=True)
    TotRmsAbvGrd = models.PositiveIntegerField(validators=[MinValueValidator(0)],null=True)
    FullBath = models.PositiveIntegerField(validators=[MinValueValidator(0)],null=True)
    BsmtQual = models.PositiveIntegerField(choices=BSMTQUAL_V, null=True)
    TotalBsmtSF = models.PositiveIntegerField(validators=[MinValueValidator(0)],null=True)
    BsmtFullBath = models.PositiveIntegerField(validators=[MinValueValidator(0)],null=True)
    GarageType = models.PositiveIntegerField(choices=GARAGETYPE_V, null=True)
    GarageArea = models.PositiveIntegerField(validators=[MinValueValidator(0)],null=True)
    RoofStyle = models.PositiveIntegerField(choices=ROOFSTYLE_V, null=True)
    RoofMatl = models.PositiveIntegerField(choices=ROOFMATL_V, null=True)
    Foundation = models.PositiveIntegerField(choices=FOUNDATION_V, null=True)
    PavedDrive = models.PositiveIntegerField(choices=PAVEDDRIVE_V, null=True)
    OpenPorchSF = models.PositiveIntegerField(validators=[MinValueValidator(0)],null=True)
    PoolArea = models.PositiveIntegerField(validators=[MinValueValidator(0)],null=True) 
    HeatingQC = models.PositiveIntegerField(choices=HEATINGQC_V, null=True)
    CentralAir = models.PositiveIntegerField(choices=CENTRALAIR_V, null=True)
    Electrical = models.PositiveIntegerField(choices=ELECTRICAL_V, null=True)
    SalePrice = models.PositiveIntegerField(blank=True)

    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/ml_model1.joblib')
        self.SalePrice = ml_model.predict(
            [[self.LotArea, self.Street, self.LotShape, self.Neighborhood,
            self.BldgType, self.HouseStyle, self.RoofStyle, self.RoofMatl,
            self.Foundation, self.BsmtQual, self.TotalBsmtSF, self.HeatingQC,
            self.CentralAir, self.Electrical, self.FirstFlrSF, self.SecondFlrSF,
            self.BsmtFullBath, self.FullBath, self.BedroomAbvGr, self.KitchenAbvGr,
            self.TotRmsAbvGrd, self.GarageType, self.GarageArea, self.PavedDrive,
            self.OpenPorchSF, self.PoolArea]])
        return super().save(*args, *kwargs)