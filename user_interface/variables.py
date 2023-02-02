class Inputs():
    def __init__(self):
        self.mnozstvi = None
        self.polozka = None
        self.zakaznik = None
        self.objednavka_id = None
        self.produkt_id = None
        self.volba = None

    def get_mnozstvi(self):
        """
        Získá množství
        :return: Číslo množství
        """
        while True:
            try:
                self.mnozstvi = int(input("Zadejte množství: "))
                if self.mnozstvi <= 0:
                    raise Exception
                break
            except Exception:
                print("Množství musí být kladné číslo")
        return self.mnozstvi

    def get_polozka(self):
        """
        Získá číslo položky
        :return: Číslo položky
        """
        while True:
            try:
                self.polozka = int(input("Zadejte číslo položky: "))
                if self.polozka <= 0:
                    raise Exception
                break
            except Exception:
                print("Číslo položky musí být kladné číslo")
        return self.polozka

    def get_zakaznik(self):
        """
        Získá číslo zákazníka
        :return: Číslo zákazníka
        """
        while True:
            try:
                self.zakaznik = int(input("Zadejte číslo zákazníka: "))
                if self.zakaznik <= 0:
                    raise Exception
                break
            except Exception:
                print("Číslo zákazníka musí být kladné číslo")
        return self.zakaznik

    def get_objednavka_id(self):
        """
        Získá číslo objednávky
        :return: Číslo objednávky
        """
        while True:
            try:
                self.objednavka_id = int(input("Zadejte číslo objednávky: "))
                if self.objednavka_id <= 0:
                    raise Exception
                break
            except Exception:
                print("Číslo objednávky musí být kladné číslo")
        return self.objednavka_id

    def get_produkt_id(self):
        """
        Získá číslo produktu
        :return: Číslo produktu
        """
        while True:
            try:
                self.produkt_id = int(input("Zadejte číslo produktu: "))
                if self.produkt_id <= 0:
                    raise Exception
                break
            except Exception:
                print("Číslo produktu musí být kladné číslo")
        return self.produkt_id

    def get_volba(self):
        """
        Získá číslo volby
        :return: Číslo volby
        """
        while True:
            try:
                self.volba = int(input("Zadejte číslo volby: "))
                if self.volba <= 0 or self.volba > 5:
                    raise Exception
                break
            except Exception:
                print("Číslo volby musí být kladné číslo od 1 do 5")
        return self.volba