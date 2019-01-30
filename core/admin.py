from django.contrib import admin
from .models import Sala


class SalaAdmin(admin.ModelAdmin):
    list_display = ['nomeSala', 'hash']
    search_fields = (
        'nomeSala','hash'
    )


admin.site.register(Sala, SalaAdmin)
