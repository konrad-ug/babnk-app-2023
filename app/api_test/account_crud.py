import requests
import unittest

class TestAccountCrud(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.url = "http://localhost:5000/api/accounts"

    def test_1_create_account(self):
        response = requests.post(self.url, json={"imie": "Jan", "nazwisko": "Kowalski", "pesel": "12345678901"})
        self.assertEqual(response.status_code, 201)

    def test_2_try_to_create_with_the_same_pesel(self):
        response = requests.post(self.url, json={"imie": "Jan", "nazwisko": "Kowalski", "pesel": "12345678901"})
        self.assertEqual(response.status_code, 409)
        count_number_response = requests.get(self.url + "/count")
        self.assertEqual(count_number_response.json()["count"], 1)

    def test_2_get_account_by_pesel(self):
        response = requests.get(self.url + "/12345678901")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"name": "Jan", "nazwisko": "Kowalski", "pesel": "12345678901", "saldo": 0})

    def test_3_not_existing_account(self):
        respons = requests.get(self.url + "/12345678990")
        self.assertEqual(respons.status_code, 404)
