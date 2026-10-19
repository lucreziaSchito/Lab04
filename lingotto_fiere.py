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
        self.__dictStand = {}
        self.__dictEspositori = {}

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
                    if len(line) == 5 :
                        if line[4].isdigit() :
                            s = PreseElettriche(line[0], line[1], line[2], line[3], line[4])
                        else :
                            s = Premium(line[0], line[1], line[2], line[3], line[4])
                    else :
                        s = Stand(line[0], line[1], line[2], line[3])
                    self.__dictStand[line[0]] = s
                elif line[0][:2] == "ES" :
                    e = Espositore(line[0], line[1], line[2])
                    self.__dictEspositori[line[0]] = e
                else :
                    print("Tipologia di dato non specificata")
            fileIn.close()
        except FileNotFoundError:
            raise FileNotFoundError("Il percorso file da lei inserito non ha trovato nessuna corrispondenza")

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):  # chiave esterna
        """Associa uno stand a un espositore"""
        # TODO
        if codice_stand not in self.__dictStand:
            raise Exception("Il codice non corrisponde a nessuno stand")
        if codice_espositore not in self.__dictEspositori:
            raise Exception("Il codice non corrisponde a nessun'espositore")
        for s in self.__dictStand.values():
            if s.idEspositore == codice_espositore:
                raise Exception(f"L'espositore {codice_espositore} è già associato allo stand {s.codice_stand}.")
        if self.__dictStand[codice_stand].idEspositore is None:
            self.__dictStand[codice_stand].idEspositore = codice_espositore
        else :
            raise Exception("Lo stand da lei inserito non è disponibile")


    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO
        # facciamo scorrere il ciclo tra i valori del dizionario : gli oggetti
        for espositore in self.__dictEspositori.values():
            standAssegnato = None # variabile flag dove andrò a memorizzare la corrispondenza se trovata
            for cod_stand in self.__dictStand :
                if self.__dictStand[cod_stand].idEspositore is not None:
                # il controllo serve per assicurarci che lo stand non sia vuoto (None) prima di confrontarlo con il nostro oggetto espositore
                    stand = self.__dictStand[cod_stand]
                    espositore_dello_stand = self.__dictEspositori[stand.idEspositore]
                    # ho trovato il collegamento tra stand ed espositore per il confronto con eq
                    if espositore == espositore_dello_stand:
                        standAssegnato = cod_stand
                        break #interrompiamo il ciclo, abbiamo trovato la corrispondenza
            if standAssegnato is not None:
                print(espositore, "associato allo stand", standAssegnato)
            else :
                print(espositore)


    def stand_ordinati_per_prezzo(self):    #polimorfismo
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
        return sorted(self.__dictStand.values())
    # abbiamo sovrasvritto il metodo di confronto __lt__ di Object() in modo tale che questo metodo restituisca una
    # lista di stand ordinati per prezzo finale crescente