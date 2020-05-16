from .mail import Mail
from .sender import Sender
from .stash import Stash

import json
import pdb

def main():

    with open('config.json') as f:
        config = json.load(f)
    print(config)

    stash = Stash(config=config)

    stash.create({
        'mail_to': 'mailbox@domain.com',
        'text': 'Hello!'
    })
    print(stash.mails)
    sender = Sender(config=config)
    #print(f'MTA return code: {sender.send(mail)}')

if __name__ == '__main__':
    main()
