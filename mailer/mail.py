from getpass import getuser
from socket import gethostname
from mimetypes import guess_type

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.audio import MIMEAudio
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase

from email.utils import formatdate
from email import encoders

from dataclasses import dataclass, field
from typing import List

known_types = {
    'text': MIMEText,
    'audio': MIMEAudio,
    'image': MIMEImage,
    'application': MIMEApplication,
}

def create_attachment(path):
    ctype, encoding = guess_type(path)
    if ctype is None or encoding is not None:
        ctype = 'application/octet-stream'
    maintype, subtype = ctype.split('/', 1)
    print(ctype, encoding)
    with open(path) as f:
        if maintype in known_types:
            msg = known_types[maintype](f.read(), _subtype=subtype)
        else:
            msg = MIMEBase(maintype, subtype)
            msg.set_payload(f.read())
            encoders.encode_base64(msg)
    msg.add_header('Content-Disposition', 'attachment', filename=path)
    print(msg)


@dataclass
class Mail:
    subject: str = "Mail subject"
    text: str = "Mail text"
    html: str = None
    mail_from: str = f"{getuser()}@{gethostname()}"
    mail_to: List[int] = field(default_factory=list)
    attachments: List[str] = field(default_factory=list)

    def __str__(self):
        email = MIMEMultipart()
        email["Subject"] = self.subject
        email["From"] = self.mail_from
        email["To"] = ", ".join(self.mail_to)
        email["Date"] = formatdate(localtime=True)

        if self.text:
            email.attach(MIMEText(self.text, 'plain'))
        if self.html:
            email.attach(MIMEText(self.html, 'html'))

        for f in self.attachments:
            part = create_attachment(f)
            email.attach(part)

        return email.as_string()
