from .Account import Account
from .Auth import Auth


class ConoHa:
    def __init__(self, username, password, identity_service, tenantId=None):
        self.account = Account(username, password, identity_service, tenantId)
        self.authinfo = Auth(self.account)
