MENU = 'BeerBarBack\n\nWybierz opcję wpisując numer.\n1.Startuj!\n2.Zamknij.'
INNE = 'Wybierz z podanych opcji'
MENU2 = '1.Szukaj piwa.\n2.Dodaj piwo.\n3.Edytuj piwo.\n4.Usuń piwo.\n5.Wypisz piwka.\n 6. Wróć' #Kwetstia estetyki - predefiniowane 'stałe' wielkimi literami


#kod jest obecnie troche zbyt rozlazly aby byl czytelny - przerzucę funkcje w górę aby były bardziej czytelne
class Piwo:
    def __init__(self,nazwa,kolor,aromat,goryczka,moc,opis):
        self.nazwa = nazwa
        self.kolor = kolor
        self.aromat = aromat
        self.goryczka = goryczka
        self.moc = moc
        self.opis = opis
    def wypisz_podstawowe(self):
        print("Nazwa: {}\t Moc: {}\t Aromat: {}".format(self.nazwa, self.moc, self.aromat)) #moja ulubiona forma stringow. format wstawia w {} kolejne zmienne, \t to tabulator

wszystkie_piwa = []


def dodanie_piwa():  # Ten self tutaj był niepotrzebny. Self używasz jak definiujesz metodę wewnątrz obiektu. Patrz metoda __init__
    nazwa = input('Podaj nazwę: ')
    kolor = input('Podaj kolor: ')
    aromat = input('Podaj aromat: ')
    goryczka = input('Podaj goryczke: ')
    moc = input('Podaj moc: ')
    opis = input('Podaj opis: ')

    nowe_piwo = Piwo(nazwa, kolor, aromat, goryczka, moc, opis)  # nawet czytelniej!

    # Problem tu jest taki że utworzyliśmy sobie nowe piwo które wisi w powietrzu - nie ma żadnej opcji odzyskania go. Pozwoliłem
    # sobie na zrobienie na górze list piwek aby je trzymać, dodanie w obiekcie piwko metody na wypisanie, i trzymanie ich w tej liście

    wszystkie_piwa.append(nowe_piwo)

    print('Dodano: ' + nowe_piwo.nazwa)  # sanity check, sprawdzam czy to co mysle ze utworzylem faktycznie utworzyłem

def pierwsza_strona():
    start = '0'
    while True:
        if start == '0': #to się wypisze tylko jak start jest 0. Czyli przy pierwszym wykonaniu lub jak ktoś wprost powiedział że chce wyjść
            print(MENU)
            start = input()
        elif start == '1':
            print(MENU2)
            while True:
                wybor = input()
                if wybor == '1':
                    szukaj_piwa = input('Wpisz szukaną nazwę piwa: ')
                    for piwo in wszystkie_piwa: #uwaga takie przeszukiwanie jest niewydajne, ale to oddzielny temat.
                        if piwo.nazwa == szukaj_piwa:
                            piwo.wypisz_podstawowe()
                    break
                elif wybor == '2':
                    dodanie_piwa()
                    break
                elif wybor == '3':
                    print('coś tam')
                    break
                elif wybor == '4':
                    usun_piwo = input('Podaj nazwę piwa do usunięcia: ')
                    for piwko in wszystkie_piwa:
                        if piwko.nazwa == usun_piwo:
                            del piwko
                    break
                elif wybor == '6':
                    start = '0' #tak rozwiazalem poruszanie się. Zrównanie start na zero sprawi że w kolejnym przejściu jeśli wyszliśmy to wrócimy na początek
                    break
                elif wybor == '5':
                    for piwko in wszystkie_piwa:
                        piwko.wypisz_podstawowe()
                    break
                else:
                    print(INNE)
                break
        elif start == '2':
            print('Do widzenia, do jutra!')
            break
        else:
            print(INNE)



#Tu musimy wywolac ta funkcje
pierwsza_strona()