class paises:
    def __init__(self,nombre,superficie,altura, nominal):
        self.__nombre=nombre
        self.__superficie = superficie
        self.__altura=altura
        self.__nominal=nominal
    def info(self):
        return f"{self.__nombre} {self.__superficie} {self.__altura} {self.nominal}"
    
    def getNombre(self):
        return self.__nombre
    
    def getSuperficie(self):
        return self.__superficie
    
    def getAltura(self):
        return self.__altura
    
    def getNominal(self):
        return self.__nominal 