from django.contrib import admin

# Register your models here.
from .models import BasicEnquiryForm

class FormAdmin(admin.ModelAdmin):
     list_display = ('student_fname','student_lname', 'contact_no_primary', 'ssc_percent','ssc_science', 'ssc_maths' )
	
admin.site.register(BasicEnquiryForm, FormAdmin)