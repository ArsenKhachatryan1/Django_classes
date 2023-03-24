from django.contrib import admin
from .models import Sitename, Portfolio, Story, Contact

# Register your models here.


admin.site.register(Sitename)
admin.site.register(Portfolio)
admin.site.register(Story)
admin.site.register(Contact)