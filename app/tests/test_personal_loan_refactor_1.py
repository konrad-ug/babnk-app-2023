import unittest
from parameterized import parameterized
from ..KontoOsobiste import KontoOsobiste

class TestKredyt(unittest.TestCase):
    imie = "darek"
    nazwisko = "Januszewski"
    pesel = "66092909876"
        


    @parameterized.expand([ #[[history], wnioskowana_kwota, oczekiwany_wynik_wniosku, oczekiwane_saldo]
        ([100, 100, 100], 500, True, 500),
        ([100, 100, 100, -3], 500, False, 0)
     ])
    def test_3_przychodzace_przelewy(self, historia, wnioskowana_kwota, oczekiwany_wynik_wniosku, oczekiwane_saldo):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        konto.historia = historia
        czy_przyznany = konto.zaciagnij_kredyt(wnioskowana_kwota)
        self.assertEqual(czy_przyznany, oczekiwany_wynik_wniosku)
        self.assertEqual(konto.saldo, oczekiwane_saldo)
    