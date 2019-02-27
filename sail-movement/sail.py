import RPi.GPIO as GPIO

def setupPi():

    GPIO.setmode(GPIO.BOARD)  # define use of BCM mode.
    GPIO.setup(12, GPIO.OUT)  # Set pin 17 to be an output.
    pinsetup = GPIO.PWM(12, 50)  # Pin and frequency of PWM.
    return pinsetup

def runPi(pin):

    try:
        print("Attempting to set sail servo")
        pin.start(1)  # Sets the initial position, this will need to be changed to be more accurate.
        pin.ChangeDutyCycle(7) # 7 is the middle point for the servo, 1 is the start, 12 is the end.
        time.sleep(5) # Sleep until change is made.
    except:
        print("Error")
        return "Failed"
    finally:
        pin.stop()
        GPIO.cleanup()
    
    return "Success"


setup = setupPi()
runPi(setup)
