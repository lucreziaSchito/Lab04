class Stand :
    def __init__(self, idStand, superficie, padiglione, prezzo):
        self.__idStand = idStand
        self.__superficie = superficie
        self.__padiglione = padiglione
        self.__prezzo = prezzo
        self.idEspositore = None

    @property
    def idEspositore(self):
        return self.__idEspositore
    @idEspositore.setter
    def idEspositore(self, id):
        self.__idEspositore = id


# figlie: premium, elettrica
# polimorfismo : PREZZO