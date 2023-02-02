from datetime import datetime
from config_database.config import Config

class Commands():
    def __init__(self):
        self.connection = None
        self.cursor = None

    def insert_zakaznik(self, jmeno, email, ulice, mesto, telefon):
        """
        Vloží zákazníka do databáze
        :param jmeno: jméno
        :param email: email
        :param ulice: ulice
        :param mesto: mesto
        :param telefon: telefon
        :return: None
        """
        config = Config()
        self.connection = config.get_connection()
        self.cursor = self.connection.cursor()
        self.cursor.execute("START TRANSACTION")
        self.cursor.execute("INSERT INTO zakaznik (jmeno, email, ulice, mesto, telefon) VALUES (%s, %s, %s, %s, %s)",
                            (jmeno, email, ulice, mesto, telefon))
        self.cursor.execute("COMMIT")
        self.connection = config.close_connection()

    def insert_produkt(self, nazev, cena, zasoba, je_aktivni):
        """
        Vloží produkt do databáze
        :param nazev: název
        :param cena: cena
        :param zasoba: počet zásob
        :param je_aktivni: aktivní
        :return: None
        """
        config = Config()
        self.connection = config.get_connection()
        self.cursor = self.connection.cursor()
        self.cursor.execute("START TRANSACTION")
        self.cursor.execute("INSERT INTO produkt (nazev, cena, zasoba, je_aktivni) VALUES (%s, %s, %s, %s)",
                            (nazev, cena, zasoba, je_aktivni))
        self.cursor.execute("COMMIT")
        self.connection = config.close_connection()

    def insert_objednavka(self, zakaznik_id, datum_objednavky):
        """
        Vloží objednávku do databáze
        :param zakaznik_id: zákazník
        :param datum_objednavky: datum objednávky
        :return: None
        """
        config = Config()
        self.connection = config.get_connection()
        self.cursor = self.connection.cursor()
        self.cursor.execute("START TRANSACTION")
        self.cursor.execute("INSERT INTO objednavka (zakaznik_id, datum_objednavky) VALUES (%s, %s)",
                            (zakaznik_id, datum_objednavky))
        self.cursor.execute("COMMIT")
        self.connection = config.close_connection()

    def insert_objednani_polozky(self, produkt_id, mnozstvi):
        """
        Vloží objednávku do databáze
        :param produkt_id: prodkut
        :param mnozstvi: množství
        :return: None
        """
        config = Config()
        self.connection = config.get_connection()
        self.cursor = self.connection.cursor()

        self.cursor.execute("START TRANSACTION")
        self.cursor.execute("INSERT INTO objednani_polozky (produkt_id, mnozstvi) VALUES (%s, %s)",
                            (produkt_id, mnozstvi))
        self.cursor.execute("COMMIT")
        self.connection = config.close_connection()

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

    def insert_kategorie_produktu(self, produkt_id, kategorie_id):
        """
        Vloží kategorii produktu do databáze
        :param produkt_id: produkt
        :param kategorie_id: kategorie
        :return: None
        """
        config = Config()
        self.connection = config.get_connection()
        self.cursor = self.connection.cursor()
        self.cursor.execute("START TRANSACTION")
        self.cursor.execute("INSERT INTO kategorie_produktu (produkt_id, kategorie_id) VALUES (%s, %s)", (produkt_id, kategorie_id))
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
        self.cursor.execute("START TRANSACTION")
        self.cursor.execute("UPDATE objednani_polozky SET mnozstvi = %s WHERE objednavka_id = %s and produkt_id = %s",
                       (mnozstvi, objednavka_id, produkt_id))
        self.cursor.execute("COMMIT")
        self.connection = config.close_connection()

    def select_pro_report(self):
        sql = "SELECT zakaznik.mesto, SUM(objednani_polozky.mnozstvi * produkt.cena) AS soucet_nakupu " \
              "FROM zakaznik " \
              "JOIN objednavka ON zakaznik.id = objednavka.zakaznik_id " \
              "JOIN objednani_polozky ON objednavka.id = objednani_polozky.objednavka_id " \
              "JOIN produkt ON produkt.id = objednani_polozky.produkt_id " \
              "GROUP BY zakaznik.mesto"

        config = Config()
        self.connection = config.get_connection()
        self.cursor.execute(sql)
        result = self.cursor.fetchall()

        print("-------------------------------------------------")
        print("\t\tSouhrnný report")
        print("-------------------------------------------------")
        print("Město\t\tSoučet nákupů")
        print("-------------------------------------------------")

        for row in result:
            print("{}\t\t{}".format(row['mesto'], row['soucet_nakupu']))

        print("-------------------------------------------------")
        self.connection = config.close_connection()