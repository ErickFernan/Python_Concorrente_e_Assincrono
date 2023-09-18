import datetime
import asyncio


async def gerar_dados(quantidade: int, dados:asyncio.Queue):
    print(f'Aguarde a geração de {quantidade} dados...')

    for idx in range(1, quantidade + 1):
        item = idx * idx
        await dados.put((item, datetime.datetime.now()))
        await asyncio.sleep(0.001)

    print(f'{quantidade} dados gerados com sucesso...')

async def processar_dados(quantidade: int, dados: asyncio.Queue, processados: int = 0):
    print(f'Aguarde o processamento de {quantidade} dados...')

    while processados < quantidade:
        await dados.get()
        processados += 1
        await asyncio.sleep(0.001)

    print(f'Foram processados {processados} itens')

if __name__ == '__main__':
    total = 5_000
    dados = asyncio.Queue()

    print(f'Computando {total * 2:.2f} dados')

    asyncio.run(gerar_dados(quantidade=total, dados=dados))
    asyncio.run(gerar_dados(quantidade=total, dados=dados))
    asyncio.run(processar_dados(quantidade=total * 2, dados=dados))
