from grace.arduino.SingletonModel import SingletonModel
from django.db import models


class ArduinoSettings(SingletonModel):
    arduino_account_rfid = models.CharField(max_length=255, default='ACbcad883c9c3e9d9913a715557dddff99')
    arduino_auth_token = models.CharField(max_length=255, default='abd4d45dd57dd79b86dd51df2e2a6cd5')

    class Meta:
        verbose_name = 'Configuração'
        verbose_name_plural = 'Configurações do arduino'
