from django.contrib import admin
from users.models import Account
from django.contrib.auth.admin import UserAdmin
# Register your models here.
#admin.site.register(Account)

class AccountAdmin(UserAdmin):
    list_display = ('email','username','first_name','last_login','is_active','is_admin','is_staff')
    search_fields = ('email','username')
    readonly_fields = ('last_login',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account,AccountAdmin)