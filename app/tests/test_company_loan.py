import unittest
from parameterized import parameterized

from ..KontoFirmowe import KontoFirmowe

class TestKredyt(unittest.TestCase):
    nazwa_firmy = "Januszex sp. z o.o"
    nip = "8461627563"

    def setUp(self):
        self.konto = KontoFirmowe(self.nazwa_firmy, self.nip)

    @parameterized.expand([
        ([100, 100, -1775], 1000, 500, True, 1500),
        ([-100, 100, -1775, 100, 1000], 800, 401, False, 800),
        ([-100, 1775, -1775, 100, -1000], 1000, 200, True, 1200),
        ([100], 666, 100, False, 666),
        ([-100, 100, 100, 100, -600, 200], 500, 1, False , 500),
    ])
    def test_company_account_creation(self, historia, saldo, wnioskowana_kwota, oczekiwany_wynik_wniosku, oczekiwane_saldo):
        self.konto.saldo = saldo
        self.konto.historia = historia
        is_credit_accepted = self.konto.zaciagnij_kredyt(wnioskowana_kwota)
        self.assertEqual(is_credit_accepted, oczekiwany_wynik_wniosku)
        self.assertEqual(self.konto.saldo, oczekiwane_saldo)

   