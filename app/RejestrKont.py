from .KontoOsobiste import KontoOsobiste
from pymongo import MongoClient


class RejestrKont():
    client = MongoClient('localhost', 27017)
    db = client['mydatabase']
    collection = db['konta']
    lista = []

    @classmethod
    def dodaj_konto(cls, konto):
        cls.lista.append(konto)

    @classmethod    
    def ile_kont(cls):
        return len(cls.lista)

    @classmethod
    def wyszukaj_konto_z_peselem(cls, pesel):
        for konto in cls.lista:
            if konto.pesel == pesel:
                return konto

    @classmethod
    def usun_konto_z_peselem(cls, pesel):
        for konto in cls.lista:
            if konto.pesel == pesel:
                cls.lista.remove(konto)

    @classmethod
    def zaladuj_konta_z_bazy_danych(cls):
        for kontoDB in cls.collection.find():
            konto = KontoOsobiste(kontoDB["name"], kontoDB["surname"], kontoDB["pesel"])
            konto.saldo = kontoDB["saldo"]
            konto.historia = kontoDB["historia"]
            cls.lista.append(konto)

    @classmethod
    def zapisz_konta_do_bazy_danych(cls):
        cls.collection.delete_many({})
        for konto in cls.lista:
            cls.collection.insert_one({"name": konto.name, "surname": konto.surname, "pesel": konto.pesel, "saldo": konto.saldo, "historia": konto.historia})

        