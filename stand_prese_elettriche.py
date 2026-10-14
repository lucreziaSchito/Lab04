from stand import Stand

class PreseElettriche(Stand) :
    def __init__(self, idStand, superficie, padiglione, prezzo, numPreseElettriche) :
        super().__init__(idStand, superficie, padiglione)
        self.prezzo = prezzo*(1 + 0.07*numPreseElettriche)
        self.numPreseElettriche = numPreseElettriche