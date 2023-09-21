import datetime
import computa


def main():
    inicio = datetime.datetime.now()

    computa.computar(fim= 50_000_000)

    tempo = datetime.datetime.now() - inicio

    print(f'Terminou em {tempo.total_seconds():.2f} segundos.')

if __name__ == '__main__':
    main()

    """
    python normal    = Terminou em 9.28 segundos.
    python compilado = Terminou em 6.61 segundos.
    cython normal    = Terminou em 0.21 segundos.
    C                = Terminou em 0.18 segundos.  Não sei direito se é o C puro ou apenas o Cython sem o GIL
    """