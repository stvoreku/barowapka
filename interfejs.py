print("BeerBarBack\n\nWybierz opcję wpisując numer.\n1.Startuj!\n2.Zamknij.")
menu = str(input())
print(menu =='1')
if menu == '1':
    print ("Wybierz kolor:\n1.Jasne\n2.Ciemne")
    kolor = input()
    if kolor == 1:
        print("dalszy kod")
    elif kolor == 2:
        print("dalszy kod")
    else:
        print("Wybierz spośród podanych opcji.")
elif menu == '2':
    print("Do widzenia, do jutra.")
else:
    print("Wybierz spośród podanych opcji.")

class Piwo:
    def __init__(self, nazwa, gatunek, procent, barwa, aromat):
        self.nazwa = nazwa
        self.gatunek = gatunek
        self.procent = procent
        self.barwa = barwa
        self.aromat = aromat
    def tell(self):
        print('Twoje piwo to: "{}" "{}" "{}" "{}" "{}"'.format(self.nazwa, self.gatunek, self.procent, self.barwa, self.aromat))

za = Piwo("Zissou APA", "american pale ale", "5.0%", "jasno-złota", "cytrusy i owoce tropikalne" )
ji = Piwo("Jungle IPA", "india pale ale", "6.0%", "złota", "orientalne przyprawy, cytrusy i mango" )
m = Piwo("Miami", "lager", "4,6%", "jasno-złota", "cytrusy i kwiaty")
nrs = Piwo("No Reason Saison", "saison", "5,6%", "jasno-złota", "owocowo-przyprawowe ze skórką pomarańczy")
scp = Piwo("Sleeping Car Porter", "milk porter", "5,5%", "ciemno-brązowa", "kawa, chleb i suszone owoce")
p = Piwo("Pilzner", "bohemian pils", "4,8%", "słomiana", "słód z delikatnymi przyprawami")
t = Piwo("Topaz", "american weizen", "4,7%", "słomiana", "banany, cytrusy i owoce egzotyczne")
wi = Piwo("Witkac IPA", "session rye india pale ale", "5,1%", "złota", "słodoko-cytrusowe z aromatem kwiatów")