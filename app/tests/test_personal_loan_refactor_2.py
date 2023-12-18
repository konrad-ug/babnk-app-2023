import unittest
from parameterized import parameterized

from ..KontoOsobiste import KontoOsobiste

class TestKredytRefaktor(unittest.TestCase):
    imie = "darek"
    nazwisko = "Januszewski"
    pesel = "66092909876"
    nazwa_firmy = "Januszex sp. z o.o"
    nip = "8461627563"

    def setUp(self):
        self.konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)

    @parameterized.expand([ #[[history], wnioskowana_kwota, oczekiwany_wynik_wniosku, oczekiwane_saldo]
        ([100, 100, 100], 500, True, 500),
        ([-100, 100, -100, 100, 1000], 700, True, 700),
        ([-100, 20000, -100, 100, -1000], 1000, True, 1000),
        ([100], 666, False, 0),
        ([-100, 100, 100, 100, -600, 200], 500, False , 0),
    ])
    def test_zaciaganie_kredytu(self, historia, wnioskowana_kwota, oczekiwany_wynik_wniosku, oczekiwane_saldo):
        self.konto.historia = historia
        is_credit_accepted = self.konto.zaciagnij_kredyt(wnioskowana_kwota)
        self.assertEqual(is_credit_accepted, oczekiwany_wynik_wniosku)
        self.assertEqual(self.konto.saldo, oczekiwane_saldo)