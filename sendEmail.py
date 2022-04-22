import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

GMAIL_USER = 'thiagohmm@gmail.com'
GMAIL_PASSWORD = 'dvgmarilyfuxhkrh'


class enviarMensagens:
    def __init__(self, receiver, msg_email, subject_info):
        self.sender = GMAIL_USER
        self.password = GMAIL_PASSWORD
        self.receiver = receiver
        self.msg_email = msg_email
        self.subject_info = subject_info


    def envMSG(self):

        message = MIMEMultipart()
        message['From'] = self.sender
        message['To'] = self.receiver
        message['Subject'] = self.subject_info

        message.attach(MIMEText(self.msg_email, 'plain'))
        try:


            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(self.sender, self.password)
            text = message.as_string()
            server.sendmail(self.sender, self.receiver, text)
            server.close()
            print ("Email enviado")
        except Exception as err:
            print ('Something went wrong...', err)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    emailObj = enviarMensagens("<tmileo@atech.com.br>", "testando email enviado pelo python ", "Mesagem de teste python 3")
    emailObj.envMSG()


