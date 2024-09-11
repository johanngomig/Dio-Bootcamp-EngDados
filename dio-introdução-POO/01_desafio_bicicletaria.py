class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        
    def buzinar(self):
        print("Plim Plim")
        
    def parar(self):
        print("Parando bicicleta")
        print("Bicicleta parada")
        
    def correr(self):
        print("Bicicleta correndo")    
            
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"
    
caloi = Bicicleta("Preta", "Caloi", 2022, 600)

caloi.buzinar()
caloi.correr()
caloi.parar()
print(caloi.cor, caloi.modelo, caloi.ano, caloi.valor)