from csv import reader
from stand import Stand
from espositore import Espositore
from stand_premium import Premium
from stand_prese_elettriche import PreseElettriche


class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.__nome = nome
        self.__listaStand = []
        self.__listaEspositori = []

    """Aggiungere setter e getter se necessari"""
    # TODO
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        # TODO
        try :
            fileIn = open(file_path, "r")
            CsvReader = reader(fileIn)
            for line in CsvReader:
                if line[0][:2] == "ST" :
                    if line[4].isdigit() :
                        s = PreseElettriche(line[0], line[1], line[2], line[3], line[4])
                    elif line[4].isalpha() :
                        s = Premium(line[0], line[1], line[2], line[3], line[4])
                    else :
                        s = Stand(line[0], line[1], line[2], line[3])
                    self.__listaStand.append(s)
                elif line[0][:2] == "ES" :
                    e = Espositore(line[0], line[1], line[2])
                    self.__listaEspositori.append(e)
                else :
                    print("Tipologia di dato non specificata")
            fileIn.close()
        except FileNotFoundError:
            raise FileNotFoundError("Il percorso file da lei inserito non ha trovato nessuna corrispondenza")

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):  # chiave esterna
        """Associa uno stand a un espositore"""
        # TODO

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):    #polimorfismo
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
