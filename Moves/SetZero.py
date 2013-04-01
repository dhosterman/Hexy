# Move: Set Zero
import time

for servo in hexy.con.servos:
    hexy.con.servos[servo].setPos(deg=0)
time.sleep(1)
