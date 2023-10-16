import unittest

from ..Konto import Konto

class TestTransfer(unittest.TestCase):
    personal_data = {
        "name": "Dariusz",
        "surname": "Januszewski",
        "pesel": "89092909876",
    }
    def test_incoming_transfer(self):
        pierwsze_konto = Konto(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        pierwsze_konto.przelew_przychodzacy(100)
        self.assertEqual(pierwsze_konto.saldo, 100, "Saldo nie jest poprawne!")

    def test_incoming_transfer_with_incorrect_amount(self):
        pierwsze_konto = Konto(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        pierwsze_konto.przelew_przychodzacy(-100)
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest poprawne!")

    def test_outgoing_transfer(self):
        pierwsze_konto = Konto(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        pierwsze_konto.saldo = 120
        pierwsze_konto.przelew_wychodzacy(100)
        self.assertEqual(pierwsze_konto.saldo, 20, "Saldo nie jest poprawne!")

    def test_series_of_transfers(self):
        konto = Konto(self.personal_data["name"], self.personal_data["surname"], self.personal_data["pesel"])
        konto.przelew_przychodzacy(100)
        konto.przelew_przychodzacy(120)
        konto.przelew_wychodzacy(50)
        self.assertEqual(konto.saldo, 100+120-50, "Saldo nie jest poprawne!")