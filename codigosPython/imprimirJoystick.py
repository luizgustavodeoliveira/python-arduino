import time
import serial

arduinoData = serial.Serial('/dev/ttyUSB0', 9600)
time.sleep(1)

while True:
    while (arduinoData.inWaiting() == 0):
        pass
    dataPacket = str(arduinoData.readline(), 'utf-8').strip('\r\n')
    splitPacket = dataPacket.split(",")
    x = int(splitPacket[0])
    y = int(splitPacket[1])
    s = int(splitPacket[2])

    print("X =", x)
    print("Y =", y)
    print("S =", s)
    print("===========")