from stand import Stand

class Premium(Stand) :
    def __init__(self, idStand, superficie, padiglione, prezzo, posizione):
        super().__init__(idStand, superficie, padiglione)
        self.prezzo = prezzo*1.30
        self.posizione = posizione