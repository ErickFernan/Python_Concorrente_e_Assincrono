import multiprocessing
import random


def ping(queue):
    queue.put('Teste')

def pong(queue):
    msg = queue.get()
    print(f'{msg} Testado')

def main():
    queue = multiprocessing.JoinableQueue() # Pode-se usar o Queue tb, mas n teremos os métodos task_done() e join()

    p1 = multiprocessing.Process(target=ping, args=(queue,))
    p2 = multiprocessing.Process(target=pong, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == '__main__':
    main()


# Queue pode ser melhor que o pipe pois possuimos um maior controle e pq tem um maior compatibilidade com threads
