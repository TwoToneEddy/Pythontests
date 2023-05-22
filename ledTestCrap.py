import serial
import time
import random
ser = serial.Serial('/dev/ttyUSB0')  # open serial port
print(ser.name)         # check which port was really used

commands = [1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576]

while(1):
	#row = random.randint(0,5)
	#col = random.randint(0,5)
	for a in commands:
		ser.write(f"{a},100\r\n".encode('utf-8'))   
		time.sleep(0.5)	 
 



ser.close()             # close port
