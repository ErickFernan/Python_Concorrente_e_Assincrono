import multiprocessing


def depositar(saldo):
    for _ in range(10_000):
        saldo.value = saldo.value + 1

def sacar(saldo):
    for _ in range(10_000):
        saldo.value = saldo.value - 1

def realizar_transacoes(saldo):
    pc1 = multiprocessing.Process(target=depositar, args=(saldo,))
    pc2 = multiprocessing.Process(target=sacar, args=(saldo,))

    pc1.start()
    pc2.start()

    pc1.join()
    pc2.join()


if __name__ == '__main__':
    saldo = multiprocessing.Value('i', 100)

    print(f'Saldo nicial: {saldo.value}')

    for _ in range(10):
        realizar_transacoes(saldo)

    print(f'Saldo final: {saldo.value}')


"""
Saldo nicial: 100
Saldo final: -2782
Por conta das race conditions
"""