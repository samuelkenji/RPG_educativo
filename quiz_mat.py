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
    global lista
    op_op, op_res = random.choice(operacoes_dificil)
    n1 = random.randint(1, 50)
    n2 = random.randint(1, 25)
    quest = '{}{}{}'.format(n1, op_op, n2)
    res = op_res(n1, n2)
    lista.insert(0, quest)
    lista.insert(1, res)

def final():
    print('O Mestre --> Parece que nosso visitante é mais esperto do que imaginávamos!')
    print('O Mestre --> Já que você é tão inteligente, que tal se eu ser seu adversário?')

def chefe_facil():
    global lista
    op_op, op_res = random.choice(operacoes_facil)
    n1 = random.randint(100, 500)
    n2 = random.randint(100, 500)
    if n1 > n2:
        quest = '{}{}{}'.format(n1, op_op, n2)
        res = op_res(n1, n2)
    else:
        quest = '{}{}{}'.format(n2, op_op, n1)
        res = op_res(n2, n1)
    lista.insert(0, quest)
    lista.insert(1, res)

def chefe_medio():
    global lista
    op_op, op_res = random.choice(operacoes_medio)
    n1 = random.randint(10, 100)
    n2 = random.randint(10, 50)
    quest = '{}{}{}'.format(n1, op_op, n2)
    res = op_res(n1, n2)
    lista.insert(0, quest)
    lista.insert(1, res)

def chefe_dificil():
    global lista
    op_op, op_res = random.choice(operacoes_dificil)
    n1 = random.randint(25, 50)
    n2 = random.randint(10, 100)
    quest = '{}{}{}'.format(n1, op_op, n2)
    res = op_res(n1, n2)
    lista.insert(0, quest)
    lista.insert(1, res)


def quiz(pontuacao):
    print('Quanto é {}'.format(lista[0]))
    t0 = time.time()
    res_jogador = float(input('Digite a resposta: '))
    tf = time.time() - t0
    pontuacao_total = 0 + (pontuacao - tf)
    if lista[1] == res_jogador:
        print('Resposta certa!')
        time.sleep(1)
        pontuacao_total = 0 + (pontuacao - tf)
    else:
        print('Resposta errada')
        time.sleep(1)
        pontuacao_total = 0
    lista.insert(2, pontuacao_total)


def facil(pontuacao_final):
    cont=0
    while True:
        for _ in range(5):
            print('O próximo adversário se aproxima')
            time.sleep(1)
            questao_facil()
            quiz(pontuacao)
            pontuacao_final = pontuacao_final + lista[2]
        if pontuacao_final<1800+cont:
            print('Infelizemente você não foi capaz de derrotar seu adversário')
            time.sleep(1)
            print('Você perdeu :(')
            time.sleep(1)
            print('Sua pontuação é de: ', int(pontuacao_final), 'pontos')
            break
        continuar = input('Deseja continuar?(s/n) ').upper()
        if continuar == 'S':
            cont += 1800
        if continuar == 'N':
            print('Sua pontuação é de: ', int(pontuacao_final), 'pontos')
            break
    final()
    chefe_facil()
    quiz(pontuacao)
    pontuacao_final = pontuacao_final + lista[2]
    if lista[2]>350:
        print('O Mestre --> NÃÃÃO! COMO EU FUI DERROTADO?!')
        print('O Mestre --> Pois bem ... você me derrotou')
        print('O Mestre --> Como recompensa irei libertá-lo')
        print('O Mestre --> Acho que não nos veremos novamente')
        print('O Mestre --> Ou talvez eu esteja enganado...')
        print('Você ganhou', int(lista[2]), 'pontos, somando', int(pontuacao_final))
    else:
        print('O Mestre --> Hahahaha você não é páreo para mim!')
        print('Sua pontuação é de: ', int(pontuacao_final), 'pontos')
        print('Você perdeu')

