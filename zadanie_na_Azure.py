"""
=============================================================================
ZADANIE NA DOMA — IoT Backend: Prevodník jednotiek s ukladaním do súboru
=============================================================================
Predmet: Internet vecí
Bodovanie: 5 bodov

=============================================================================
ÚLOHA:
=============================================================================
Rozšírte projekt z cvičenia o prevodník jednotiek pre IoT senzory.
Každý prevod sa uloží do JSON súboru na serveri a výsledky
sa zobrazia na Frontend B.

=============================================================================
POŽIADAVKY:
=============================================================================

1. BACKEND — endpoint /api/prevod (2 body)
   - Prijme GET parametre: hodnota (číslo) + typ (typ prevodu)
   - Podporované prevody (min. 3):
       • °C → °F
       • hPa → mmHg  (tlak)
       • m/s → km/h   (rýchlosť vetra)
       (alebo vlastné, ak dávajú zmysel pre IoT senzory)
   - Výsledok uloží do súboru "prevody.json" na serveri
     (súbor obsahuje ZOZNAM všetkých doterajších prevodov)
   - Vráti JSON odpoveď s výsledkom

2. BACKEND — endpoint /api/historia-prevodov (1 bod)
   - Načíta súbor "prevody.json" a vráti jeho obsah ako JSON
   - Ak súbor neexistuje, vráti prázdny zoznam []

3. FRONTEND A — formulár (1 bod)
   - <input type="number"> — zadanie hodnoty
   - <select> — výber typu prevodu (°C→°F, hPa→mmHg, m/s→km/h)
   - <button type="submit"> — odoslanie
   - Po odoslaní zobrazte výsledok na stránke

4. FRONTEND B — zobrazenie histórie (1 bod)
   - Načítajte históriu prevodov cez fetch() z /api/historia-prevodov
   - Zobrazte ju v tabuľke (vstup, typ, výsledok, čas)

=============================================================================
UKÁŽKY KÓDU (na naštudovanie, NIE na skopírovanie):
=============================================================================
"""

# ── UKÁŽKA: Ukladanie do JSON súboru ──

"""
import json
import os

SUBOR = "prevody.json"

def nacitaj_prevody():
    if not os.path.exists(SUBOR):
        return []
    with open(SUBOR, "r", encoding="utf-8") as f:
        return json.load(f)

def uloz_prevod(zaznam):
    prevody = nacitaj_prevody()
    prevody.append(zaznam)
    with open(SUBOR, "w", encoding="utf-8") as f:
        json.dump(prevody, f, ensure_ascii=False, indent=2)
"""

# ── UKÁŽKA: Endpoint s výpočtom ──

"""
@app.route("/api/prevod")
def prevod():
    hodnota = request.args.get("hodnota", type=float)
    typ = request.args.get("typ", "c_to_f")

    if hodnota is None:
        return jsonify({"chyba": "Zadajte hodnotu!"}), 400

    if typ == "c_to_f":
        vysledok = (hodnota * 9/5) + 32
        popis = f"{hodnota} °C = {vysledok:.2f} °F"
    elif typ == "hpa_to_mmhg":
        vysledok = hodnota * 0.75006
        popis = f"{hodnota} hPa = {vysledok:.2f} mmHg"
    # ... ďalšie prevody ...

    zaznam = {
        "hodnota": hodnota,
        "typ": typ,
        "vysledok": round(vysledok, 2),
        "popis": popis,
        "cas": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    uloz_prevod(zaznam)  # <-- uloženie do súboru

    return jsonify(zaznam)
"""

# ── UKÁŽKA: Načítanie histórie ──

"""
@app.route("/api/historia-prevodov")
def historia_prevodov():
    return jsonify(nacitaj_prevody())
"""

# =============================================================================
# ODOVZDANIE:
# =============================================================================
# 1. Upravené súbory: app.py, frontend_a.html, frontend_b.html
# 2. Funkčné nasadenie na Azure App Service
#
# =============================================================================
# HODNOTENIE:
# =============================================================================
# ✅ Endpoint /api/prevod funguje a ukladá do súboru         (2 body)
# ✅ Endpoint /api/historia-prevodov číta zo súboru           (1 bod)
# ✅ Frontend A formulár s inputom, selectom a buttonom       (1 bod)
# ✅ Frontend B zobrazuje históriu prevodov z API             (1 bod)
# ─────────────────────────────────────────────────────────────
# SPOLU: 5 bodov
# =============================================================================
