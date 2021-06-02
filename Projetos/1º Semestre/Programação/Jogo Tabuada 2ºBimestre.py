import random
import time


roupas = ["calças", "camisas", "meias", "tênis"]
numeros = [1,2,3,4,5,6,7,8,9,10,11,12]

def intro () :
    print("Esse é um jogo de tabuada")
    time.sleep(3)
    print("Você deverá acertar o número de combinações entre roupas")
    time.sleep(3)
    print("Você responderá 10 perguntas")
    time.sleep(3)
    print("Se a reposta estiver errada, irá aparecer a correção dela")
    time.sleep(3)
    print("Vamos lá!!")
    time.sleep(2)
    
def sortear_roupas ():
    roupa = random.choice(roupas) 
    return roupa

def sortear_numeros ():
    num = random.choice(numeros)
    return num

def comb (n1,r1,n2,r2):

    print("Você possui {} {} e {} {}.".format(n1,r1,n2,r2))

def entrada ():
    resp = int(input("Quantas combinações de roupas são possíveis? "))
    while resp < 0 :
        resp = int(input("Digite um valor válido: "))
        return resp        
    return resp


def validacao (resp):
    while resp < 0 :
        resp = int(input("Digite um valor válido: "))
        return resp


def resposta (x,y):
    rc = x*y
    return rc


def pontos (rc,resp):
    if rc != resp:
        print("Resposta errada, a certa é {}".format(rc))
    else :
        print("Parabéns, resposta certa !!")
    time.sleep(3)




        

def main() :
    intro()
    for i in range (10):
        n1 = sortear_numeros()
        n2 = sortear_numeros()
        r1 = sortear_roupas()
        r2 = sortear_roupas()
        comb (n1,r1,n2,r2)
        resp = entrada()
        rc = resposta(n1,n2)
        pontos(rc,resp)
   

    
main()
    
