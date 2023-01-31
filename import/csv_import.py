import pandas as pd
from config_database.config import Config
class CSV_Import():
    def __init__(self):
        self.connection = None

    def csv_import(self, nazev_souboru, nazev_tabulky):
        """
        Importuje do tabulky z csv souboru
        :param nazev_souboru: název souboru
        :param nazev_tabulky: název tabulky
        :return: None
        """
        imp = pd.read_csv(nazev_souboru + ".csv")
        conn = self.connection = Config.get_connection()
        imp.to_sql(
            name=nazev_tabulky,
            con=conn,
            if_exists='append',
            index=False
        )
        self.connection = Config.close_connection()