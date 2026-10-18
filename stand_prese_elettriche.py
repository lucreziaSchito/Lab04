from stand import Stand

class PreseElettriche(Stand) :
    def __init__(self, idStand, superficie, padiglione, prezzo, numPreseElettriche) :
        super().__init__(idStand, superficie, padiglione, prezzo)
        #self.prezzo = prezzo*(1 + 0.07*numPreseElettriche)
        self.__numPreseElettriche = numPreseElettriche

    # OVERRIDING

    def prezzo_finale(self):
        return self.__prezzo * (1 + 0.07 * self.__numPreseElettriche)

    def __str__(self):
        if self.idEspositore is None:
            return f"{self.__idStand}: Prese Extra | {self.__superficie} mq - Padiglione {self.__padiglione} - Prezzo {self.prezzo_finale():.2f}€ - Prese aggiuntive :{self.__numPreseElettriche} - Disponibile"
        else:
            return f"{self.__idStand}: Prese Extra | {self.__superficie} mq - Padiglione {self.__padiglione} - Prezzo {self.prezzo_finale():.2f}€ - Prese aggiuntiva :{self.__numPreseElettriche} - Espositore: {self.__idEspositore}"