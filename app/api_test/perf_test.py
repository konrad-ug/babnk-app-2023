import requests
import unittest

class TestAccountPerf(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.url = "http://localhost:5000/api/accounts"

    def test_perf_create_account(self):
        for i in range(50):
            pesel = f"223456789{i:02}"
            print(f"Testing with pesel: {pesel}")
            response = requests.post(self.url, json={"imie": "Jan", "nazwisko": "Kowalski", "pesel": pesel}, timeout=2)
            self.assertEqual(response.status_code, 201)
            delete_response = requests.delete(self.url + "/" + pesel, timeout=2)
            self.assertEqual(delete_response.status_code, 200)