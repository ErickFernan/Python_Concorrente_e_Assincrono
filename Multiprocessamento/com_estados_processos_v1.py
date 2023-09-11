import multiprocessing
import time


def funcao1(value, status):
    if status:
        resultado = value + 10
        status = False
    else:
        resultado = value + 20
        value = 200 # não altera na principal
        status = True

    print(f'O resultado da função 1 é {resultado}') # 120
    time.sleep(0.001)

def funcao2(value, status):
    if status:
        resultado = value + 30
        status = False
    else:
        resultado = value + 40
        value = 400 # não altera na principal
        status = True

    print(f'O resultado da função 2 é {resultado}') # 140
    time.sleep(0.001)

def main():
    val = 100
    stat = False

    p1 = multiprocessing.Process(target=funcao1, args=(val,stat))
    p2 = multiprocessing.Process(target=funcao2, args=(val,stat))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == "__main__":
    main()


# Observe que apesar de estar recebendo as mesmas variáveis as alterações feitas em cada função não irá interferir
# no estado da outra, isso se deve pois não há compartilhamento de memória.