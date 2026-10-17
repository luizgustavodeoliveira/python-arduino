import time
import serial

arduinoData = serial.Serial('/dev/ttyUSB0', 9600) #Porta, BAUD
time.sleep(1) #Aguarda 1 segundo para a porta carregar

while True: #Cria um loop infinito
    while (arduinoData.inWaiting()==0): #Verifica se há dados sendo recebidos
        pass #Se não, espera e verifica novamente
    dataPacket = str(arduinoData.readline(), 'utf-8').strip('\r\n') #Pacote de dados com os valores passados pelo Arduino
    print(dataPacket)