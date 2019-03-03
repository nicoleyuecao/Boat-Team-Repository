# Sail Movement

![sailingImage](https://github.com/potato-chip-studios/Boat-Team-Repository/blob/master/sail-movement/SailServo.png)

Uses the RIP.GPIO and time libraries.

setupPi sets up the GPIO in the board configuration, this is done by setting the initial frequency and setting the pin to be an output.

setSail uses an angle conversion formula to interpret a standard angle into a pwm duty change cycle usable figure, the diagram above explains the general positioning of the sail based on the input. Input for the function is the angle and the pin configuration. The servo direction is changed in the changedutycycle sections with a short sleep placed afterwards to ensure the servo has finished moving the servo. Finally the gpio configuration is reset to ensure the pin is ready for any further input and to save power.

The runner is placed at the bottom of the script with the capability to allow spontaneous changes either manually or by passing in an appropriate angle based on feed back from other navigational analysis. A controlling function will determine the flow of this python script.
