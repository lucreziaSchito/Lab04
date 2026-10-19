from stand import Stand

class Premium(Stand) :
    def __init__(self, idStand, superficie, padiglione, prezzo, posizione):
        super().__init__(idStand, superficie, padiglione, prezzo)
        #self.prezzo = prezzo*1.30  --> modifico il prezzo in un metodo a parte
        self.__posizione = posizione

    # OVERRIDING

    def prezzo_finale(self):
        return self.prezzo*1.30

    def __str__(self):
        if self.idEspositore is None:
            return f"{self.idStand}: Stand Premium | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.prezzo_finale():.2f}€ - Posizione:{self.__posizione} - Disponibile"
        else:
            return f"{self.idStand}: Stand Premium | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.prezzo_finale():.2f}€ - Posizione:{self.__posizione} - Espositore: {self.idEspositore}"