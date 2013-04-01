distance = "CM: 0.00"

while distance.strip() == "CM: 0.00":
	controller.serialHandler.ser.write("Q")
	distance = controller.serialHandler.ser.readline()
	
print distance.strip()
