import socket
import time
from datetime import datetime
from ping3 import ping, verbose_ping
import sendEmail
import csvClass

class CheckServer:
    def __init__(self, servidor):
        self.servidor = servidor



    @property
    def connectionTCPSocket(self):
         a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         return a_socket

    def checkServer(self, port=80):

        csvServer =[]
        csvServer.append(str(datetime.today()))
        csvServer.append(str(self.servidor))
        mensagem = "Ocorreu um erro as " + str(datetime.today()) + " no IP/dominio " + self.servidor

        try:
            _sock = self.connectionTCPSocket
            location = (self.servidor, port)
            result_of_check = _sock.connect_ex(location)

            #TODO implementar gravcao de csv
            print("#############################################")
            if result_of_check == 0:
                print("Dominio/IP ", self.servidor +" UP")
                csvServer.append('UP')
            else:
                print("Dominio/IP ", self.servidor +" DOWN")
                csvServer.append('Down')
                mail = sendEmail.enviarMensagens("<tmileo@atech.com.br>", mensagem, "Erro no Servidor")
                mail.envMSG()

        except:
            #TODO Mandar email

            mail = sendEmail.enviarMensagens("<tmileo@atech.com.br>",mensagem, "Erro no Servidor")
            mail.envMSG()
            print (mensagem)
            _sock.close()

            csvServer.append('Error')
        return csvServer



    def scanhost(self, port):

        csvport = []
        csvport.append(str(datetime.today()))
        csvport.append(self.servidor)
        csvport.append(port)

        try:
            _sock = self.connectionTCPSocket
            location = (self.servidor, int(port.strip()))
            result_of_check = _sock.connect_ex(location)

            # TODO implementar gravcao de csv
            if result_of_check == 0:
                print("Dominio/IP ", self.servidor + " Porta", port + " OK ")
                csvport.append('OPEN')
            else:
                print("Dominio/IP ", self.servidor +" Porta", port +  " NOK")
                csvport.append('CLOSE')



        except:
            # TODO Mandar email
            mensagem = "Ocorreu um erro as " + str(datetime.today()) + " no IP/dominio " + self.servidor + " scan Port"
            print(mensagem)
            _sock.close()
            csvport.append('ERROR')

        return csvport






    def checkPort(self, ports):
        statusPort=[]
        if (isinstance(ports, int)) :


           statusPort.append(self.scanhost(ports))

        else:
            for port in ports.split(","):
                if not("-" in str(port)):
                        statusPort.append(self.scanhost(port))

                elif ("-" in str(port)):

                    iniport= int(port.split("-")[0])
                    finalport = int(port.split("-")[1])
                    while iniport <= finalport:

                        statusPort.append(self.scanhost(str(iniport)))
                        iniport = iniport + 1

        return statusPort


    def testar_com_ping(self, tempo=2, qtd=1):
        csvping = []
        csvping.append(str(datetime.today()))
        csvping.append(self.servidor)

        for i in range(qtd):
            resultado = ping(self.servidor, unit='ms')
            csvping.append(resultado)
            if resultado == False:
                mensagem = "Ocorreu um erro as perca de ping " + str(datetime.today()) + " no IP/dominio " + self.servidor
                print (mensagem)
                mail = sendEmail.enviarMensagens("<tmileo@atech.com.br>", mensagem, "Perca de ping no servidor")
                mail.envMSG()


            else:
                time.sleep(tempo)
                print ("Dominio/IP ", self.servidor + " " , str(resultado) + " ms")
        return csvping


if __name__ == '__main__':
    ServerHeader= ['Data', 'Server','Status']
    PortHeader = ['Data', 'Server', 'port','Status']
    PingHeader =  ['Data', 'Server', 'Ping ms']
    csvServerobj = csvClass.csvServer('Status_Server.csv', ServerHeader)
    csvportobj = csvClass.csvServer('Status_Port.csv', PortHeader)
    csvpingobj = csvClass.csvServer('Status_Ping.csv', PingHeader)

    dominios = ['google.com', 'atech.com.br', '10.103.3.105']
    for i in dominios:
        obj = CheckServer(i)
        #print (obj.checkServer())
        csvServerobj.wrintingCSVServer(obj.checkServer())
        csvportobj.wrintingCSVPort(obj.checkPort("80,22,443-445"))
        csvpingobj.wrintingCSVServer(obj.testar_com_ping(1,5))
       # print (obj.testar_com_ping(1, 5))






