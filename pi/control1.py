# Python Code to test the Game Controller
# Before running this code , make sure you have connected the USB of controller & switched ON the controller 
import _thread
import time
import evdev 
from evdev import InputDevice, categorize, ecodes
import RPi.GPIO as GPIO
from Stepper import stepper

s1=[2,3,4]     #3,5,7
s2=[17,27,22]  #11,13,15
s3=[10,9,11]   #19,21,23
s4=[5,6,13]    #29,31,33
s5=[25,8,7]    #22,24,26
s6=[16,20,21]  #36,38,40

testStepper1 = stepper(s1)
testStepper2 = stepper(s2)
testStepper3 = stepper(s3)
testStepper4 = stepper(s4)
testStepper5 = stepper(s5)
testStepper6 = stepper(s6)


devices_list = evdev.list_devices() # This would give us the list of devices 
index = 0

"""
InputDevice gives the device type which has following properties :
1.name
2.capbilities
3.phys


Event has following properties mainly : 
1.Code
2.type 
3.Value



"""



for device in devices_list:
	if evdev.InputDevice(device).name == "Microsoft X-Box 360 pad":
		print("Index where the Controller is found is : " + str(index))
		break
	else:
		index = index + 1

controller =evdev.InputDevice(devices_list[index])
#print(controller.name)

def print_time( threadName, delay,s,steps, dir,speed):
   count = 1
   while count>0:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
      testStepper = stepper(s)
      testStepper.step(steps, dir,speed);

    for event in controller.read_loop():
            if event.code != 0:
                    #print(categorize(event))
                    #print(event)
                try:
                    if event.code == 310:
                        if event.value == 1:
                            print("button pressed")
                            testStepper5.step(10, "left",1000); #steps, dir, speed, stayOn
                            
                    #_thread.start_new_thread( print_time, ("stepper-1", 0.1, s1,10,"left",1000) )
                   
                   #_thread.start_new_thread( print_time, ("stepper-2", 0.2, s2,20,"right",500) )
               
                   #_thread.start_new_thread( print_time, ("stepper-3", 0.3, s3,10,"left",1000) )
                   #_thread.start_new_thread( print_time, ("stepper-4", 0.4, s4,40,"right",500) )

                   #_thread.start_new_thread( print_time, ("stepper-5", 0.5, s5,50,"left",1000) )
                   #_thread.start_new_thread( print_time, ("stepper-6", 0.6, s6,60,"right",500) )
                except:
                   print ("Error: unable to start thread")

                while 1:
                   pass
            
	