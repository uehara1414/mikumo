import unittest
import json
import mikumo
import datetime


class TestAuth(unittest.TestCase):

    def setUp(self):
        userinfo = json.load(open("auth.json", "r", encoding="utf8"))
        self.username = userinfo.get("username")
        self.password = userinfo.get("password")
        self.tenantId = userinfo.get("tenantId")
        self.identity_service = userinfo.get("identity_service")

    def test_auth_0(self):
        conoha = mikumo.ConoHa(self.username, self.password, self.identity_service, self.tenantId)
        token = conoha.authinfo.token
        self.assertEqual(type(token), str)
        self.assertGreater(len(token), 10)

    def test_auth_1(self):
        conoha = mikumo.ConoHa(self.username, self.password, self.identity_service)
        token = conoha.authinfo.token
        self.assertEqual(type(token), str)
        self.assertGreater(len(token), 10)

    def test_auth_2(self):
        conoha = mikumo.ConoHa(self.username, self.password, self.identity_service)
        self.assertEqual(type(conoha.authinfo.expires), datetime.datetime)