def medio(pontuacao_final):
    cont=0
    while True:
        for _ in range(5):
            questao_media()
            quiz(pontuacao)
            pontuacao_final = pontuacao_final + lista[2]
        if pontuacao_final<1800+cont:
            print('Infelizemente você não foi capaz de derrotar seu adversário')
            time.sleep(1)
            print('Você perdeu :(')
            time.sleep(1)
            print('Sua pontuação é de: ', int(pontuacao_final), 'pontos')
            break
        continuar = input('Deseja continuar?(s/n) ').upper()
        if continuar == 'S':
            cont += 1800
        if continuar == 'N':
            print('Sua pontuação é de: ', int(pontuacao_final), 'pontos')
            break
    chefe_medio()
    quiz(pontuacao)
    pontuacao_final = pontuacao_final + lista[2]
    if lista[2]>375:
        print('O Mestre --> NÃÃÃO! COMO EU FUI DERROTADO?!')
        print('O Mestre --> Pois bem ... você me derrotou')
        print('O Mestre --> Como recompensa irei libertá-lo')
        print('O Mestre --> Acho que não nos veremos novamente')
        print('O Mestre --> Ou talvez eu esteja enganado...')
        print('Você ganhou', int(lista[2]), 'pontos, somando', int(pontuacao_final))
    else:
        print('O Mestre --> Hahahaha você não é páreo para mim!')
        print('Sua pontuação é de: ', int(pontuacao_final), 'pontos')
        print('Você perdeu')

def dificil(pontuacao_final):
    cont=0
    while True:
        for _ in range(5):
            print('Seu adversário se aproxima')
            questao_dificil()
            quiz(pontuacao)
            pontuacao_final = pontuacao_final + lista[2]
        if pontuacao_final<1800+cont:
            print('Infelizemente você não foi capaz de derrotar seu adversário')
            time.sleep(1)
            print('Você perdeu :(')
            time.sleep(1)
            print('Sua pontuação é de: ', int(pontuacao_final), 'pontos')
            break
        continuar = input('Deseja continuar?(s/n) ').upper()
        if continuar == 'S':
            cont += 1800
        if continuar == 'N':
            print('Sua pontuação é de: ', int(pontuacao_final), 'pontos')
            break
    chefe_dificil()
    quiz(pontuacao)
    pontuacao_final = pontuacao_final + lista[2]
    if lista[2]>400:
        print('O Mestre --> NÃÃÃO! COMO EU FUI DERROTADO?!')
        print('O Mestre --> Pois bem ... você me derrotou')
        print('O Mestre --> Como recompensa irei libertá-lo')
        print('O Mestre --> Acho que não nos veremos novamente')
        print('O Mestre --> Ou talvez eu esteja enganado...')
        print('Você ganhou', int(lista[2]), 'pontos, somando', int(pontuacao_final))
    else:
        print('O Mestre --> Hahahaha você não é páreo para mim!')
        print('Sua pontuação é de: ', int(pontuacao_final), 'pontos')
        print('Você perdeu')

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
    print('--> O Mestre: Então vamos à batalha!')
    time.sleep(0.5)

def regras():
    regras = ('RULES:\n'
        '#1- NÃO É PERMITIDO O USO DE CALCULADORAS;\n'
        '#2- OS OPONENTES DEVERÃO SER DERROTADOS ATRAVÉS DE EXPRESSÕES MATEMÁTICAS;\n'
        '#3- QUANTO MENOR FOR O TEMPO DE RESPOSTA, MAIS PONTOS SERÃO ADQUIRIDOS;\n'
        '#4- HÁ 3 NÍVEIS DE DIFICULDADE (FÁCIL, MÉDIO E DIFÍCIL);\n'
        '#6- O JOGO PODE SER JOGADO EM ATÉ 2 PESSOAS;\n'
        '#7- AS RODADAS SERÃO RÁPIDAS E O TEMPO TOTAL DA PARTIDA NÃO EXCEDERÁ 15 MINUTOS;\n'
        '#8- PARA PROSSEGUIR O JOGADOR DEVERÁ OBTER UM NÚMERO MÍNIMO DE PONTOS, CASO CONTRÁRIO, PERDERÁ!\n' 
            'OBS: A PONTUAÇÃO MÍNIMA PARA CONTINUAR É DE 1800 PONTOS\n'
        '#9- OS RECORDES DOS DESENVOLVEDORES PARA UMA RODADA (5 PERGUNTAS) SÃO:\n'
        'FÁCIL = 2492+485(chefe)   MÉDIO = 2379+445    DIFÍCIL = 2433+443\n'
        'TENTE SUPERÁ-LOS!\n'
            'OBS: A PONTUÇÃO MÁXIMA É 2500 (mas duvido você conseguir)')
    print(regras)
    print()

def main():
    regras()
    #hist()
    dif()


main()
