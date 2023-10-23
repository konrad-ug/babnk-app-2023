class Konto:
    express_transfer_fee = 0
     
    def __init__(self):
        self.saldo = 0
        
    def zaksieguj_przelew_przychodzacy(self, kwota):
        if kwota > 0:
            self.saldo += kwota

    def przelew_wychodzacy(self, kwota):
        if kwota > 0 and kwota <= self.saldo:
            self.saldo -= kwota

    def przelew_wychodzacy_expressowy(self, kwota):
        if kwota > 0 and kwota <= self.saldo:
            self.saldo -= kwota
            self.saldo -= self.express_transfer_fee