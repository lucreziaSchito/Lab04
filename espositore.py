class Espositore :
    def __init__(self, idEspositore, nome, cognome) :
        self.idEspositore = idEspositore
        self.__nome = nome
        self.__cognome = cognome

    def __eq__(self, other):
        if isinstance(other, Espositore) :
            return self.idEspositore == other.idEspositore
        return False

    def __str__(self) :
        return f"Espositore {self.idEspositore}: {self.__nome} {self.__cognome}"
