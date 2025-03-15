from django.contrib import admin

# Register your models here.
from .models import ecom
from .models import call



class callAdmin(admin.ModelAdmin):
    list_display=('fullname','username','email','password')

admin.site.register(ecom,callAdmin)

class callAdmin(admin.ModelAdmin):
    list_display=('name','phno','email','cal')

admin.site.register(call,callAdmin)








