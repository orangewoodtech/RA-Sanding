# Python Code to test the Game Controller
# Before running this code , make sure you have connected the USB of controller & switched ON the controller 
from Stepper import stepper
import evdev 
from evdev import InputDevice, categorize, ecodes
import RPi.GPIO as GPIO

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

for event in controller.read_loop():
	if event.code != 0:
		#print(categorize(event))
		#print(event)
		
		if event.code == 17:
                        if event.value ==-1:
                             print("top button pressed")
                             testStepper1.step(10, "left",1000); #steps, dir, speed, stayOn
