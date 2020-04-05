
#!/usr/bin/env/python
#Importando blibiotecas
import socket
import subsubprocess
import sys
from datetime import datetime

#Limpando a tela
subprocess.call('clear', shell=True)

#Recendo valore
remoteServer = raw_input("Digite o host para scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

#Banner de scan
print "-" * 60
print "Aguarde! Escaneado o host", rremoteServerIP
print "-" * 60

#Hora que iniciou o scan
t1 = datetime.now()

#Usando o range espeficio de portas(entre 1,1024)
#Capturando erros se necessaio

try:
    for port in range(1,1024):
        sock = socket.socket(socket.AF_INET, socket.SOCK.STREAM)
        result = sock.connect_ex((remoteServerIP,port))
        if result == 0:
            print "Port {}: Open".format(port)
        sock.close

except KeyboardInterrupt:
    print "Voce apertou Ctrl + C"
    sys.exit()

except socket.gaierror:
    print "Hostname não esta comunicando. Saindo..."
    sys.exit()

except socket.erro:
    print "Não foi possivel fazer conexão com o servidor..."
    sys.exit()

#Calculando a diferença de tempo. Para ver quanto tempo demorou para executar o script
total = t2-t1

#Mostrando as informações na tela
print "Scanning completa: ", total
    
