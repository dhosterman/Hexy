hexy
====

Modifications to Hexy the Hexapod (http://arcbotics.com/products/hexy/) control files

##What is it?

This is a re-write of the excellent software that came with Hexy. My goals are to strip out the GUI interface and allow
command-line interaction with tools to make it easy to control Hexy via a Raspberry Pi brain. Also, I eventually want to
implement memory and personality modules for Hexy.

##What have I done so far?
    * Strip out the GUI interface
    * Implement a basic command line interface
    * Create some basic natural speech functionality for the CLI
    * Allow for manual activation of the ultrasound sensor
    * Create some more precise basic movement controls (degrees of rotation, distance of movement)
    * Implement a basic memory for Hexy that records the times and durations of interactions
    
##How do I use this code?

You'll need to flash the new Arduino code to Hexy's Servotor in order to manually activate the ultrasound sensor.
This step isn't necessary if you don't want to use that functionality.
Otherwise, just download and run hexy.py and everything should work out fine assuming you could get the original
software to work. (Note: You will need an offsets.cfg file if you want to use offsets.)

When interacting with Hexy, try typing naturally and asking him to perform moves in the Moves folder. Hexy should
respond correctly regardless of the syntax as long as the move name is in the request. For example:

*Me: get up*

Is the same as:

*me: Hexy, please get up.*
