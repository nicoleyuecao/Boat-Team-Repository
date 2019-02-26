import RPi.GPIO as GPIO

def setupPi():

    GPIO.setmode(GPIO.BCM)  # define use of BCM mode.
    GPIO.setup(17, GPIO.OUT)  # Set pin 17 to be an output.
    pinsetup = GPIO.PWM(17, 50)  # Pin and frequency of PWM.
    if runPi(pinsetup) == "Success":
        print("Sail turned")
    else:
        return "Sail turning failed."


def runPi(pin):

    try:
        print("Attempting to set sail servo")
        pin.start(1)  # Sets the initial position, this will need to be changed to be more accurate.
    except:
        print("Error")
        pin.stop()
        GPIO.cleanup()
        return "Failed"
    
    return "Success"


setupPi()
