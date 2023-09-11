import multiprocessing
import time
import ctypes


def funcao1(value, status):
    if status.value: # o '.value' é para acessar o valor da variável com o ctypes
        resultado = value.value + 10
        status.value = False
    else:
        resultado = value.value + 20
        value.value = 200 # altera na principal
        status.value = True

    print(f'O resultado da função 1 é {resultado}') # 120
    time.sleep(0.001)

def funcao2(value, status):
    if status.value:
        resultado = value.value + 30
        status.value = False
    else:
        resultado = value.value + 40
        value.value = 400 # altera na principal
        status.value = True

    print(f'O resultado da função 2 é {resultado}') # 230
    time.sleep(0.001)

def main():
    val = multiprocessing.Value('i', 100) # value do tipo inteiro inicializado com valor 100
    stat = multiprocessing.Value(ctypes.c_bool, False) # value do tipo bool inicializado com valor False

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