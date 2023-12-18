from .Konto import Konto
import datetime

class KontoOsobiste(Konto):
    express_transfer_fee = 1

    def __init__(self, imie, nazwisko, pesel, kod_promocyjny=None):
        self.historia = []
        self.name = imie
        self.surname = nazwisko
        if pesel.isdigit() and len(pesel) == 11:
            self.pesel = pesel
        else:
            self.pesel = "niepoprawny pesel"
        if self.is_promo_code_correct(kod_promocyjny) and self.is_born_after_1950():
            self.saldo = 50
        else:
            self.saldo = 0

    def is_promo_code_correct(self, kod_promocyjny):
        if kod_promocyjny is None:
            return False
        if len(kod_promocyjny) != 8:
            return False
        if kod_promocyjny[:5] != "PROM_":
            return False
        return True
    
    def is_born_after_1950(self):
        if int(self.pesel[0:2]) > 50 or int(self.pesel[2:4]) > 20:
            return True
        else:
            return False
        
    def zaciagnij_kredyt(self, kwota):
        if len(self.historia) < 3:
            return False
        if self.historia[-3] > 0 and self.historia[-2] > 0 and self.historia[-1] > 0:
            self.saldo += kwota
            return True
        if len(self.historia) < 5:
            return False
        if sum(self.historia[-5:]) <= kwota:
            return False
        self.saldo += kwota
        return True

    def zaciagnij_kredyt(self, kwota):
        if self.czy_ostatnie_n_transakcji_byly_wplatami(3) or self.oblicz_sume_ostatnich_n_transakcji(5) > kwota: 
            self.saldo += kwota
            return True
        return False
        
    def czy_ostatnie_n_transakcji_byly_wplatami(self, n):
        if len(self.historia) < n:
            return False
        for ksiegowanie in self.historia[-n:]:
            if ksiegowanie < 0:
                return False
        return True

    def oblicz_sume_ostatnich_n_transakcji(self, n):
        if len(self.historia) < n:
            return False
        return sum(self.historia[-n:])
    
    def wyslij_historie_na_maila(self, adresat, smtp_connection):
        tresc = f"Twoja historia konta to: {self.historia}"
        temat = f"Wyciąg z dnia {datetime.datetime.today().strftime('%Y-%m-%d')}"
        return smtp_connection.wyslij(temat, tresc, adresat)