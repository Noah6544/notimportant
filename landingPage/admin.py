from django.contrib import admin
from .models import PotentialUser


class PotentialUserAdmin(admin.ModelAdmin):
    readonly_fields = ['created','email','os','tier']

    list_display = ('email','tier','os', 'created')
    fieldsets = [
        ('User Information', {'fields': ['email', 'os','tier','created']}),
    ]

# Register your models here.
admin.site.register(PotentialUser, PotentialUserAdmin)
