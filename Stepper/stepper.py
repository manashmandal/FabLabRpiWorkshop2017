import sys
import time
import RPi.GPIO as GPIO


class StepperMotor(object):

    SEQUENCE = [[1,0,0,1],
       [1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1]]

    
    def __init__(self, pins):
        # Assign pins
        self.pins = pins
        
        # Current step sequence
        self.current_step = 0

        # Default Step direction
        self.step_dir = 1

        # Use BCM GPIO references
        GPIO.setmode(GPIO.BCM)

        # Setup the pin
        for pin in self.pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, False)

        # Max step sequence count
        self.max_step_sequence = len(StepperMotor.SEQUENCE)

        # Default delay
        self.step_delay = 5

        # Pincount
        self.pin_count = len(self.pins)

    
    # Sets step direction. +1, +2 and -1, -2
    def set_direction(self, dir):
        self.step_dir = dir

    # Step delay
    def set_step_delay(self, delay_time):
        self.step_delay = delay_time

    # Set step direction before calling this function
    def step(self, step_count):
        # Perform number of steps
        for i in range(step_count):
            for pin in range(0, self.pin_count):
                # Get Motor GPIO
                _pin = self.pins[pin]

                if StepperMotor.SEQUENCE[self.current_step][_pin] != 0:
                    GPIO.output(_pin, True)
                else:
                    GPIO.output(_pin, False)
            
            self.current_step += self.step_dir

            if self.current_step >= self.step_count:
                self.current_step = 0
            else:
                self.current_step = self.current_step + self.step_dir

            time.sleep(self.step_delay) 
