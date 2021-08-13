from django.contrib import admin

# Register your models here.

from accounts.models import UserAccount

# Register your models to admin site, then you can add, edit, delete and search your models in Django admin site.

class UserAdmin(admin.ModelAdmin):
    # list_display = ("id","first_name", "last_name",)
    search_fields = ['email' ]

admin.site.register(UserAccount, UserAdmin)
