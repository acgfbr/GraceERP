from django.contrib import admin
from grace.arduino.models import ArduinoSettings


class ArduinoModelAdmin(admin.ModelAdmin):
    list_display = ('arduino_account_rfid', 'arduino_auth_token')

admin.site.register(ArduinoSettings, ArduinoModelAdmin)

