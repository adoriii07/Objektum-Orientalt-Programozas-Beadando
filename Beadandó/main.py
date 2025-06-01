from Osztályok.Szemelyauto import Szemelyauto
from Osztályok.Teherauto import Teherauto
from Osztályok.Autokolcsonzo import Autokolcsonzo

def kezdeti_adatok(kolcsonzo):
    auto1 = Szemelyauto(rendszam="AAA-111", tipus= "Opel Astra", berleti_dij= 10000)
    auto2 = Szemelyauto(rendszam="BBB-222", tipus= "Citroen Combi", berleti_dij= 8000)
    auto3 = Teherauto(rendszam="CCC-333", tipus= "Ford Transit", berleti_dij= 15000)

    kolcsonzo.auto_listazasa(auto1)
    kolcsonzo.auto_listazasa(auto2)
    kolcsonzo.auto_listazasa(auto3)

    kolcsonzo.auto_berlese("AAA-111", "2025-05-28", "Eötvös Loránd")
    kolcsonzo.auto_berlese("BBB-222", "2025-05-29", "Nemes Tihamér")
    kolcsonzo.auto_berlese("CCC-333", "2025-05-30", "Neumann János")
    kolcsonzo.auto_berlese("AAA-111", "2025-05-30", "Gábor Dénes")

def menu():
    print("\n--- Autókölcsönző ---")
    print("1. Autó bérlése")
    print("2. Bérlés lemondása")
    print("3. Bérlések listázása")
    print("4. Kilépés")

def main():
    kolcsonzo = Autokolcsonzo("Példa Autókölcsönző")
    kezdeti_adatok(kolcsonzo)

    while True:
        menu()
        valasztas = input("Választás (1-4): ").strip()

        if valasztas == "1":
            rendszam = input("Rendszám: ").strip().upper()
            datum = input("Dátum (ÉÉÉÉ-HH-NN): ").strip()
            nev = input("Név: ").strip()
            eredmeny = kolcsonzo.auto_berlese(rendszam, datum, nev)
            print(f"\n{eredmeny}")

        elif valasztas == "2":
            rendszam = input("Rendszám: ").strip().upper()
            datum = input("Dátum (ÉÉÉÉ-HH-NN): ").strip()
            nev = input("Név: ").strip()
            eredmeny = kolcsonzo.berles_lemondasa(rendszam, nev, datum)
            print(f"\n{eredmeny}")

        elif valasztas == "3":
            lista = kolcsonzo.osszes_berles()
            print("\n--- Aktív bérlések ---")
            if isinstance(lista, list):
                for b in lista:
                    print(b)
            else:
                print(lista)

        elif valasztas == "4":
            print("Kilépett a programból.")
            break

        else:
            print("Hibás választás. Kérlek adj meg 1 és 4 között egy számot.")

if __name__ == "__main__":
    main()
