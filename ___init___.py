from getallfiles import GetAll
from pathlib import Path

def main(username, password):
    mypath = str(Path(__file__).parent.absolute()) + "\\texto\\"
    GetAll(mypath)

if __name__ == "__main__":
    username = "lupadocidadao"
    password = "esaniagro12"
    main(username, password)