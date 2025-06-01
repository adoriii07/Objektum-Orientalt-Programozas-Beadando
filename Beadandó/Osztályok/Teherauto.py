from Osztályok.Auto import *
class Teherauto(Auto):
    def __str__(self, rendszam, berleti_dij):
        self.rendszam = rendszam
        self.berleti_dij = berleti_dij
        self.berlesek = []
        self.tipus = "Teherautó"