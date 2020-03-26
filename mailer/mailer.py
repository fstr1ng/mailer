import subprocess

class Mailer:
    def __init__(self, emails=None):
        self.emails = emails or []

    def send(self, email) -> int:
        print(str(email))
        proc = subprocess.run(["exim", "-i", "-t"], text=True, input=str(email))
        return proc.returncode
