import unittest

from ..KontoOsobiste import KontoOsobiste
from ..KontoFirmowe import KontoFirmowe
from ..SmtpConnection import SMTPConnection
from unittest.mock import patch
from unittest.mock import MagicMock
from datetime import datetime
class TestCreateBankAccount(unittest.TestCase):
    imie = "darek"
    nazwisko = "Januszewski"
    pesel = "66092909876"
    nazwa_firmy = "Januszex sp. z o.o"
    nip = "8461627563"

    def test_wysyłanie_maila_z_historia(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 1000
        konto.przelew_wychodzacy(100)
        smtp_connector = SMTPConnection()
        smtp_connector.wyslij = MagicMock(return_value = True)
        status = konto.wyslij_historie_na_maila("konrad@gmail.com", smtp_connector)
        self.assertTrue(status)
        smtp_connector.wyslij.assert_called_once_with(f"Wyciąg z dnia {datetime.today().strftime('%Y-%m-%d')}", f"Twoja historia konta to: {konto.historia}", "konrad@gmail.com")

    def test_wysyłanie_maila_z_historia_niepowodzenie(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        konto.saldo = 1000
        konto.przelew_wychodzacy(100)
        smtp_connector = SMTPConnection()
        smtp_connector.wyslij = MagicMock(return_value = False)
        status = konto.wyslij_historie_na_maila("konrad@gmail.com", smtp_connector)
        self.assertFalse(status)

    @patch('app.KontoFirmowe.KontoFirmowe.czy_nip_istnieje_w_gov')
    def test_wysyłanie_maila_z_historia_firmowe(self, czy_nip_istnieje_w_gov):
        czy_nip_istnieje_w_gov.return_value = True
        konto = KontoFirmowe(self.nazwa_firmy, self.nip)
        konto.saldo = 1000
        konto.przelew_wychodzacy(100)
        smtp_connector = SMTPConnection()
        smtp_connector.wyslij = MagicMock(return_value = True)
        status = konto.wyslij_historie_na_maila("konrad@gmail.com", smtp_connector)
        self.assertTrue(status)