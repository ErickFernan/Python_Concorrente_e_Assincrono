# pip install aiofiles

import asyncio
import aiofiles

async def exemplo_arq1():
    async with aiofiles.open('texto.txt') as arquivo:
        conteudo = await arquivo.read()
    print(conteudo)

async def exemplo_arq2():
    async with aiofiles.open('texto.txt') as arquivo:
        async for linha in arquivo:
            print(linha)

# def main():
    # el = asyncio.get_event_loop()
    # el.run_until_complete(exemplo_arq1())
    # el.close()

async def main():
    # await exemplo_arq1()
    await exemplo_arq2()

if __name__ =='__main__':
    asyncio.run(main())
