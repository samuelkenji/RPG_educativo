from time import time
import random
import operator

pontuacao=500
pontuacao_final=0

lista=[]

operacoes_facil=[
    ('+', operator.add),
    ('-', operator.sub)
]

operacoes_medio=[
    ('+', operator.add),
    ('-', operator.sub),
    ('*', operator.mul),
    ('/', operator.floordiv),
]

operacoes_dificil=[
    ('*', operator.mul),
    ('/', operator.floordiv),
]

def questao_facil():
    global lista
    op_op, op_res=random.choice(operacoes_facil)
    n1=random.randint(1,20)
    n2=random.randint(1,20)
    if n1>n2:
        quest = '{}{}{}'.format(n1, op_op, n2)
        res=op_res(n1,n2)
    else:
        quest = '{}{}{}'.format(n2,op_op,n1)
        res=op_res(n2,n1)
    lista.insert(0,quest)
    lista.insert(1,res)


def questao_media():
    global lista
    op_op, op_res = random.choice(operacoes_medio)
    n1 = random.randint(1, 50)
    n2 = random.randint(1, 10)
    quest = '{}{}{}'.format(n1, op_op, n2)
    res = op_res(n1, n2)
    return quest, res

def questao_dificil():
    op_op, op_res = random.choice()
    n1 = random.randint(1, 50)
    n2 = random.randint(1, 25)
    quest = '{}{}{}'.format(n1, op_op, n2)
    res = op_res(n1, n2)
    print (res)
    return quest, res

def quiz(pontuacao):
    print('Quanto é {}'.format(lista[0]))
    t0=time()
    res_jogador=int(input('Digite a resposta: '))
    tf=time()-t0
    pontuacao_total=0+(pontuacao-tf)
    if lista[1]==res_jogador:
        print('Resposta certa!')
    else:
        print('Resposta errada')
    lista.insert(2, pontuacao_total)

def facil(pontuacao_final):
    for _ in range(2):
        questao_facil()
        quiz(pontuacao)
        pontuacao_final=pontuacao_final+lista[2]
        print('Sua pontuação é de: ',int(pontuacao_final),'pontos')

def medio():
    for _ in range(2):
        questao_media()
        quiz(quest, res, pontuacao_total)


def dificil():
    for _ in range(3):
        questao_dificil()
        quiz(quest, res, pontuacao_total)

def menu():
    print('Bem-vindo ao jooj')
    dificuldade=int(input('Selecione a dificuldade:\n1 - Fácil\n2 - Médio\n3 - Difícil'))
    while dificuldade<1 or dificuldade>3:
        dificuldade = int(input('Selecione a dificuldade:\n1 - Fácil\n2 - Médio\n3 - Difícil'))
    if dificuldade==1:
        facil(pontuacao_final)
    elif dificuldade==2:
        medio()
    elif dificuldade==3:
        dificil()

def main():
    menu()

main()
