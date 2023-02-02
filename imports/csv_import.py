from config_database.config import Config
import csv

class CSV_Import():
    def __init__(self):
        self.connection = None
        self.cursor = None

    def csv_import(self, nazev_souboru, nazev_tabulky):
        """
        Importuje do tabulky z csv souboru
        :param nazev_souboru: název souboru
        :param nazev_tabulky: název tabulky
        :return: None
        """
        config = Config()
        self.connection = config.get_connection()
        self.cursor = self.connection.cursor()
        # Otevření souboru CSV a načtení dat
        with open("bin/" + nazev_souboru, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            query = "INSERT INTO " + nazev_tabulky + " (" + ",".join(header) + ") VALUES (" + ",".join(
                ["%s"] * len(header)) + ");"
            for data in reader:
                self.cursor.execute(query, data)
        self.connection.commit()
        self.connection = config.close_connection()