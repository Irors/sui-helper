import asyncio
import random
from .constant import timeS

async def sleeping():
    x = random.randint(timeS[0], timeS[1])
    await asyncio.sleep(x)