#Move: FindClosest

import time

def getDistance():
    distance = "CM: 0.00"

    while distance.strip() == "CM: 0.00":
        controller.serialHandler.ser.write("Q")
        distance = controller.serialHandler.ser.readline()
    
    return float(distance.strip()[3:])
    
def rotate(deg):
    
    #re-plant tripod2 deg degrees forward
    for leg in hexy.tripod2:
        leg.replantFoot(deg,stepTime=0.2)
    time.sleep(0.3)

    #raise tripod1 feet
    for leg in hexy.tripod1:
        leg.setFootY(int(floor/2.0))
    time.sleep(0.3)

    #swing tripod2 feet back 2*deg degrees (to -deg)
    for leg in hexy.tripod2:
        leg.setHipDeg(-deg,stepTime=0.3)

    #reset neck as body turns
    hexy.neck.set(0)
    time.sleep(0.4)

    #lower tripod1 feet
    for leg in hexy.tripod1:
        leg.setFootY(floor)
    time.sleep(0.3)

    #re-plant legs to starting position
    hexy.LF.replantFoot(deg,stepTime=0.3)
    hexy.RM.replantFoot(1,stepTime=0.3)
    hexy.LB.replantFoot(-deg,stepTime=0.3)

    time.sleep(0.5)

distances = []
degree = 80

time.sleep(.1)
hexy.neck.set(degree)
time.sleep(.2)
dist = getDistance()
#print(dist)
distances.append((degree, dist))
time.sleep(.1)

for each in range(degree /10 * 2):
    degree = degree - 10
    hexy.neck.set(degree)
    time.sleep(.1)
    dist = getDistance()
    #print(dist)
    distances.append((degree, dist))
    time.sleep(.1)
    
#print distances
distances.sort(key=lambda tup: tup[1])
#print(distances)
#print(distances[0][0])
hexy.neck.set(distances[0][0])
time.sleep(.5)
rotate(distances[0][0])
time.sleep(.5)
move("Kill")
for each in range(int(distances[0][1] / 10)):
    print each
    #move("Move Forward")
move("Move Forward")