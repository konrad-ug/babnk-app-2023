import requests
import unittest

class TestAccountCrud(unittest.TestCase):
    
    url = "http://localhost:5000/api/accounts"
    pesel = "12345678902"

    def setUp(self):
        requests.post(self.url, json={"imie": "Jan", "nazwisko": "Kowalski", "pesel": self.pesel})

    def tearDown(self):
        requests.delete(self.url + "/" + self.pesel)

    def test_incoming_transfer(self):
        transfer_response = requests.post(self.url + f"/{self.pesel}/transfer", json={"amount": 100, "type": "incoming"})
        self.assertEqual(transfer_response.status_code, 200)
        account_response = requests.get(self.url + f"/{self.pesel}")
        self.assertEqual(account_response.status_code, 200)
        self.assertEqual(account_response.json()["saldo"], 100)

    def test_outgoing_transfer(self):
        requests.post(self.url + f"/{self.pesel}/transfer", json={"amount": 600, "type": "incoming"})
        requests.post(self.url + f"/{self.pesel}/transfer", json={"amount": 100, "type": "outgoing"})
        account_response = requests.get(self.url + f"/{self.pesel}")
        self.assertEqual(account_response.status_code, 200)
        self.assertEqual(account_response.json()["saldo"], 500)

    def test_failed_outgoing_transfer(self):
        requests.post(self.url + f"/{self.pesel}/transfer", json={"amount": 600, "type": "incoming"})
        requests.post(self.url + f"/{self.pesel}/transfer", json={"amount": 100, "type": "outgoing"})
        account_response = requests.get(self.url + f"/{self.pesel}")
        self.assertEqual(account_response.status_code, 200)
        self.assertEqual(account_response.json()["saldo"], 500)

