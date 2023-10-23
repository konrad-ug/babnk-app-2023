from .Konto import Konto

class KontoOsobiste(Konto):
    express_transfer_fee = 1

    def __init__(self, imie, nazwisko, pesel, kod_promocyjny=None):
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