################################################################################
# main.py: GPIO implementation using threads.
################################################################################
import threading        # Contains the thread class.
import RPi.GPIO as GPIO # Python GPIO library.
GPIO.setwarnings(False) # Disabling unnecessary warnings.
GPIO.setmode(GPIO.BCM)  # Using BCM pin numbers.

def leds_init(leds):
   """
   leds_init: Setting data direction of pins connected to leds to output.

              - leds: List containing pin numbers for leds.
   """
   for i in leds:
      GPIO.setup(i, GPIO.OUT) 
   return

def leds_blink(leds, blink_speed_ms):
   """
   leds_blinks: Genererates continuous blinking of leds in a sequence 
                with specified blink_speed.

                - leds          : List containing pin number for the leds.
                - blink_speed_ms: Blink speed in milliseconds.
   """
   import time 
   while True:
      for i in leds:
         GPIO.output(i, 1)
         time.sleep(blink_speed_ms / 1000.0) 
         GPIO.output(i, 0) 
   return

def main():
   """
   main: Stores pin numbers for leds 17, 22, 23 and 24 in two lists. 
         The pins are set to output by calling the leds_init function.
         Two threads are implemented to blink the leds simultaneously
         with different blink speeds. For both threads the leds_blinks 
         function is therefore used as target.

   """

   # Storing pin numbers for leds in two lists:
   l1 = [ 17, 22 ]
   l2 = [ 23, 24 ]

   # Setting pins to output:
   leds_init(l1)
   leds_init(l2)

   # Creating threads, setting target function to leds_blink and the lists and blink speeds as arguments:
   t1 = threading.Thread(target = leds_blink, args = (l1, 50))
   t2 = threading.Thread(target = leds_blink, args = (l2, 250)) 

   # Starting threads:
   t1.start()
   t2.start()

   # Synchronizing threads:
   t1.join()
   t2.join()

   return

# If this is the startup script, the main function is called to start the program:
if __name__ == "__main__":
   main()