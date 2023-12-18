from flask import Flask, request, jsonify
from app.RejestrKont import RejestrKont
from app.KontoOsobiste import KontoOsobiste


app = Flask(__name__)

@app.route("/api/accounts/load", methods=['PATCH'])
def load():
    RejestrKont.zaladuj_konta_z_bazy_danych()
    return jsonify({"message": f"Konta zaladowane. Ilość kont: {len(RejestrKont.lista)}" }), 200

@app.route("/api/accounts/save", methods=['PATCH'])
def save():
    RejestrKont.zapisz_konta_do_bazy_danych()
    return jsonify({"message": f"Konta zapisane. Ilość kont: {len(RejestrKont.lista)}" }), 200

@app.route("/api/accounts", methods=['POST'])
def stworz_konto():
    dane = request.get_json()
    print(f"Request o stworzenie konta z danymi: {dane}")
    if RejestrKont.wyszukaj_konto_z_peselem(dane["pesel"]) != None:
        return jsonify({"message": "Konto juz istnieje"}), 409
    konto = KontoOsobiste(dane["imie"], dane["nazwisko"], dane["pesel"])
    RejestrKont.dodaj_konto(konto)
    return jsonify({"message": "Konto stworzone"}), 201


@app.route("/api/accounts/count", methods=['GET'])
def ile_kont():
    ilosc_kont = RejestrKont.ile_kont()
    return jsonify({"count": ilosc_kont}), 200


@app.route("/api/accounts/<pesel>", methods=['GET'])
def wyszukaj_konto_z_peselem(pesel):
    konto = RejestrKont.wyszukaj_konto_z_peselem(pesel)
    if  konto != None:
        return jsonify({"name": konto.name, "nazwisko": konto.surname, "pesel": konto.pesel, "saldo": konto.saldo }), 200
    else:
        return jsonify({"message": "Nie znaleziono konta"}), 404
    
@app.route("/api/accounts/<pesel>", methods=['DELETE'])
def usun_konto_z_peselem(pesel):
    konto = RejestrKont.wyszukaj_konto_z_peselem(pesel)
    if  konto != None:
        RejestrKont.usun_konto_z_peselem(pesel)
        return jsonify({"message": "konto usuniete"}), 200
    else:
        return jsonify({"message": "Nie znaleziono konta"}), 404
    
@app.route("/api/accounts/<pesel>/transfer", methods=['POST'])
def transfer(pesel):
    dane = request.get_json()
    amount = dane["amount"]
    type = dane["type"]
    konto = RejestrKont.wyszukaj_konto_z_peselem(pesel)
    if konto == None:
        return jsonify({"message": "Nie znaleziono konta"}), 404
    if type == "incoming":
        konto.zaksieguj_przelew_przychodzacy(amount)
    elif type == "outgoing":
        konto.przelew_wychodzacy(amount)
    return jsonify({"message": "Zlecenie przyjeto do realizacji"}), 200