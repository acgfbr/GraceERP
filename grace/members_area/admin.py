from django.contrib import admin
from django.utils.timezone import now

from grace.members_area.models import Registration


class RegistrationModelAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'name', 'cpf', 'phone', 'email', 'created_at', 'registred_today', 'paid')
    date_hierarchy = 'created_at'
    search_fields = ('username', 'name', 'email', 'phone', 'cpf', 'created_at')
    list_filter = ('paid', 'created_at')
    actions = ['mark_as_paid']

    def registred_today(self, obj):
        return obj.created_at == now().date()

    registred_today.short_description = 'Registrou hoje?'
    registred_today.boolean = True

    def mark_as_paid(self, request, queryset):
        count = queryset.update(paid=True)

        if count == 1:
            msg = '{} registro foi marcado como pago.'
        else:
            msg = '{} registros foram marcados como pagos.'


        self.message_user(request, msg.format(count))

    mark_as_paid.short_description = 'Marcar como pago'

admin.site.register(Registration, RegistrationModelAdmin)