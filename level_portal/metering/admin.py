from django.contrib import admin
from .models import Meter
from .models import Data

# Register your models here.
admin.site.register(Meter)
admin.site.register(Data)
