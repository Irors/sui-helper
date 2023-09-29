
import logger
from .modul import *
async def Withdraw_scallo_protocol(client, token, amount, number, address):

    try:
        txer = AsyncTransaction(client)
        wealthy_coin_object_id, max_balance_object = await get_wealthy_and_object(client=client, token=suis)

        if int(max_balance_object) == 0:
            return True
        else:
            logger.info("Остынь ...")
            await sleeping()

            # Split
            await txer.split_coin(coin=wealthy_coin_object_id, amounts=[int(max_balance_object)])

            # Transfer
            await txer.transfer_objects(transfers=[wealthy_coin_object_id], recipient=client.config.active_address)

            # MoveCall
            trx = await txer.move_call(
                target="0xc05a9cdf09d2f2451dea08ca72641e013834baef3d2ea5fcfee60a9d1dc3c7d9::redeem::redeem",
                arguments=[
                    ObjectID('0x07871c4b3c847a0f674510d4978d5cf6f960452795e8ff6f189fd2088a3f6ac7'),
                    ObjectID('0xa757975255146dc9686aa823b7838b507f315d704f428cbadad2f4ea061939d9'),
                    bcs.Argument("NestedResult", (0, 0)),
                    ObjectID('0x0000000000000000000000000000000000000000000000000000000000000006')

                ],
                type_arguments=[
                    '0x2::sui::SUI',
                ],
            )

            # Transfer
            await txer.transfer_objects(transfers=[trx], recipient=client.config.active_address)

            logger.info("Transaction Withdraw Lending send | Scallop |")
            await trex_runner(txer)

    except TypeError as e:
        logger.error(f"Ошибка: {e}")