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

# def main():  # Os comentários é o jeito que o curso faz, mas que serão descontinuados
async def main():
    total = 5_000
    dados = asyncio.Queue()

    print(f'Computando {total * 2:.2f} dados')

    # el = asyncio.get_event_loop() # el = event loop

    # tarefa1 = el.create_task(gerar_dados(total, dados))
    # tarefa2 = el.create_task(gerar_dados(total, dados))
    # tarefa3 = el.create_task(processar_dados(total * 2, dados))

    # tarefas = asyncio.gather(tarefa1, tarefa2, tarefa3) # gather é o coletor, ele agrupa as 3 tarefas na variável

    # el.run_until_complete(tarefas)

    tarefa1 = gerar_dados(total, dados)
    tarefa2 = gerar_dados(total, dados)
    tarefa3 = processar_dados(total * 2, dados)

    await asyncio.gather(tarefa1, tarefa2, tarefa3)

if __name__ == '__main__':
    asyncio.run(main())
