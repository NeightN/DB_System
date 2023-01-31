from database_commands.commands import Commands

def main():
    command = Commands()
    kategorie = "fgh"
    command.insert_kategorie(kategorie)

if __name__ == '__main__':
    main()

