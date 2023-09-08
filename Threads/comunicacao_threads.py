import time
import colorama

from threading import Thread
from queue import Queue


def gerador_de_dados(queue):
    for i in range (1, 11):
        print(colorama.Fore.GREEN + f'Dados {i} gerado', flush=True)  # é usado para garantir que os dados impressos com print sejam exibidos imediatamente, em vez de aguardar a quebra de linha ou o preenchimento do buffer de saída.
        time.sleep(2)
        queue.put(i)

def consumidor_de_dados(queue):
    while queue.qsize() > 0:  # usada para obter o tamanho atual da fila, ou seja, o número de elementos na fila
        valor = queue.get()  # A função get() permite que você remova e obtenha o próximo item na fila, bloqueando o programa se a fila estiver vazia até que um item esteja disponível (ou até que seja definido um limite de tempo para o bloqueio).
        print(colorama.Fore.RED + f'Dado {valor * 2} processado.', flush=True)
        time.sleep(1)
        queue.task_done() # é usado para sinalizar a conclusão de tarefas em uma fila implementada com a biblioteca queue


if __name__ == '__main__':
    print(colorama.Fore.WHITE + 'Sistema iniciado', flush=True)
    queue = Queue()
    th1 = Thread(target=gerador_de_dados, args=(queue,))
    th2 = Thread(target=consumidor_de_dados, args=(queue,))

    th1.start()
    th1.join()

    th2.start()
    th2.join()
