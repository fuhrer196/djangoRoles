from django.contrib import admin
# Register your models here.
from .models import *
#from .models import setup
#from .models import roleAdd

#admin.site.register(role)
#admin.site.register(roleAdd)

##class roleInLine(admin.StackedInline):
##    model = role
##    extra = 1
##class setupAdmin(admin.ModelAdmin):
##    inlines = [roleInLine]
admin.site.register(setup)
