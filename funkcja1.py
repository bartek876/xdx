class Uczen:
    def __init__(self,_imie,_nazwisko,_wiek,_wzrost,_pochodzenie,_kolor_skóry) -> None:
        self.imie =_imie
        self.nazwisko =_nazwisko
        self.wiek =_wiek
        self.wzrost =_wzrost
        self.pochodzenie =_pochodzenie
        self.kolor_skóry =_kolor_skóry

    def inf(self):
        print(f"imie: {self.imie}")
        print(f"imie: {self.nazwisko}")
        print(f"wiek: {self.wiek}")
        print(f"wzrost: {self.wzrost}")
        print(f"pochodzenie: {self.pochodzenie}")
        print(f"kolor_skóry: {self.kolor_skóry}")

    def następny(self):
        print("następny")

u1 = Uczen("Marcin","Grucha","12","167","Polska","Biały")
u2 = Uczen("Adam","Nowak","13","187","Polska","Biały")
u3 = Uczen("Mateusz","Dąbrowski","14","179","Anglia","Biały")
u4 = Uczen("Bartosz","Kowalski","13","187","Polska","Biały")
u5 = Uczen("Mahamadou","Rabi","19","203","Niger","Czarny")

u1.inf()
u1.następny()
#-------------------------------
u2.inf()
u2.następny()
#-------------------------------
u3.inf()
u3.następny()
#-------------------------------
u4.inf()
u4.następny()
#-------------------------------
u5.inf()
u5.następny()
            
