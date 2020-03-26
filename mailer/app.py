from .mail import Mail
from .sender import Sender

def main():
    mail = Mail(mail_to=['m.fedoseev@sprinthost.ru'])
    sender = Sender()
    sender.send(mail)


if __name__ == '__main__':
    main()
