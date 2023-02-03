# DB_System

Program
---------------------
## Úvod
Úloha je řešena v prostředí Pycharm a MySQL Workbench

##Program
Aby bylo možné spustit aplikaci, je nutné mít nainstalovaný Python 3.11 a všechny potřebné knihovny.
Aplikaci je možné spustit v konzoli pomocí příkazu "python main.py". Je třeba však být v přímém adresáři. 
Poté se zobrazí uživatelské rozhraní, ve kterém je možné provádět různé operace, 
jako je import dat z csv souboru nebo zobrazení záznamu z reportu.

##Konfigurace
Konfigurace programu se provádí pomocí konfiguračního souboru ini. Tento soubor obsahuje sekci "[database]" a následující možné volby:
host: specifikuje adresu hostitele, na kterém se databáze nachází. Je možné zadat IP adresu nebo název hostitele. Výchozí hodnotou byla využita "localhost".
user: specifikuje uživatelské jméno, které se má použít pro přihlášení k databázi.
password: specifikuje heslo, které se má použít pro přihlášení k databázi.
db: specifikuje název databáze, ke které se má program připojit.

Všechny volby jsou povinné a musí být správně nastaveny pro správné fungování programu.

Databáze
---------------------
## E-R model
konceptuální model databáze se nachází v /doc/diagram.png

## Entitní integrita
Každá entita obsahuje uměle vytvořený primární klíč, označený jako id, 
který se s každým dalším záznamem inkrementuje.

## Export
V prostředí mysql workbench stačí vzít pařičné soubory s .sql příponou a spustit příkazy, jenž vytvoří databázy.
Následně lze insertovat testovací data.
Soubory s .sql příponou se nacházejí ve složce bin.
