from .mail import Mail
from .mailer import Mailer

def main():
    email = Mail(mail_to=['m.fedoseev@sprinthost.ru'])
    mailer = Mailer()
    mailer.send(email)


if __name__ == '__main__':
    main()
