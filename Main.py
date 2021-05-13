# intefraz alcancia: define como deben comportarse todas las alcancias
class IAlcancia:
    def ahorrar(self, valor):
        """ metodo vacio
        """
        pass
    def entregar_dinero(self):
        """ metodo vacio
        """
        pass

# Clase abstracta Alcancia: implementa como ahorrar, pero no como entrar el dinero.
class Alcancia(IAlcancia):  
    valorahorrado = 0     
    def __init__(self):
        self.valorahorrado = 0
    def ahorrar(self,valor):
        self.valorahorrado += valor
    def entregar_dinero(self):
        """
        """
        pass

class Marranito(Alcancia):
    def entregar_dinero(self):
        print ("Romper el marranito 😥, habia " + str( self.valorahorrado ))

class AlcanciaCarton(Alcancia):
    def entregar_dinero(self):
        print ("abri la alcancia! , habia " + str( self.valorahorrado))


marranito = Marranito()
marranito.ahorrar(100)
marranito.ahorrar(100)
marranito.ahorrar(100)
marranito.ahorrar(100)
marranito.ahorrar(100)
marranito.entregar_dinero()
carton = AlcanciaCarton()
carton.ahorrar(1000)
carton.ahorrar(100)
carton.entregar_dinero()