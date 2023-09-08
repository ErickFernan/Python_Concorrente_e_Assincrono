import threading
import random
import time

from typing import List


class Conta:

    def __init__(self, saldo=0) -> None:
        self.saldo = saldo


def main():
    contas = criar_contas()
    total = sum(conta.saldo for conta in contas)
    print('Iniciando transferências...')

    tarefas = [
        threading.Thread(target=servicos, args=(contas, total)),
        # threading.Thread(target=servicos, args=(contas, total)),
        # threading.Thread(target=servicos, args=(contas, total)),
        # threading.Thread(target=servicos, args=(contas, total)),
        # threading.Thread(target=servicos, args=(contas, total)),
        # threading.Thread(target=servicos, args=(contas, total)),
        """
        Caso seja enviado uma lista de threads, temos o caso em qua várias threads tentam acessar o mesmo valor,
        assim sendo, varias threads podem modificar a mesma variável sem uma organização o que pode gerar
        RACE CONDITIONS. Para contornar isso faz-se necessário usar métodos de sincronização de threads.
        """
    ]

    [tarefa.start() for tarefa in tarefas]
    [tarefa.join() for tarefa in tarefas]

    print('Transferências completas.')
    valida_banco(contas, total)

def servicos(contas, total):
    for _ in range(1,10_000):
        c1, c2 = pega_duas_contas(contas)
        valor = random.randint(1,100)
        transferir(c1, c2, valor)
        valida_banco(contas, total)

def criar_contas() -> List[Conta]:
    return [
        Conta(saldo= random.randint(5_000, 10_000)),
        Conta(saldo= random.randint(5_000, 10_000)),
        Conta(saldo= random.randint(5_000, 10_000)),
        Conta(saldo= random.randint(5_000, 10_000)),
        Conta(saldo= random.randint(5_000, 10_000)),
        Conta(saldo= random.randint(5_000, 10_000))
    ]

def transferir(origem: Conta, destino: Conta, valor: int):
    if origem.saldo < valor:
        return

    origem.saldo -= valor
    time.sleep(0.001)
    destino.saldo += valor

def valida_banco(contas: List[Conta], total: int):
    atual = sum(conta.saldo for conta in contas)

    if atual != total:
        print(f'ERRO: Balanço bancário inconsistente. BRL$ {atual:.2f} vs {total:.2f}', flush=True)
    else:
        print(f'Tudo certo: Balançoa bancário consistente: BRL$ {total:.2f}', flush=True)

def pega_duas_contas(contas):
    c1 = random.choice(contas)
    c2 = random.choice(contas)

    while c1 == c2:
        c2 = random.choice(contas)

    return c1, c2

if __name__ == '__main__':
    main()

# Tempo execução real    0m11,219s
