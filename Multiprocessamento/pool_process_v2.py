import multiprocessing


def calcular(dado):
    return dado ** 2

def imprimir_nome_processo():
     print(f'Iniciando o processo com o nome {multiprocessing.current_process().name}') # unica diferença desse para o outro é q e esse "prova" que são processos diferentes

def main():
    tamanho_pool = multiprocessing.cpu_count() * 2 # Quantos processos serão criados

    print(f'Tamano da Pool: {tamanho_pool}')

    pool = multiprocessing.Pool(processes=tamanho_pool, initializer=imprimir_nome_processo) # O initializer é responsável por executar essa função para cada processo criado

    entradas = list(range(7))
    saidas = pool.map(calcular, entradas)

    print(f'Saídas: {saidas}', )

    pool.close()  # Seria o start nas threads
    pool.join()

if __name__ == '__main__':
        main()
