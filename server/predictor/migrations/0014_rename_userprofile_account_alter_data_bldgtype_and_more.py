# Generated by Django 4.0.4 on 2022-07-11 14:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('predictor', '0013_alter_data_bldgtype_alter_data_bsmtqual_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='Account',
        ),
        migrations.AlterField(
            model_name='data',
            name='BldgType',
            field=models.PositiveIntegerField(choices=[(3, 'Townhouse Inside Unit'), (2, 'Duplex'), (0, 'Single-family Detached'), (4, 'Townhouse End Unit'), (1, 'Two-family Conversion; originally built as one-family dwelling')], null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='BsmtQual',
            field=models.PositiveIntegerField(choices=[(2, 'Good (90-99 inches)'), (1, 'Fair (70-79 inches)'), (3, 'Typical (80-89 inches)'), (0, 'Excellent (100+ inches)')], null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='CentralAir',
            field=models.PositiveIntegerField(choices=[(0, 'No'), (1, 'Yes')], null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='Electrical',
            field=models.PositiveIntegerField(choices=[(3, 'Mixed'), (0, 'Fuse Box over 60 AMP and all Romex wiring (Average)'), (4, 'Standard Circuit Breakers & Romex'), (2, '60 AMP Fuse Box and mostly knob & tube wiring (poor)'), (1, '60 AMP Fuse Box and mostly Romex wiring (Fair)')], null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='Foundation',
            field=models.PositiveIntegerField(choices=[(1, 'Cinder Block'), (2, 'Poured Contrete'), (3, 'Slab'), (0, 'Brick & Tile'), (5, 'Wood'), (4, 'Stone')], null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='GarageType',
            field=models.PositiveIntegerField(choices=[(2, 'Basement Garage'), (0, 'More than one type of garage'), (3, 'Built-In (Garage part of house - typically has room above garage)'), (4, 'Car Port'), (5, 'Detached from home'), (1, 'Attached to home')], null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='HeatingQC',
            field=models.PositiveIntegerField(choices=[(4, 'Average/Typical'), (2, 'Good'), (1, 'Fair'), (3, 'Poor'), (0, 'Excellent')], null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='HouseStyle',
            field=models.PositiveIntegerField(choices=[(3, 'Two and one-half story: 2nd level finished'), (7, 'Split Level'), (5, 'Two story'), (0, 'One and one-half story: 2nd level finished'), (1, 'One and one-half story: 2nd level unfinished'), (2, 'One story'), (6, 'Split Foyer'), (4, 'Two and one-half story: 2nd level unfinished')], null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='LotShape',
            field=models.PositiveIntegerField(choices=[(0, 'Slightly irregular'), (3, 'Regular'), (1, 'Moderately Irregular'), (2, 'Irregular')], null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='Neighborhood',
            field=models.PositiveIntegerField(choices=[(18, 'South & West of Iowa State University'), (3, 'Brookside'), (19, 'Sawyer'), (11, 'Mitchell'), (14, 'North Ames'), (24, 'Veenker'), (15, 'Northridge'), (5, 'College Creek'), (1, 'Bluestem'), (4, 'Clear Creek'), (6, 'Crawford'), (22, 'Stone Brook'), (13, 'Northpark Villa'), (8, 'Gilbert'), (16, 'Northridge Heights'), (10, 'Meadow Village'), (21, 'Somerset'), (7, 'Edwards'), (0, 'Bloomington Heights'), (23, 'Timberland'), (9, 'Iowa DOT and Rail Road'), (17, 'Old Town'), (2, 'Briardale'), (12, 'Northwest Ames'), (20, 'Sawyer West')], null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='PavedDrive',
            field=models.PositiveIntegerField(choices=[(0, 'Dirt/Gravel'), (1, 'Partial Pavement'), (2, 'Paved ')], null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='RoofMatl',
            field=models.PositiveIntegerField(choices=[(4, 'Roll'), (3, 'Metal'), (1, 'Standard (Composite) Shingle'), (0, 'Clay or Tile'), (6, 'Wood Shakes'), (7, 'Wood Shingles'), (2, 'Membrane'), (5, 'Gravel & Tar')], null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='RoofStyle',
            field=models.PositiveIntegerField(choices=[(2, 'Gabrel (Barn)'), (3, 'Hip'), (4, 'Mansard'), (0, 'Flat'), (1, 'Gable'), (5, 'Shed')], null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='Street',
            field=models.PositiveIntegerField(choices=[(1, 'Paved'), (0, 'Gravel')], null=True),
        ),
        migrations.CreateModel(
            name='PredictionAuthor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
