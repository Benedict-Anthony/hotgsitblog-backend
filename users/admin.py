from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "is_publisher",)
    list_filter = ("is_publisher", "first_name", "last_name",)
    
    
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("phone",)


admin.site.site_header = "Hot Gist administration"
admin.site.site_title = "Hot gist"


admin.site.register(User, UserAdmin)
