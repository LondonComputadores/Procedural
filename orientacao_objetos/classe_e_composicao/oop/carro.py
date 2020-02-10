"""
Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

1) Motor
2) Direção

O Motor terá a responsabilidade de controlar a velocidade!
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Metodo acelerar, que deverá incrementar a velocidade de uma unidade
3) Metodo frear que deverá decrementar a velocidade em duas unidades

A Direção terá a responsabilidade de controlar a direção. Ela oferecerá
os seguintes atributos:
1) Valor da direção com os valores possíveis: Norte,Sul,Leste,Oeste
2) Método girar_a_direita
3) Método girar_a_esquerda

             N
           O  L
            S

    Exemplo:

    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0

    #Testando a Direção

    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direção.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direção.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direção.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direção.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direção.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direção.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direção.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direção.valor
    'Norte'

    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Oeste'
"""