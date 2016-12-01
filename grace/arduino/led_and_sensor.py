from flask import Flask, render_template, request, redirect, url_for
from pyarduino import *
import time

app = Flask(__name__)

"""
initialize connection to Arduino
if your arduino was running on a serial port other than '/dev/ttyACM0/'
declare: a = Arduino(serial_port='/dev/ttyXXXX')
"""

ardObj = Arduino()
time.sleep(3)

# declare the pins we're using
YELLOW_LED_PIN = 2
YELLOW_LED_PIN2 = 3
ANALOG_PIN = 0

# initialize the digital pin as output
ardObj.set_pin_mode(YELLOW_LED_PIN, 'O')
ardObj.set_pin_mode(YELLOW_LED_PIN2, 'O')

print('Arduino initialized')


@app.route('/', methods=['POST', 'GET'])
def ZuckYbergson():
    # variables for template page (templates/index.html)
    author = "EliteDev"

    # if we make a post request on the webpage aka press button then do stuff
    if request.method == 'POST':

        # if we press the turn on button
        if request.form['yellow'] == 'Turn On Yellow':
            print('TURN ON YELLOW')

            # turn on LED on arduino
            ardObj.digital_write(YELLOW_LED_PIN, 1)
            ardObj.digital_write(YELLOW_LED_PIN2, 1)

        # if we press the turn off button
        elif request.form['yellow'] == 'Turn Off Yellow':
            print('TURN OFF YELLOW')

            # turn off LED on arduino
            ardObj.digital_write(YELLOW_LED_PIN, 0)
            ardObj.digital_write(YELLOW_LED_PIN2, 0)

        else:
            pass

    # read in analog value from photoresistor
    readval = ardObj.analog_read(ANALOG_PIN)

    # the default page to display will be our template with our template variables
    return render_template('index.html', author=author, value=100 * (readval / 1023.))


if __name__ == "__main__":
    # lets launch our webpage!
    # do 0.0.0.0 so that we can log into this webpage
    # using another computer on the same network later
    app.run(host='0.0.0.0')
