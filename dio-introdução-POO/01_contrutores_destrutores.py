class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Iniciando a classe.....")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
        
    def __del__(self):
        print("Removendo a instância da classe......")
        
    def falar(self):
        print("Au au")
        
def criar_cachorro():
    c = Cachorro("Zeus", "branco e preto", False)
    print(c)
        
c = Cachorro("Chappie", "amarelo")
c.falar()


print("Olá Mundo")

del c

print("Olá Mundo")
print("Olá Mundo")
print("Olá Mundo")
print("Olá Mundo")
print("Olá Mundo")

#criar_cachorro()       
    