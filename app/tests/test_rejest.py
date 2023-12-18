import unittest

from ..KontoOsobiste import KontoOsobiste
from ..RejestrKont import RejestrKont
from unittest.mock import patch, MagicMock

class TxxxestRejestr(unittest.TestCase):
    imie = "darek"
    nazwisko = "Januszewski"
    pesel = "66092909876"

    # @classmethod
    # def setUpClass(cls):
    #     konto = KontoOsobiste(cls.imie, cls.nazwisko, cls.pesel)
    #     RejestrKont.dodaj_konto(konto)

    def setUp(self):
        RejestrKont.lista = []

    def test_1_dodawanie_pierwszego_konta(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        konto1 = KontoOsobiste(self.imie + "ddd", self.nazwisko, self.pesel)
        RejestrKont.dodaj_konto(konto)
        RejestrKont.dodaj_konto(konto1)
        self.assertEqual(RejestrKont.ile_kont(), 2)

    def test_2_dodawania_drugie_konta(self):
        konto = KontoOsobiste(self.imie, self.nazwisko, self.pesel)
        RejestrKont.dodaj_konto(konto)
        self.assertEqual(RejestrKont.ile_kont(), 1)

    @classmethod
    def tearDownClass(cls):
        RejestrKont.lista = []

    @patch('app.RejestrKont.RejestrKont.collection')
    def test_zaladuj_konta_z_bazy_danych(self, mock_collection):
        mock_collection.find.return_value = [
            {"name": "Jan", "surname": "Kowalski", "pesel": "89092909875", "saldo": 1000, "historia": []}
        ]
        RejestrKont.zaladuj_konta_z_bazy_danych()
        self.assertEqual(len(RejestrKont.lista), 1)
        self.assertEqual(RejestrKont.lista[0].name, 'Jan')
        self.assertEqual(RejestrKont.lista[0].surname, 'Kowalski')
        self.assertEqual(RejestrKont.lista[0].pesel, '89092909875')
        self.assertEqual(RejestrKont.lista[0].saldo, 1000)
        self.assertEqual(RejestrKont.lista[0].historia, [])

    @patch('app.RejestrKont.RejestrKont.collection')
    def test_zapisz_konta_do_bazy_danych(self, mock_collection):
        konto = KontoOsobiste('Jan', 'Kowalski', '1234567890')
        konto.saldo = 1000
        konto.historia = [100, 200, -500]
        RejestrKont.lista.append(konto)
        RejestrKont.zapisz_konta_do_bazy_danych()
        mock_collection.delete_many.assert_called_once_with({})
        mock_collection.insert_one.assert_called_once_with({"name": 'Jan', "surname": 'Kowalski', "pesel": 'niepoprawny pesel', "saldo": 1000, "historia": [100, 200, -500]})