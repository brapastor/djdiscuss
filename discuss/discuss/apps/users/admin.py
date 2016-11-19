from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class UserAdmin(UserAdmin):
    #Declarar bloques que campos queremos que se muestre en cada bloque
    fieldsets = (
        ('User', {'fields': ('username','password')}),
        ('Personal Info', {'fields': ('first_name',
                                      'last_name',
                                      'email',
                                      'avatar')}),
        ('Permissions', {'fields': ('is_active',
                                    'is_staff',
                                    'is_superuser',
                                    'groups',
                                    'user_permissions')}),
                 )
admin.site.register(User, UserAdmin)

