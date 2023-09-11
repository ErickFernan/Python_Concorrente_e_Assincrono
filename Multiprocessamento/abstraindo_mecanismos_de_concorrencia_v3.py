import time

# from concurrent.futures.thread import ThreadPoolExecutor as Executor
from concurrent.futures.process import ProcessPoolExecutor as Executor

def processar():
    print('[',end='', flush=True)
    for _ in range(1, 11):
        print('#', end='', flush=True)
        time.sleep(1)
    print(']', end='', flush=True)

    return 42 # apenas para mostrar o funcionamento

if __name__ == '__main__':
    with Executor() as executor:
        future = executor.submit(processar) # caso  tivesse parametros extras é só adicionar (processar, outro)

    print(f'o retornor foi: {future.result()}')
    print(future)