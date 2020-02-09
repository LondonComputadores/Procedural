class Pessoa:
    def __init__(self, *filhos, nome=None, idade=36):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá! {id(self)}'

if __name__ == '__main__':
    alex = Pessoa(nome='Ahlex')
    london = Pessoa(alex, nome='London')
    print(Pessoa.cumprimentar(london))
    print(id(alex))
    print(alex.cumprimentar())
    print(alex.nome)
    alex.nome = 'Alexandre'
    print(alex.nome)
    print(alex.idade)
    for filho in london.filhos:
        print(filho.nome)