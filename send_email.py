# Program Developed by AJIMATI IBRAHIM A.K.A Horlalaycon @ github https://github.com/Horlalaycon
"""
        Please Do not use for Illegal Activities.
    This is a program which can be used to spoof and send email
"""


import smtplib
import credentials as cred
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

welcome = """
                    +**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**+
                    |**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**|
                    ||||        E-Mail Spoof / Sender             |||
                    ||||                                          |||
                    ||||    By:                                   |||
                    ||||       IBRAHIM AJIMATI                    |||
                    ||||              Horlalaycon @ github        |||
                    |**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**|
                    +**=**=**=**=**=**=**=**=**=**=**=**=**=**=**=**+
                                        =**=**=**=
                                     =**=**=**=**=**=
"""


class SendMail:
    def __init__(self, smtp_server, smtp_port, server_login_username, server_login_password, file_name, from_address, to_address, subject):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.server_login_username = server_login_username
        self.server_login_password = server_login_password
        self.file_name = file_name
        self.from_address = from_address
        self.to_address = to_address
        self.subject = subject

    def send_message(self):
        server = smtplib.SMTP(host=self.smtp_server, port=self.smtp_port)
        server.starttls()
        server.login(user=self.server_login_username, password=self.server_login_password)
        with open(self.file_name, 'r') as f:
            html_content = f.read()

            msg = MIMEMultipart()
            msg['From'] = self.from_address
            msg['To'] = self.to_address
            msg['Subject'] = self.subject

            html_msg = MIMEText(html_content, 'html')
            msg.attach(html_msg)

            server.sendmail(from_addr=self.server_login_username, to_addrs=self.to_address, msg=msg.as_string())
            server.close()


if __name__ == '__main__':
    try:
        print(welcome)
        from_addr = input('From => fakeaddr@mail.com: ')
        to_addr = input('To => recieveraddr@mail.com: ')
        Subject = input('Subject => Important message: ')

        if from_addr != "" or to_addr != "" or Subject != "":
            send = SendMail(smtp_server=cred.smtp_server,
                            smtp_port=cred.server_port,
                            server_login_username=cred.server_login_username,
                            server_login_password=cred.server_login_password,
                            file_name='message.html',
                            from_address=from_addr,
                            to_address=to_addr,
                            subject=Subject
                            )

            print('')
            print(f"\nSending Mail to {to_addr}...\n")

            send.send_message()

            print(f"+-------------------------------------------+")
            print(f"|           Mail Sent Successfully.         |")
            print(f"+-------------------------------------------+")
        else:
            print('')
            print(f"+----------------------------------------------+")
            print(f"|     Please enter all required information    |")
            print(f"+----------------------------------------------+")

    except EnvironmentError:
        print("")
        print(f"+-------------------------------------------------------+")
        print(f"|       Error! Please Check your Network Connection     |")
        print(f"+-------------------------------------------------------+")
