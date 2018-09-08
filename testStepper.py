import math
import evdev
import _thread
import time

from Stepper import stepper

def print_time(threadName, delay,s,steps, dir,speed):
   count = 1
   while count >=1:
      time.sleep(delay)
      count -= 1
      #print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
      testStepper = stepper(s)
      testStepper.step(steps, dir,speed);
      
#[stepPin, directionPin, enablePin]
s1=[2,3,4]     #3,5,7--Rpi pins
s2=[17,27,22]  #11,13,15
s3=[10,9,11]   #19,21,23

######### Link Lenghts in cm.
l1=42
l2=36
######## Coordinates in xy frame in cm

x=10
y=62

#######Inverse Kinematics Equation for obtaining th joint angles -

theta3=math.degrees(math.acos((x*x+y*y-(l1*l1)-(l2*l2))/(2*l1*l2)))
theta2=math.degrees(math.atan((y*(l1+l2*math.cos(theta3))-(x*l2*math.sin(theta3)))/(x*(l1+l2*math.cos(theta3))+(y*l2*math.sin(theta3)))))
theta1=math.degrees(math.atan(y/x))

print(str(theta1)+" "+str(theta2)+ " "+str(theta3))

## Creation of objects for various motors
testStepper1 = stepper(s1)
testStepper2 = stepper(s2)
testStepper3 = stepper(s3)

ppr=1600  # Pulse Per Revolution

# angles to be moved
a1=theta1  #base
a2=theta2  #link 1
a3=theta3  #link 2

##a1=30  #base
##a2=40  #link 1
##a3=30  #link 2

## Gear Ratios
g1=12.2
g2=10
g3=10

# Calculation for step and Speed
step1=(ppr/360)*a1*g1  
#speed1=0.01

step2=(ppr/360)*a2*g2
#speed2=0.01

step3=(ppr/360)*a3*g3  
#speed3=0.01

# Calculation of timedelay for differnt motors
execTime=10

td1=abs((execTime-(step1*0.002))/step1)
td2=abs((execTime-(step2*0.002))/step2)
td3=abs((execTime-(step3*0.002))/step3)

#print(td1)
#print(td2)
#print(td3)


#testStepper1.step(step1, "l",td1); #steps, dir, speed, stayOn  BASE--[left==ccw; right= cw]
#testStepper2.step(step1, "l",td2); #steps, dir, speed, stayOn Link 1--[Left==forward; Right= backward]
#testStepper3.step(angle3, "right",speed3); #steps, dir, speed, stayOn  Link 2--[left==downward; right= upward]
if step1<0:
    dir1="r"
else:
    dir1="l"
    
if step2<0:
    dir2="l"
else:
    dir2="r"

if step3<0:
    dir3="l"
else:
    dir3="r"

_thread.start_new_thread( print_time, ("stepper-1", 0.2, s1,abs(step1),"l",td1))
_thread.start_new_thread( print_time, ("stepper-2", 0.2, s2,abs(step2),"l",td2))
_thread.start_new_thread( print_time, ("stepper-3", 0.2, s3,abs(step3),"r",td3))