from django.contrib import admin

# Register your models here.
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','username','listing','fname','lname','email','contact_date','message')
    list_display_links = ('id','username','listing','fname','lname','email','contact_date','message')
    list_per_page=25

admin.site.register(Contact,ContactAdmin)