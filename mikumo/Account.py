class Account:
    def __init__(self, username, password, identity_service, tenantId=None):
        self.username = username
        self.password = password
        self.identity_service = identity_service
        self.tenantId = tenantId
