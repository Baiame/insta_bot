from instagrapi import Client
import json
import os
from typing import List, Tuple


class Bot:
    _cl = None

    def __init__(self, credential_path = 'src/credentials.json'):
        self._cl = Client()
        if os.path.exists(credential_path):
            log, psw = self.load_credentials(credential_path)
            self._cl.login(log, psw)
            print('OK')
        else:
            print('No creds')
    
    def load_credentials(self, credential_path: str) -> Tuple[str, int]:
        f = open(credential_path)
        cred = json.load(f)
        log = cred['Accounts'][0]['Login']
        psw = cred['Accounts'][0]['Password']
        return log, psw

if __name__ == '__main__':
    bot = Bot()