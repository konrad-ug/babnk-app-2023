from .KontoOsobiste import Konto
import requests
import os
import datetime

class KontoFirmowe(Konto):    
    express_transfer_fee = 5
    def __init__(self, name, nip):
        self.historia = []
        self.name = name
        self.saldo = 0
        if len(nip) != 10:
            self.nip = "Niepoprawny NIP!"
            return
        else:
            self.nip = nip
        if not self.czy_nip_istnieje_w_gov(self.nip):
            raise Exception("NIP nie istnieje w gov")

    def zaciagnij_kredyt(self, wnioskowana_kwota):
        if self.saldo >= 2 * wnioskowana_kwota and self.historia.count(-1775) > 0:
            self.saldo += wnioskowana_kwota
            return True
        else:
            return False
        
    @classmethod
    def czy_nip_istnieje_w_gov(cls, nip):
        gov_url = os.getenv('BANK_APP_MF_URL', 'https://wl-test.mf.gov.pl/')
        today = datetime.datetime.today().strftime('%Y-%m-%d')
        nip_path = f"{gov_url}api/search/nip/{nip}/?date={today}"
        print(f"sending requests to {nip_path}")
        response = requests.get(nip_path)
        print(f"Response dla nipu: {response.status_code}, {response.json()}")
        if response.status_code == 200:
            return True
        return False

    def wyslij_historie_na_maila(self, adresat, smtp_connection):
        tresc = f"Historia konta Twojej firmy to: {self.historia}"
        temat = f"Wyciąg z dnia {datetime.datetime.today().strftime('%Y-%m-%d')}"
        return smtp_connection.wyslij(temat, tresc, adresat)
