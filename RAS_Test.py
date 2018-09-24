import math
import evdev
import _thread
import time

from Stepper import stepper

##from array import*

def print_time(threadName, delay, s, steps, dir, speed):
   count = 1
   while count >=1:
      time.sleep(delay)
      count -= 1
      print ("%s: %s" % ( threadName, time.ctime(time.time())))
      testStepper = stepper(s)
      testStepper.step(steps, dir,speed);
      
#[stepPin, directionPin, enablePin]
s1=[2,3,4]     #3,5,7--Rpi pins
s2=[17,27,22]  #11,13,15
s3=[10,9,11]   #19,21,23

######### Link Lenghts in cm.
l1=42
l2=36
#######Inverse Kinematics Equation for obtaining th joint angles -

######## Coordinates in xy frame in cm
ox = [65,60,55,50,45]
for ix in range(5):
    ##ox[5] = {40 45 50 55 60}
    print(ox[ix])
    x=ox[ix]
    oy = -6
    oz = 0

    oldtheta2=-math.degrees(math.acos((x*x+oy*oy-(l1*l1)-(l2*l2))/ (2*l1*l2)))  
    oldtheta1=math.degrees(math.atan(oy/x) - math.atan((l2*math.sin(oldtheta2*math.pi/180))/(l1 + l2*math.cos(oldtheta2*math.pi/180))))
    oldtheta3=math.degrees(math.acos(oz/(l1*math.cos(oldtheta1*math.pi/180) + l2*math.cos((oldtheta2 + oldtheta1)*math.pi/180))))
    print(" oldtheta1:" + str(oldtheta1)+" oldtheta2:"+ str(oldtheta2)+ " oldtheta3:"+ str(oldtheta3))
    ppr=1600  # Pulse Per Revolution

    nx = x-5 ##{45,50,55,60,65}
    ny = -6
    nz = 0

    theta2=-math.degrees(math.acos((nx*nx+ny*ny-(l1*l1)-(l2*l2))/ (2*l1*l2)))  
    theta1=math.degrees(math.atan(ny/nx) - math.atan((l2*math.sin(theta2*math.pi/180))/(l1 + l2*math.cos(theta2*math.pi/180))))
    theta3=math.degrees(math.acos(nz/(l1*math.cos(theta1*math.pi/180) + l2*math.cos((theta2 + theta1)*math.pi/180))))

    # angles to be moved
    a1=theta3 - oldtheta3 #base
    a2=theta1 - oldtheta1 #link 1
    a3=theta2 - oldtheta2 #link 2
    print(str(theta1)+" theta2:"+str(theta2)+ " theta3:"+str(theta3))
    print(str(a1)+" a2:"+str(a2)+ " a3:"+str(a3))
    ## Gear Ratios
    g1=12.22222222222
    g2=10
    g3=10
    # Calculation for step and Speed
    step1=(ppr/360)*a1*g1  
    step2=(ppr/360)*a2*g2
    step3=(ppr/360)*a3*g3
    # Calculation of timedelay for differnt motors
    execTime=5
    if (step1 == 0):
        td1 = 0
    else :
        td1 = execTime/step1
    if (step2 == 0):
        td2 = 0
    else:
        td2 = execTime/step2
    if (step3 == 0) :
        td3 = 0
    else:
        td3 = execTime/step3
    print(td1)
    print(td2)
    print(td3)

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
    _thread.start_new_thread( print_time, ("stepper-1", 0.2, s1,abs(step1),dir1,td1))
    _thread.start_new_thread( print_time, ("stepper-2", 0.2, s2,abs(step2),dir2,td2))
    _thread.start_new_thread( print_time, ("stepper-3", 0.2, s3,abs(step3),dir3,td3))
    time.sleep(0.2)
