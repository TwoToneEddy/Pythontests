import serial
import time
import random
ser = serial.Serial('/dev/ttyUSB0')  # open serial port
print(ser.name)         # check which port was really used


while(1):
	#row = random.randint(0,5)
	#col = random.randint(0,5)
	for row in range(0,5):
		for col in range(0,6):
			print(f"r{row},c{col}\r\n")
			for duty in range(0,11):
				ser.write(f"r{row},c{col},d{duty*10:03d}\r\n".encode('utf-8'))     # write a string
				time.sleep(0.03)			
			for duty in range(10,0,-1):
				ser.write(f"r{row},c{col},d{duty*10:03d}\r\n".encode('utf-8'))     # write a string
				time.sleep(0.03)
ser.close()             # close port
