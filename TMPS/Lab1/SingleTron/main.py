import asyncio
import random

import database_connection

async def chet():
    db1 = database_connection.Database.get_instance()
    for i in range(10):
        db1.insert_data("Данные из первого цикла")
        await asyncio.sleep(random.randint(1,3))

async def nechet():
    db2 = database_connection.Database.get_instance()
    for i in range(10):
        db2.insert_data("Данные из второго цикла")
        await asyncio.sleep(random.randint(1,3))

async def start():
    await asyncio.gather(chet(),nechet())
    db3 = database_connection.Database.get_instance()
    db3.select_data()

asyncio.run(start())