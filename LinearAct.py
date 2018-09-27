import math
import evdev
import _thread
import time

from Stepper import stepper

def print_time(threadName, delay, s, steps, dir, speed):
   count = 1
   while count >=1:
      time.sleep(delay)
      count -= 1
      print ("%s: %s" % ( threadName, time.ctime(time.time())))
      testStepper = stepper(s)
      testStepper.step(steps, dir,speed);

s1=[26,19,13]
_thread.start_new_thread( print_time, ("stepper-LA", 0.2, s1,abs(200),"l",100))