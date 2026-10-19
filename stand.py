class Stand :
    def __init__(self, idStand, superficie, padiglione, prezzo):
        self.__idStand = idStand
        self.__superficie = float(superficie)
        self.__padiglione = padiglione
        self.__prezzo = float(prezzo)
        self.__espositoreAssegnato = None # var. di riferimento

    @property
    def espositoreAssegnato(self):
        return self.__espositoreAssegnato
    @espositoreAssegnato.setter
    def espositoreAssegnato(self, id):
        self.__espositoreAssegnato = id

    # ho implementato il metodo getter per ogni attributo della classe padre per l'ereditarietà delle classi figlie
    @property
    def idStand(self):
        return self.__idStand
    @property
    def superficie(self):
        return self.__superficie
    @property
    def padiglione(self):
        return self.__padiglione
    @property
    def prezzo(self):
        return self.__prezzo


    def prezzo_finale(self):  #polimorfismo
        return self.prezzo   # sto usando la property

    def __str__(self):
        if self.espositoreAssegnato is None:
            return f"{self.__idStand}: Stand Base | {self.__superficie} mq - Padiglione {self.__padiglione} - Prezzo {self.prezzo_finale():.2f}€ - Disponibile"
        # stamperà il risultato con 2 cifre decimali grazie al :.2f
        else :
            return f"{self.__idStand}: Stand Base | {self.__superficie} mq - Padiglione {self.__padiglione} - Prezzo {self.prezzo_finale():.2f}€ - {self.__espositoreAssegnato}"


    def __lt__(self, other):
    # sto sovrascrivendo l'algoritmo di confronto per permettere a sorted()
    # di ordinare gli stand per prezzo CRESCENTE
        if isinstance(other, Stand):
            return self.prezzo_finale() < other.prezzo_finale()
        else :
            raise Exception("il confronto non è effettuabile")