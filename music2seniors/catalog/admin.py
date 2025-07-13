from django.contrib import admin

# Register your models here.
from .models import performer, senior_home, enquiry

admin.site.register(performer)
admin.site.register(senior_home)
# admin.site.register(enquiry)

@admin.register(enquiry)
class enquiryAdmin(admin.ModelAdmin):
    list_display = ('about','last_name','first_name','email','submitted')