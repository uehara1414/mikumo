import requests
import datetime


class Auth:
    def __init__(self, account):
        self.account = account
        self.token = ""
        self.expires = None
        self.auth()

    def auth(self):
        data = {
            "auth": {
                "passwordCredentials": {
                    "username": self.account.username,
                    "password": self.account.password
                },
                "tenantId": self.account.tenantId
            }
        }
        r = requests.post(self.account.identity_service, data=data)
        print(r)

    def check_expired(self):
        pass

    def convert_expires_to_localtime(self):
        self.expires = datetime.datetime()
