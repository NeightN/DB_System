from database_commands.commands import Commands
from variables import Inputs

class Menu():
    def __init__(self):
        self.command = Commands()
        self.variable = Inputs()
        self.menu = {
            "1": "Vložit objednávlku s dvěma položkami",
            "2": "Smazaní objednávky s objednávkovými položkami",
            "3": "Úprava objednávky",
            "4": "Výpis reportu",
            "5": "Konec"
        }

    def get_menu(self):
        """
        Metoda pro vypsání menu
        :return: Seznam voleb menu
        """
        return self.menu

    def get_vstup(self):
        """
        Metoda pro získání vstupu od uživatele
        :return: Vstup od uživatele
        """
        return self.variable.get_volba()

    def volba(self):
        """
        Metoda pro získání vstupu od uživatele a zavolání příslušné metody
        :return: Příslušná metoda
        """
        while True:
            self.get_menu()
            for key, value in self.menu.items():
                print(key, value)
            vstup = self.get_vstup()
            if vstup == "1":
                zakaznik = self.variable.get_zakaznik()
                mnozstvi1 = self.variable.get_mnozstvi()
                mnozstvi2 = self.variable.get_mnozstvi()
                polozka1 = self.variable.get_polozka()
                polozka2 = self.variable.get_polozka()
                self.command.insert_nova_objednavka_s_dvema_polozkama(zakaznik, mnozstvi1, mnozstvi2, polozka1, polozka2)
            elif vstup == "2":
                objednavka_id = self.variable.get_objednavka_id()
                self.command.delete_objednavka_s_objednanymi_polozkami(objednavka_id)
            elif vstup == "3":
                objednavka_id = self.variable.get_objednavka_id()
                produkt_id = self.variable.get_produkt_id()
                mnozstvi = self.variable.get_mnozstvi()
                self.command.update_objednavky(objednavka_id, produkt_id, mnozstvi)
            elif vstup == "4":
                self.command.select_pro_report()
            elif vstup == "5":
                break
            else:
                print("Neplatná volba")
    def complete_menu(self):
        """
        Metoda pro zobrazení menu
        :return: None
        """
        return self.volba()
