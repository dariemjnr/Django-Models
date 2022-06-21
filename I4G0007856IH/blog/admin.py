from django.contrib import admin

# Register your models here.
from.models import Title,Text,Author,Dates

admin.site.register(Title)
admin.site.register(Text)
admin.site.register(Author)
admin.site.register(Dates)