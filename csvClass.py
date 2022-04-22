import csv


class csvServer:

    def __init__(self, nome, header):
        self.nome = nome
        self.header = header



    def wrintingCSVServer(self, linhas):

        list_row = []
        list_row.append(linhas)

        with open(self.nome, 'a') as file:
           write = csv.writer(file)
           write.writerow(self.header)
           write.writerows(list_row)



    def wrintingCSVPort(self, linhas):


        with open(self.nome, 'a') as file:
           write = csv.writer(file)
           write.writerow(self.header)
           write.writerows(linhas)



