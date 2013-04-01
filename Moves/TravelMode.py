import time

# Move: Point
hexy.neck.set(0)
time.sleep(0.5)

move("Reset")

for angle in range(45, -25, -3):
    for leg in hexy.legs:
        leg.knee(angle)
        leg.ankle(-90+angle)
    time.sleep(0.1)

for leg in hexy.legs:
	leg.knee(-90)
	leg.ankle(90)
	time.sleep(0.2)
time.sleep(1)
