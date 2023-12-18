import unittest
from unittest.mock import patch
from ..KontoFirmowe import KontoFirmowe

@patch('app.KontoFirmowe.KontoFirmowe.czy_nip_istnieje_w_gov')
class TestCreateBankAccount(unittest.TestCase):
    name = "JDG"
    nip = "8461627563"
    czy_nip_istnieje_w_gov = True
    
    def test_tworzenie_konta_poprawny_nip(self, czy_nip_istnieje_w_gov):
        czy_nip_istnieje_w_gov.return_value = True
        pierwsze_konto = KontoFirmowe(self.name, self.nip)
        self.assertEqual(pierwsze_konto.name, self.name, "Name incorrect")
        self.assertEqual(pierwsze_konto.nip, self.nip, "NIP incorrect")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")

    def test_tworzenie_konta_z_niepoprawnym_nipem(self, czy_nip_istnieje_w_gov):
        konto = KontoFirmowe(self.name, "123456789")
        self.assertEqual(konto.nip, "Niepoprawny NIP!", "NIP incorrect")

    def test_tworzenie_konta_z_nie_istniejacym_nipem(self, czy_nip_istnieje_w_gov):
        czy_nip_istnieje_w_gov.return_value = False
        with self.assertRaises(Exception) as context:
            konto = KontoFirmowe(self.name, "8461627565")
        self.assertTrue("NIP nie istnieje w gov" in str(context.exception))

    def test_tworzenie_konta(self, mock_czy_nip_istnieje_w_gov):
        # mock_czy_nip_istnieje_w_gov.return_value = True
        pierwsze_konto = KontoFirmowe(self.name, self.nip)
        self.assertEqual(pierwsze_konto.name, self.name, "Nazwa firmy nie została zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.nip, self.nip, "NIP nie zostało zapisany!")



