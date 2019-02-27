#Adrian and Gareth

import RPi.GPIO as GPIO
import time

def setupPi():

    GPIO.setmode(GPIO.BOARD)  # define use of BCM mode.
    GPIO.setup(12, GPIO.OUT)  # Set pin 17 to be an output.
    pinsetup = GPIO.PWM(12, 50)  # Pin and frequency of PWM.
    return pinsetup

def runPi(pin, angle):
    
    dutyChange = int(angle/18) + 1

    try:
        print("Attempting to set sail servo")
        pin.start(0)  # Sets the initial position.
        pin.ChangeDutyCycle(dutyChange) # 7 is the middle point for the servo, 1 is the start, 12 is the end.
        time.sleep(5) # Sleep until change is made.
    except:
        print("Error")
        return "Failed"
    finally:
        pin.stop()
        GPIO.cleanup()
    
    return "Success"


setup = setupPi() 
runner = true

sailAngle = int(input("Please enter the angle you would like the sail and then press enter: ")) #90 degrees as the angle is central starting location.

"""
while runner:
    sailAngle = int(input("Please enter the angle you would like the sail and then press enter: ")) # 90 degrees as the angle is currently central starting location.
    if sailAngle == "q" or sailAngle == "Q":
        runner = false
"""    
runPi(setup, sailAngle)
