from Stepper import stepper
import _thread
import time
import RPi.GPIO as gpio

# Define a function for the thread
# gpio-p,d,e   board pins
s1=[2,3,4]     #3,5,7
s2=[17,27,22]  #11,13,15
s3=[10,9,11]   #19,21,23
s4=[5,6,13]    #29,31,33
s5=[25,8,7]    #22,24,26
s6=[16,20,21]  #36,38,40

def print_time( threadName, delay,s,steps, dir,speed):
   count = 1
   while count >=1:
      time.sleep(delay)
      count -= 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
      testStepper = stepper(s)
      testStepper.step(steps, dir,speed); 

# Create two threads as follows
try:
    
   _thread.start_new_thread( print_time, ("stepper-1", 0.2, s1,50,"left",1000) )
   _thread.start_new_thread( print_time, ("stepper-2", 0.3, s2,20,"right",500) )
   
   _thread.start_new_thread( print_time, ("stepper-3", 0.4, s3,10,"left",1000) )
   _thread.start_new_thread( print_time, ("stepper-4", 0.5, s4,40,"right",500) )

   _thread.start_new_thread( print_time, ("stepper-5", 0.1, s5,50,"left",1000) )
   _thread.start_new_thread( print_time, ("stepper-6", 0.1, s6,60,"right",500) )
except:
   print ("Error: unable to start thread")

while 1:
   pass