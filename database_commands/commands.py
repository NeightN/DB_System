from datetime import datetime
from config_database.config import Config
import pymysql

class Commands():
    def __init__(self):
        self.connection = None
        self.cursor = None
    def insert_kategorie(self, nazev):
        """
        Vloží kategorii do databáze
        :param nazev: název
        :return: None
        """
        config = Config()
        self.connection = config.get_connection()
        self.cursor = self.connection.cursor()
        self.cursor.execute("START TRANSACTION")
        self.cursor.execute("INSERT INTO kategorie (nazev) VALUES (%s)", (nazev))
        self.cursor.execute("COMMIT")
        self.connection = config.close_connection()

    def insert_nova_objednavka_se_dvema_polozkama(self, zakaznik, polozka1, polozka2, mnozstvi1, mnozstvi2):
        """
        Vloží objednávku s položkama do databáze
        :param zakaznik: zákazník
        :param polozka1: první položka
        :param polozka2: druhá položka
        :param mnozstvi1: mnžství první položky
        :param mnozstvi2: množství druhé položky
        :return: None
        """
        config = Config()
        self.connection = config.get_connection()
        self.cursor = self.connection.cursor()
        self.cursor.execute("START TRANSACTION")
        self.cursor.execute("INSERT INTO objednavka (zakaznik_id, datum_objednavky) VALUES (%s, %s)", (zakaznik, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        objednavka_id = self.cursor.lastrowid
        self.cursor.execute("INSERT INTO objednani_polozky (objednavka_id, produkt_id, mnozstvi) VALUES (%s, %s, %s)", (objednavka_id, polozka1, mnozstvi1))
        self.cursor.execute("INSERT INTO objednani_polozky (objednavka_id, produkt_id, mnozstvi) VALUES (%s, %s, %s)", (objednavka_id, polozka2, mnozstvi2))
        self.cursor.execute("COMMIT")
        self.connection = config.close_connection()

    def delete_objednavka_s_objednanymi_polozkami(self, objednavka_id):
        """
        Smazání obednávky s objednanýma položkama
        :param objednavka_id: objednávka
        :return: None
        """
        config = Config()
        self.connection = config.get_connection()
        self.cursor = self.connection.cursor()
        self.cursor.execute("START TRANSACTION")
        self.cursor.execute("DELETE FROM objednani_polozky WHERE objednavka_id = %s", (objednavka_id))
        self.cursor.execute("DELETE FROM objednavka WHERE id = %s", (objednavka_id))
        self.cursor.execute("COMMIT")
        self.connection = config.close_connection()

    def update_objednavky(self, objednavka_id, produkt_id, mnozstvi):
        """
        Aktualizace množství položky pro danou objednávku
        :param objednavka_id: objednávka
        :param produkt_id: produkt
        :param mnozstvi: množství
        :return:
        """
        config = Config()
        self.connection = config.get_connection()
        self.cursor = self.connection.cursor()
        self.cursor.execute("START TRANSACTION")
        self.cursor.execute("UPDATE objednani_polozky SET mnozstvi = %s WHERE objednavka_id = %s and produkt_id = %s",
                       (mnozstvi, objednavka_id, produkt_id))
        self.cursor.execute("COMMIT")
        self.connection = config.close_connection()

    def select_pro_report(self):
        """
        Výběr pro report
        :return: None
        """
        sql = "SELECT zakaznik.mesto, SUM(objednani_polozky.mnozstvi * produkt.cena) AS soucet_nakupu FROM zakaznik JOIN objednavka ON zakaznik.id = objednavka.zakaznik_id JOIN objednani_polozky ON objednavka.id = objednani_polozky.objednavka_id JOIN produkt ON produkt.id = objednani_polozky.produkt_id GROUP BY zakaznik.mesto"

        config = Config()
        self.connection = config.get_connection()
        self.cursor = self.connection.cursor()
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        print("-------------------------------------------------")
        print("Souhrnný report")
        print("-------------------------------------------------")
        print("Město\t\tSoučet nákupů")
        print("-------------------------------------------------")
        for result in results:
            print(f"{result[0]}\t\t{int(result[1])}" + " Kč")
        print("-------------------------------------------------")
        self.connection = config.close_connection()

    def view_nejprodavanejsi_produkty(self):
        """
        Výpis nejprodávanějších produktů
        :return: None
        """
        sql = "SELECT * FROM v_nejprodavanejsi_produkty;";
        config = Config()
        self.connection = config.get_connection()
        self.cursor = self.connection.cursor()
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        print("-------------------------------------------------")
        print("Nejprodávanější produkty")
        print("-------------------------------------------------")
        print("Název\t\t\t\t\t\t\t\tMnožství")
        print("-------------------------------------------------")
        for result in results:
            print("{:<30}{:>10}".format(result[0], int(result[1])))
        print("-------------------------------------------------")
        self.connection = config.close_connection()

    def view_objdenavky_zakazniku(self):
        """
        Výpis objednávek zákazníků
        :return: None
        """
        sql = "SELECT * FROM v_objdenavky_zakazniku;";
        config = Config()
        self.connection = config.get_connection()
        self.cursor = self.connection.cursor()
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        print("-------------------------------------------------")
        print("Objednávky zákazníků")
        print("-------------------------------------------------")
        print("Jméno\t\t\t\tID\t\t\tDatum objednávky")
        print("-------------------------------------------------")
        for result in results:
            print("{:<20}{:<11}{:>20}".format(result[0], int(result[1]), result[2].strftime("%Y-%m-%d %H:%M:%S")))

        print("-------------------------------------------------")
        self.connection = config.close_connection()