import unittest

from ..KontoOsobiste import KontoOsobiste

class TestCreateBankAccount(unittest.TestCase):

    def test_tworzenie_konta(self):
        pierwsze_konto = KontoOsobiste("Dariusz", "Januszewski", "89092909876")
        self.assertEqual(pierwsze_konto.name, "Dariusz", "Imie nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.surname, "Januszewski", "Nazwisko nie zostało zapisane!")
        self.assertEqual(pierwsze_konto.saldo, 0, "Saldo nie jest zerowe!")
        self.assertEqual(pierwsze_konto.pesel, "89092909876", "pesel nie został zapisany!")

    def test_tworzenie_konta_z_niepoprawnym_pesel(self):
        konto = KontoOsobiste("Dariusz", "Januszewski", "89092909874ddd")
        self.assertEqual(konto.pesel, "niepoprawny pesel")

    def test_tworzenie_konta_z_poprawnym_kodem(self):
        konto = KontoOsobiste("Dariusz", "Januszewski", "89092909876", "PROM_123")
        self.assertEqual(konto.saldo, 50, "Saldo nie jest poprawne")

    def test_too_long_promo_code(self):
        konto = KontoOsobiste("Dariusz", "Januszewski", "89092909876", "PROM_1234")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest poprawne")

    def test_too_short_promo_code(self):
        konto = KontoOsobiste("Dariusz", "Januszewski", "89092909876", "PROM_12")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest poprawne")
    
    def test_incorrect_promo_code(self):
        konto = KontoOsobiste("Dariusz", "Januszewski", "89092909876", "AAA_124")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest poprawne")

    def test_born_after_50_correct_code(self):
        konto = KontoOsobiste("Dariusz", "Januszewski", "03292909875", "PROM_123")
        self.assertEqual(konto.saldo, 50, "Saldo nie jest poprawne")

    def test_born_after_50_incorrect_code(self):
        konto = KontoOsobiste("Dariusz", "Januszewski", "50092909876", "PROM_1234")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest poprawne")

    def test_born_after_2000_incorrect_code(self):
        konto = KontoOsobiste("Dariusz", "Januszewski", "04092909876", "PROM_123")
        self.assertEqual(konto.saldo, 0, "Saldo nie jest poprawne")
    #tutaj proszę dodawać nowe testy