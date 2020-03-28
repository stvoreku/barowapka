menu = 'BeerBarBack\n\nWybierz opcję wpisując numer.\n1.Startuj!\n2.Zamknij.'
inne = 'Wybierz z podanych opcji'
menu2 = '1.Szukaj piwa.\n2.Dodaj piwo.\n3.Edytuj piwo.\n4.Usuń piwo.\n5.Wróć.'

class Piwo:
    def __init__(self,nazwa,kolor,aromat,goryczka,moc,opis):
        self.nazwa = nazwa
        self.kolor = kolor
        self.aromat = aromat
        self.goryczka = goryczka
        self.moc = moc
        self.opis = opis
def pierwsza_strona():
    print(menu)
    while True:
        start = input()
        if start == '1':
            def druga_strona():
                print(menu2)
                while True:
                    wybor = input()
                    if wybor == '1':
                        szukaj_piwa = input('Wpisz szukaną nazwę piwa: ')
                        for szukaj_piwa in Piwo:
                            print(szukaj_piwa)
                        druga_strona()
                        break
                    elif wybor == '2':
                        def dodanie_piwa(self):
                            self.nazwa = input('Podaj nazwę: ')
                            self.kolor = input('Podaj kolor: ')
                            self.aromat = input('Podaj aromat: ')
                            self.goryczka = input('Podaj goryczke: ')
                            self.moc = input('Podaj moc: ')
                            self.opis = input('Podaj opis: ')

                            self.nazwa = Piwo(self.nazwa, self.kolor, self.aromat, self.goryczka, self.moc, self.opis)
                            print('Dodano' + self.nazwa)
                        druga_strona()
                        break
                    elif wybor == '3':
                        print('coś tam')
                        druga_strona()
                        break
                    elif wybor == '4':
                        usun_piwo = input('Podaj nazwę piwa do usunięcia: ')
                        del usun_piwo
                        druga_strona()
                        break
                    elif wybor == '5':
                        pierwsza_strona()
                        break
                    else:
                        print(inne)

                    break
        elif start == '2':
            print('Do widzenia, do jutra!')
            break
        else:
            print(inne)