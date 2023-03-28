from django.contrib import admin
from . models import Hero, Topic, Download, Social, Contact
# Register your models here.



@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'badge_1', 'badge_2']

admin.site.register(Topic)
admin.site.register(Download)
admin.site.register(Social)
admin.site.register(Contact)



