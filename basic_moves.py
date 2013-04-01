#"""
# Basic moves for Hexy.
#"""

#imports
import time

def moveForward(steps):
	#move forward a number of complete steps
	deg = 25
	midFloor = 30
	hipSwing = 25
	
	for step in range(steps):
		hexy.LF.replantFoot(deg-hipSwing,stepTime=0.5)
		hexy.RM.replantFoot(hipSwing,stepTime=0.5)
		hexy.LB.replantFoot(-deg-hipSwing,stepTime=0.5)

		hexy.RF.setHipDeg(-deg-hipSwing,stepTime=0.5)
		hexy.LM.setHipDeg(hipSwing,stepTime=0.5)
		hexy.RB.setHipDeg(deg-hipSwing,stepTime=0.5)
		time.sleep(0.6)

		hexy.RF.replantFoot(-deg+hipSwing,stepTime=0.5)
		hexy.LM.replantFoot(-hipSwing,stepTime=0.5)
		hexy.RB.replantFoot(deg+hipSwing,stepTime=0.5)

		hexy.LF.setHipDeg(deg+hipSwing,stepTime=0.5)
		hexy.RM.setHipDeg(-hipSwing,stepTime=0.5)
		hexy.LB.setHipDeg(-deg+hipSwing,stepTime=0.5)
		time.sleep(0.6)
		
def moveBackward(steps):
	#move backward a number of complete steps
	deg = 25
	midFloor = 30
	hipSwing = 25
	
	for step in range(steps):
		hexy.LF.replantFoot(deg+hipSwing,stepTime=0.5)
		hexy.RM.replantFoot(-hipSwing,stepTime=0.5)
		hexy.LB.replantFoot(-deg+hipSwing,stepTime=0.5)

		hexy.RF.setHipDeg(-deg+hipSwing,stepTime=0.5)
		hexy.LM.setHipDeg(-hipSwing,stepTime=0.5)
		hexy.RB.setHipDeg(deg+hipSwing,stepTime=0.5)
		time.sleep(0.6)

		hexy.RF.replantFoot(-deg-hipSwing,stepTime=0.5)
		hexy.LM.replantFoot(hipSwing,stepTime=0.5)
		hexy.RB.replantFoot(deg-hipSwing,stepTime=0.5)

		hexy.LF.setHipDeg(deg-hipSwing,stepTime=0.5)
		hexy.RM.setHipDeg(hipSwing,stepTime=0.5)
		hexy.LB.setHipDeg(-deg-hipSwing,stepTime=0.5)
		time.sleep(0.6)
		
def rotateLeft(degrees):
	#rotate left a number of degrees in one or more complete moves
	deg = 40
	moves = int(degrees) // deg
	remainder = int(degrees) % deg
	
	for each in range(moves):	
		for leg in hexy.tripod2:
			leg.replantFoot(deg,stepTime=0.2)
		time.sleep(0.3)

		for leg in hexy.tripod1:
			leg.setFootY(int(floor/2.0))
		time.sleep(0.3)

		for leg in hexy.tripod2:
			leg.setHipDeg(-deg,stepTime=0.3)
		time.sleep(0.3)

		for leg in hexy.tripod1:
			leg.setFootY(floor)
		time.sleep(0.3)

		hexy.LF.replantFoot(deg,stepTime=0.3)
		hexy.RM.replantFoot(1,stepTime=0.3)
		hexy.LB.replantFoot(-deg,stepTime=0.3)
		time.sleep(0.5)
		
	if remainder != 0:	
		for leg in hexy.tripod2:
			leg.replantFoot(remainder,stepTime=0.2)
		time.sleep(0.3)

		for leg in hexy.tripod1:
			leg.setFootY(int(floor/2.0))
		time.sleep(0.3)

		for leg in hexy.tripod2:
			leg.setHipDeg(-remainder,stepTime=0.3)
		time.sleep(0.3)

		for leg in hexy.tripod1:
			leg.setFootY(floor)
		time.sleep(0.3)

		hexy.LF.replantFoot(remainder,stepTime=0.3)
		hexy.RM.replantFoot(1,stepTime=0.3)
		hexy.LB.replantFoot(-remainder,stepTime=0.3)
		time.sleep(0.5)
		
def rotateRight(degrees):
	#rotate right a number of degrees in one or more complete moves
	deg = -40
	moves = int(degrees) // abs(deg)
	remainder = int(degrees) % deg

	for each in range(moves):
		for leg in hexy.tripod1:
			leg.replantFoot(deg,stepTime=0.2)
		time.sleep(0.5)

		for leg in hexy.tripod2:
			leg.setFootY(int(floor/2.0))
		time.sleep(0.3)

		for leg in hexy.tripod1:
			leg.setHipDeg(-deg,stepTime=0.3)
		time.sleep(0.3)

		for leg in hexy.tripod2:
			leg.setFootY(floor)
		time.sleep(0.3)

		hexy.RF.replantFoot(deg,stepTime=0.3)
		hexy.LM.replantFoot(1,stepTime=0.3)
		hexy.RB.replantFoot(-deg,stepTime=0.3)
		time.sleep(0.5)

	if remainder != 0:
		for leg in hexy.tripod1:
			leg.replantFoot(remainder,stepTime=0.2)
		time.sleep(0.5)

		for leg in hexy.tripod2:
			leg.setFootY(int(floor/2.0))
		time.sleep(0.3)

		for leg in hexy.tripod1:
			leg.setHipDeg(-remainder,stepTime=0.3)
		time.sleep(0.3)

		for leg in hexy.tripod2:
			leg.setFootY(floor)
		time.sleep(0.3)

		hexy.RF.replantFoot(remainder,stepTime=0.3)
		hexy.LM.replantFoot(1,stepTime=0.3)
		hexy.RB.replantFoot(-remainder,stepTime=0.3)
		time.sleep(0.5)

def getDistance():
	#return distance
	distance = "CM: 0.00"

	while distance.strip() == "CM: 0.00":
		controller.serialHandler.ser.write("Q")
		distance = controller.serialHandler.ser.readline()
	
	return float(distance.strip()[3:])

def scanDistance(degrees):
	#scan a total number of degrees in front of Hexy and return list of distances
	distances = []
	degree = degrees // 2

	time.sleep(.1)
	hexy.neck.set(degree)
	time.sleep(.3)
	dist = getDistance()
	distances.append((degree, dist))
	time.sleep(.1)

	for each in range(degrees // 10):
		degree = degree - 10
		hexy.neck.set(degree)
		time.sleep(.2)
		dist = getDistance()
		distances.append((degree, dist))
		time.sleep(.1)
		
	print(distances)	
	distances.sort(key=lambda tup: tup[1])
	time.sleep(.5)
	return distances
