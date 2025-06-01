from Osztályok.Berles import Berles
from datetime import datetime

class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []
        self.berlesek = []

    def auto_listazasa(self, auto):
        self.autok.append(auto)

    class Autokolcsonzo:
        def __init__(self, nev):
            self.nev = nev
            self.autok = []
            self.berlesek = []

        def auto_listazasa(self, auto):
            self.autok.append(auto)

    def auto_berlese(self, rendszam, datum, nev):
        try:
            datetime.strptime(datum, "%Y-%m-%d")
        except ValueError:
            return "Hibás dátumformátum! Használd: ÉÉÉÉ-HH-NN (pl. 2025-06-01)"

        keresett_auto = None
        for auto in self.autok:
            if auto.rendszam == rendszam:
                keresett_auto = auto
                break

        if not keresett_auto:
            return f"Nincs ilyen rendszámú autó: {rendszam}"

        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam and berles.datum == datum:
                return f"Az autó már foglalt ezen a napon: {datum}"

        uj_berles = Berles(keresett_auto, datum, nev)
        self.berlesek.append(uj_berles)
        return f"Sikeres bérlés: {rendszam} ({datum}), ár: {keresett_auto.berleti_dij} Ft"

    def berles_lemondasa(self, rendszam, nev, datum):
        try:
            datetime.strptime(datum, "%Y-%m-%d")
        except ValueError:
            return "Hibás dátumformátum! Használj ÉÉÉÉ-HH-NN formátumot (pl. 2025-06-01)"

        for berles in self.berlesek:
            if (
                    berles.auto.rendszam == rendszam
                    and berles.nev == nev
                    and berles.datum == datum
            ):
                self.berlesek.remove(berles)
                return "Bérlés sikeresen lemondva."

        return "Nem található ilyen bérlés (név + rendszám + dátum alapján)."

    def osszes_berles(self):
        if not self.berlesek:
            return "Nincsenek aktív bérlések."
        return [f"{b.nev} bérelte: {b.auto.rendszam} ({b.auto.tipus}) - {b.datum}" for b in self.berlesek]
