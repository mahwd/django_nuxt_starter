from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):
    list_display = ("email", "username", "date_joined", "last_login", "is_admin", "is_staff")
    search_fields = ("email", "username")
    readonly_fields = ("date_joined", "last_login")
    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_active', 'is_staff', 'is_superuser',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_admin', 'is_active', 'is_staff', 'is_superuser',)}
         ),
    )


admin.site.register(Account, AccountAdmin)
