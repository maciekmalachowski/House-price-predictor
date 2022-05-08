from django.contrib import admin
from .models import Data

class DataAdmin(admin.ModelAdmin):
    list_display = ('BldgType', 'SalePrice')

admin.site.register(Data, DataAdmin)