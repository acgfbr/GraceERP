from grace.arduino.models import ArduinoSettings


def settings(request):
    return {'settings': ArduinoSettings.load()}