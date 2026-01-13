from django.contrib import admin
#
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'nombres',
        'apellidos',
        'is_active',
        'is_staff',
        'creacion',
    )


admin.site.register(User, UserAdmin)
