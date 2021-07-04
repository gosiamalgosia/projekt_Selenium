class Czlowiek():
    def __init__(self, i, w):
        self.imie = i
        self.wiek = w
    gatunek = "homo sapiens"

adam = Czlowiek("Adam", 24)
ewa = Czlowiek("Ewa", 23)

print(adam.imie)
print(adam.gatunek)
print(ewa.imie)
print(ewa.gatunek)
# Import niezbędnych bibliotek
