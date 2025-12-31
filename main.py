# --- 🏥 Lab-Result-Verifier v1.0 ---
# Moduł odpowiedzialny za logikę medyczną

# 1. BAZA WIEDZY (Słownik)
# Tu definiujemy normy. Kluczem jest nazwa badania, a wartością zestaw granic.
NORMY_LABORATORYJNE = {
    "HGB": {
        "min": 12.0, "max": 16.0,   # Norma podstawowa
        "alarm_min": 7.0, "alarm_max": 20.0, # Wartości krytyczne
        "jednostka": "g/dL"
    },
    "WBC": {
        "min": 4.0, "max": 10.0,
        "alarm_min": 1.5, "alarm_max": 30.0,
        "jednostka": "tys/uL"
    },
    "PLT": {
        "min": 150, "max": 400,
        "alarm_min": 30, "alarm_max": 1000,
        "jednostka": "tys/uL"
    },
    "TSH": {
        "min": 0.27, "max": 4.20,
        "alarm_min": 0.01, "alarm_max": 100.0,
        "jednostka": "uIU/mL"
    }
}

# 2. SILNIK WERYFIKACJI (Funkcja)
def weryfikuj_wynik(badanie, wynik):
    """
    Funkcja przyjmuje nazwę badania (np. 'HGB') i wynik (np. 11.5).
    Zwraca flagę (L, H, N, CRITICAL) oraz komentarz.
    """
    
    # Krok A: Sprawdzamy, czy w ogóle mamy normę dla tego badania
    if badanie not in NORMY_LABORATORYJNE:
        return "?", "Brak normy w bazie"

    # Pobieramy konkretne normy dla tego jednego badania
    norma = NORMY_LABORATORYJNE[badanie]
    
    # Krok B: Sprawdzamy wartości KRYTYCZNE (Najważniejsze!)
    if wynik <= norma["alarm_min"]:
        return "!!!", "KRYTYCZNIE NISKI"
    if wynik >= norma["alarm_max"]:
        return "!!!", "KRYTYCZNIE WYSOKI"
        
    # Krok C: Sprawdzamy normy zwykłe
    if wynik < norma["min"]:
        return "L", "Poniżej normy"
    if wynik > norma["max"]:
        return "H", "Powyżej normy"
        
    # Krok D: Jeśli nic powyżej nie zaszło, to jest OK
    return "N", "W normie"

# --- 3. TESTY MANUALNE (Sprawdzamy czy działa) ---
print("--- TEST SILNIKA ---")

# Lista przypadków do sprawdzenia: (Nazwa, Wynik)
przypadki_testowe = [
    ("HGB", 14.5),  # Powinno być N
    ("HGB", 6.8),   # Powinno być !!! (Krytyczne)
    ("PLT", 50),    # Powinno być L
    ("WBC", 15.0),  # Powinno być H
    ("XYZ", 100)    # Nieznane badanie
]

for badanie, wartosc in przypadki_testowe:
    flaga, opis = weryfikuj_wynik(badanie, wartosc)
    print(f"Badanie: {badanie} | Wynik: {wartosc} -> Flaga: [{flaga}] ({opis})")
