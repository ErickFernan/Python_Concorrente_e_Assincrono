import multiprocessing


def calcular(dado):
    return dado ** 2

def main():
    tamanho_pool = multiprocessing.cpu_count() * 2 # Quantos processos serão criados

    print(f'Tamano da Pool: {tamanho_pool}')

    pool = multiprocessing.Pool(processes=tamanho_pool)

    entradas = list(range(7))
    saidas = pool.map(calcular, entradas)

    print(f'Saídas: {saidas}', )

    pool.close()  # Seria o start nas threads
    pool.join()

if __name__ == '__main__':
        main()
