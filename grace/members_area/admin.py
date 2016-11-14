from django.contrib import admin
from django.utils.timezone import now

from grace.members_area.models import Registration


class RegistrationModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'name', 'cpf', 'phone', 'email', 'created_at', 'registred_today')
    date_hierarchy = 'created_at'
    search_fields = ('username', 'name', 'email', 'phone', 'cpf', 'created_at')
    list_filter = ('created_at',)

    def registred_today(self, obj):
        return obj.created_at == now().date()

    registred_today.short_description = 'Registrou hoje?'
    registred_today.boolean = True


admin.site.register(Registration, RegistrationModelAdmin)