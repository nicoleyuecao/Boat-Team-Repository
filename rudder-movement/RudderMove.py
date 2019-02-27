#Andrew/Hardeep

import RPi.GPIO as GPIO

#straight -> 100Hz
#starboard, soft -> 75Hz
#starboard, hard -> 50Hz
#port, soft -> 125Hz
#port, hard -> 150Hz

def setupPi(frequency):
    GPIO.setmode(GPIO.BOARD) #uses board pins
    GPIO.setup(12, GPIO.OUT) #sets pin 18 as the output (rudder motor)
    pinsetup = GPIO.PWM(12,frequency)#rudder is set to straight
    pin.start(1) #sets initial position of rudder
    return pinsetup

def runPi(pin):
    try:
        print("Attempting to set rudder servo")
        GPIO.output(12,1) #sends a HIGH signal to pin 12
    except:
        print("Error")
        return "Failed"

    finally:
        pin.stop()
        GPIO.cleanup()
    return "Success"

def main():
    Angle.lower() #allows for input    
    if Angle == "starboard soft":
        frequency = 75
    elif Angle == "starboard hard":
        frequency = 50
    elif Angle == "port soft":
        frequency = 125
    elif Angle == "port hard":
        frequency = 150
    else:
        frequency = 100
        
    setup = setupPi(frequency)
    runPi(setup)
