import time
import random
import operator

pontuacao = 500
pontuacao_final = 0

lista = []

operacoes_facil = [
    ('+', operator.add),
    ('-', operator.sub)
]

operacoes_medio = [
    ('-', operator.sub),
    ('*', operator.mul),
]

operacoes_dificil = [
    ('*', operator.mul),
]


def questao_facil():
    global lista
    op_op, op_res = random.choice(operacoes_facil)
    n1 = random.randint(1, 20)
    n2 = random.randint(1, 20)
    if n1 > n2:
        quest = '{}{}{}'.format(n1, op_op, n2)
        res = op_res(n1, n2)
    else:
        quest = '{}{}{}'.format(n2, op_op, n1)
        res = op_res(n2, n1)
    lista.insert(0, quest)
    lista.insert(1, res)


def questao_media():
    global lista
    op_op, op_res = random.choice(operacoes_medio)
    n1 = random.randint(1, 50)
    n2 = random.randint(1, 10)
    quest = '{}{}{}'.format(n1, op_op, n2)
    res = op_res(n1, n2)
    lista.insert(0, quest)
    lista.insert(1, res)


def questao_dificil():
    op_op, op_res = random.choice(operacoes_dificil)
    n1 = random.randint(1, 50)
    n2 = random.randint(1, 25)
    quest = '{}{}{}'.format(n1, op_op, n2)
    res = op_res(n1, n2)
    lista.insert(0, quest)
    lista.insert(1, res)
    print(res)


def quiz(pontuacao):
    print('Quanto é {}'.format(lista[0]))
    t0 = time.time()
    res_jogador = float(input('Digite a resposta: '))
    tf = time.time() - t0
    pontuacao_total = 0 + (pontuacao - tf)
    if lista[1] == res_jogador:
        print('Resposta certa!')
        pontuacao_total = 0 + (pontuacao - tf)
    else:
        print('Resposta errada')
        pontuacao_total = 0
    lista.insert(2, pontuacao_total)


def facil(pontuacao_final):
    while True:
        for _ in range(5):
            questao_facil()
            quiz(pontuacao)
            pontuacao_final = pontuacao_final + lista[2]
        cont = input('Deseja continuar?(s/n) ').upper()
        if cont == 'N':
            print('Sua pontuação é de: ', int(pontuacao_final), 'pontos')
            break


def medio(pontuacao_final):
    while True:
        for _ in range(5):
            questao_media()
            quiz(pontuacao)
            pontuacao_final = pontuacao_final + lista[2]
        cont = input('Deseja continuar?(s/n) ').upper()
        if cont == 'N':
            print('Sua pontuação é de: ', int(pontuacao_final), 'pontos')
            break


def dificil(pontuacao_final):
    while True:
        for _ in range(5):
            questao_dificil()
            quiz(pontuacao)
            pontuacao_final = pontuacao_final + lista[2]
        cont = input('Deseja continuar?(s/n) ').upper()
        if cont == 'N':
            print('Sua pontuação é de: ', int(pontuacao_final), 'pontos')
            break


def dif():
    dificuldade = int(input('Selecione a dificuldade:\n1 - Fácil\n2 - Médio\n3 - Difícil'))
    while dificuldade < 1 or dificuldade > 3:
        dificuldade = int(input('Selecione a dificuldade:\n1 - Fácil\n2 - Médio\n3 - Difícil'))
    if dificuldade == 1:
        facil(pontuacao_final)
    elif dificuldade == 2:
        medio(pontuacao_final)
    elif dificuldade == 3:
        dificil(pontuacao_final)

def hist():
    print('Você acorda num salão escuro')
    time.sleep(3)
    print('Sua cabeça está muito confusa')
    time.sleep(3)
    print('--> ???: Parece que nosso convidado finalmente acordou!')
    time.sleep(3)
    print('Vários holofotes acendem ao mesmo tempo, ofuscando sua vista')
    time.sleep(3)
    print('--> ???: Seja bem-vindo ao maior e melhor jogo de toda a história!')
    time.sleep(3)
    print('--> ???: Eu imagino que devem ter muitas perguntas passando na sua cabeça')
    time.sleep(3)
    print('--> ???: Mas não se preocupe, a única coisa que precisa saber sobre mim é que você pode me chamar de O Mestre')
    time.sleep(3)
    print('--> O Mestre: Sobre onde você está ... receio que não posso dizer')
    time.sleep(3)
    print('--> O Mestre: Porém, eu posso afirmar que esse é o jogo mais real que existe')
    time.sleep(3)
    print('--> O Mestre: Como eu sei que você já conhece as regras, não irei ser repetitivo')
    time.sleep(3)
    print('--> O Mestre: Então vamos ao jogo!')
    time.sleep(0.5)

def main():
    #hist()
    dif()


main()
