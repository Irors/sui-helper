from pysui.abstracts import SignatureScheme
from pysui import SuiConfig

from settings import amount, custom_route, rpc, token

from modules import *
import logging


async def ready(cfg, number):

    client = AsyncClient(cfg)
    address = await get_address(client)

    if Modul.run_modul == 'Custom route':
        for route in custom_route:
            await eval(route)(client, token=token, amount=amount, number=number, address=address)
    else:
        await Modul.run_modul(client, token=token, amount=amount, number=number, address=address)


async def main(wallets, number=2):
    tasks = []
    for keys in wallets:

        key = {
            'wallet_key': f'0x{keys.split(";")[0]}',
            'key_scheme': SignatureScheme.ED25519
        }

        cfg = SuiConfig.user_config(
            rpc_url=rpc,
            prv_keys=[key]
        )

        tasks.append(asyncio.create_task(ready(cfg, number)))
        number += 1

    await asyncio.gather(*tasks)



if __name__ == '__main__':
    logging.disable(logging.CRITICAL)

    with open("Wallet\\private_keys.txt") as file:
        wallets = [i.strip() for i in file]
    excel = Excel()

    """ Ассинхронность """
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main(wallets))


