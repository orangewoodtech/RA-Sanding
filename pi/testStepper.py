from Stepper import stepper



testStepper = stepper([2, 3, 4])  #[stepPin, directionPin, enablePin]
testStepper.step(360*19*4, "left",0.0005); #steps, dir, speed, stayOn


