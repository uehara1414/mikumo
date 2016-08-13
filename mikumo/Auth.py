import requests
import datetime


class Auth:
    def __init__(self, account):
        self.account = account
        self.token = ""
        self.jst_expires = None
        self.auth()

    def auth(self):
        pass

    def check_expired(self):
        pass

    def convert_expires_to_localtime(self):
        self.jst_expires = datetime.datetime()