from stand import Stand

class PreseElettriche(Stand) :
    def __init__(self, idStand, superficie, padiglione, prezzo, numPreseElettriche) :
        super().__init__(idStand, superficie, padiglione, prezzo)
        #self.prezzo = prezzo*(1 + 0.07*numPreseElettriche)  --> modifico il prezzo in un metodo a parte
        self.__numPreseElettriche = int(numPreseElettriche)

    # OVERRIDING

    def prezzo_finale(self):
        return self.prezzo * (1 + 0.07 * self.__numPreseElettriche)

    def __str__(self):
        if self.idEspositore is None:
            return f"{self.idStand}: Prese Extra | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.prezzo_finale():.2f}€ - Prese aggiuntive :{self.__numPreseElettriche} - Disponibile"
        else:
            return f"{self.idStand}: Prese Extra | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.prezzo_finale():.2f}€ - Prese aggiuntiva :{self.__numPreseElettriche} - Espositore: {self.idEspositore}"