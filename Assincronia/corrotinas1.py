import asyncio


async def diz_oi():
    print('Oi...')

# el = asyncio.get_event_loop()  # O modo comentado está que será descontinuado, DeprecationWarning: There is no current event loop
# el.run_until_complete(diz_oi())

asyncio.run(diz_oi())

# el.close()
