from stand import Stand

class Premium(Stand) :
    def __init__(self, idStand, superficie, padiglione, prezzo, posizione):
        super().__init__(idStand, superficie, padiglione, prezzo)
        #self.prezzo = prezzo*1.30
        self.__posizione = posizione

    # OVERRIDING

    def prezzo_finale(self):
        return self.__prezzo*1.30

    def __str__(self):
        if self.idEspositore is None:
            return f"{self.__idStand}: Stand Premium | {self.__superficie} mq - Padiglione {self.__padiglione} - Prezzo {self.prezzo_finale():.2f}€ - Posizione:{self.__posizione} - Disponibile"
        else:
            return f"{self.__idStand}: Stand Premium | {self.__superficie} mq - Padiglione {self.__padiglione} - Prezzo {self.prezzo_finale():.2f}€ - Posizione:{self.__posizione} - Espositore: {self.__idEspositore}"