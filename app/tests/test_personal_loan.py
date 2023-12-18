import unittest
from parameterized import parameterized


from ..KontoOsobiste import KontoOsobiste

class TestKredyt(unittest.TestCase):
    imie = "darek"
    nazwisko = "Januszewski"
    pesel = "66092909876"

    # def test_zaciaganie_kredytow(self, historia, wnioskowana_kwota, oczekiwany_wynik_wniosku, oczekiwane_saldo):
    #     self.konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
    #     self.konto.historia = historia
    #     czy_przyznany = self.konto.zaciagnij_kredyt(wnioskowana_kwota)
    #     self.assertEqual(czy_przyznany, oczekiwany_wynik_wniosku)
    #     self.assertEqual(self.konto.saldo, oczekiwane_saldo)

    def test_3_przychodzace_przelewy(self):
        self.konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        self.konto.historia = [-100, 100, 100, 100]
        czy_przyznany = self.konto.zaciagnij_kredyt(500)
        self.assertTrue(czy_przyznany)
        self.assertEqual(self.konto.saldo, 500)






















    def test_4_mieszane_przelewy(self):
        self.konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        self.konto.historia = [ 100, 100, -100, 1000]
        czy_przyznany = self.konto.zaciagnij_kredyt(500)
        self.assertFalse(czy_przyznany)
        self.assertEqual(self.konto.saldo, 0)

    def test_5_przelewow_kwota_wieksza(self):
        self.konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        self.konto.historia = [-100, 100, -100, 100, 1000]
        czy_przyznany = self.konto.zaciagnij_kredyt(700)
        self.assertTrue(czy_przyznany)
        self.assertEqual(self.konto.saldo, 700)

    def test_5_przelewow_kwota_mniejsza(self):
        self.konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        self.konto.historia = [-100, 100, -100, 100, 200]
        czy_przyznany = self.konto.zaciagnij_kredyt(700)
        self.assertFalse(czy_przyznany)
        self.assertEqual(self.konto.saldo, 0)

    def test_5_przelewow_kwota_mniejsza_3_przychodzace(self):
        self.konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        self.konto.historia = [-1000, 100, 100, 100, 200]
        czy_przyznany = self.konto.zaciagnij_kredyt(700)
        self.assertTrue(czy_przyznany)
        self.assertEqual(self.konto.saldo, 700)