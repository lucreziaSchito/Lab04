from csv import reader

from stand import Stand


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
                    s = Stand(line[0], line[1], line[2], line[3])


############################################################################

            fileIn.close()
        except FileNotFoundError:
            raise FileNotFoundError("Il percorso file da lei inserito non ha trovato nessuna corrispondenza")

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):  # chiave esterna
        """Associa uno stand a un espositore"""
        # TODO

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
