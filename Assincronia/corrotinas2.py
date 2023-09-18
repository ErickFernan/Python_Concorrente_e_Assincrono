import asyncio


async def diz_oi_demorado():
    print('Oi...')
    await asyncio.sleep(2)
    print('todos...')

# el = asyncio.get_event_loop()  # O modo comentado está que será descontinuado, DeprecationWarning: There is no current event loop
# el.run_until_complete(diz_oi_demorado())

asyncio.run(diz_oi_demorado())

# el.close()
