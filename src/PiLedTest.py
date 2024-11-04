import time
from hal import hal_input_switch as switch
from hal import hal_led as led

def main():
    # Initialize the switch and LED
    switch.init()
    led.init()
    
    while True:
        if switch.read_slide_switch():  # Switch is active (left position)
            # Blink LED at 5 Hz
            led.set_output(0, 1)  
            time.sleep(0.1)       
            led.set_output(0, 0)  
            time.sleep(0.1)       
        else:
            # Blink LED at 10 Hz for 5 seconds when the switch is in the right position
            start_time = time.time()
            while time.time() - start_time < 5:
                led.set_output(0, 1)  
                time.sleep(0.05)      
                led.set_output(0, 0)  
                time.sleep(0.05)      
                           # Turn off the LED after 5 seconds
            led.set_output(0, 0)
            # Wait a moment to avoid constantly retriggering the 5-second timer
            time.sleep(0.1)

if __name__ == "__main__":
    main()
