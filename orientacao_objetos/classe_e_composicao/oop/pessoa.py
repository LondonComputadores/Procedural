class Pessoa:
    olhos=2

    def __init__(self, *filhos, nome=None, idade=36):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá! {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributo_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

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
    london.sobrenome = 'Computadores'
    del london.filhos
    print(london.__dict__)
    print(alex.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print('Name: {}',format(alex))
    print(alex.olhos)
    print(id(Pessoa.olhos), id(alex.olhos), id(london.olhos))
    print(Pessoa.metodo_estatico(), london.metodo_estatico())
    print(Pessoa.nome_e_atributo_de_classe(), alex.nome_e_atributo_de_classe())
