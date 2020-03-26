class SaveLoader:
    def __init__(self):
        pass

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
