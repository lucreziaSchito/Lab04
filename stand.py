class Stand :
    def __init__(self, idStand, superficie, padiglione, prezzo):
        self.__idStand = idStand
        self.__superficie = float(superficie)
        self.__padiglione = padiglione
        self.__prezzo = float(prezzo)
        self.__idEspositore = None

    @property
    def idEspositore(self):
        return self.__idEspositore
    @idEspositore.setter
    def idEspositore(self, id):
        self.__idEspositore = id

    def prezzo_finale(self):  #polimorfismo
        return self.__prezzo

    def __str__(self):
        if self.idEspositore is None:
            return f"{self.__idStand}: Stand base | {self.__superficie} mq - Padiglione {self.__padiglione} - Prezzo {self.prezzo_finale():.2f}€ - Disponibile"
        # stamperà il risultato con 2 cifre decimali grazie al :.2f
        else :
            return f"{self.__idStand}: Stand base | {self.__superficie} mq - Padiglione {self.__padiglione} - Prezzo {self.prezzo_finale():.2f}€ - Espositore: {self.__idEspositore}"


    def __eq__(self, other):
        if isinstance(other, Stand):
            return self.__idStand == other.__idStand
        return False

    def __lt__(self, other):
    # permette a sorted() e .sort() di ordinare gli stand per prezzo crescente
        if isinstance(other, Stand):
            return self.prezzo_finale() < other.prezzo_finale()
        else :
            raise Exception("il confronto non è effettuabile")