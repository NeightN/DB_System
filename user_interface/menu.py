from database_commands.commands import Commands

class Menu():
    def __init__(self):
        self.command = Commands()
        self.menu = {
            "1": "Vložit objednávlku s dvěma položkami",
            "2": "Smazaní objednávky s objednávkovými položkami",
            "3": "Úprava objednávky",
            "4": "Výpis reportu",
            "5": "Konec"
        }

    def get_menu(self):
        return self.menu

    def get_vstup(self):
        return input("Zadejte číslo: ")

    def volba(self):
        while True:
            for key, value in self.menu.items():
                print(key, value)
            vstup = self.get_vstup()
            if vstup == "1":
                self.command.insert_nova_objednavka_s_dvema_polozkama(mnozstvi1, mnozstvi2, polozka1, polozka2, zakaznik)
            elif vstup == "2":
                self.command.delete_objednavka_s_objednanymi_polozkami(objednavka_id)
            elif vstup == "3":
                self.command.update_objednavky(objednavka_id, produkt_id, mnozstvi)
            elif vstup == "4":
                self.command.select_pro_report()
            elif vstup == "5":
                break
            else:
                print("Neplatná volba")


