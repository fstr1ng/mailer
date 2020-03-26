from .mail import Mail

class Stash:
    def __init__(self, config=None, mails=None):
        self.config = config or {}
        self.mails = mails or []

    def create(self, headers):
        mail = Mail(self.config['default_mail'].update(headers))
        self.mails.append(mail)

    def get(self, uuid):
        return filter(lambda mail: mail.uuid == uuid, self.mails)

    def readMailData(self):
        with open(self.path, "r") as data_file:
            self.mail_data = Email(**json.load(data_file))

    def writeMailData(self):
        with open(self.path, "w") as data_file:
            json.dump(asdict(Email), data_file)

    def updateMailData(self, new_data: dict):
        self.current_data = asdict(self.mail_data)
        self.current_data.update(new_data)
        self.mail_data = MailData(**self.current_data)
