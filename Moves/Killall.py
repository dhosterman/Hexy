# Move: Killall
import time

for servo in hexy.con.servos:
    hexy.con.servos[servo].kill()
time.sleep(1)
