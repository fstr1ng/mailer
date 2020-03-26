import subprocess
import shlex


class Sender:
    def __init__(self, config=None):
        self.config = config or {}

    def send(self, email) -> int:
        subcommands = shlex.split(self.config['sendmail_path'])
        proc = subprocess.run(subcommands, text=True, input=str(email))
        return proc.returncode
