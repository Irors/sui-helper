import asyncio
import random
from pysui.sui.sui_types import *
from pysui.sui.sui_txn import AsyncTransaction
from pysui.sui.sui_bcs import bcs
from pysui import AsyncClient
from loguru import logger
from .constant import *
from .sleeping import sleeping


async def get_token(client, token):

    SuiTokenObject = await client.get_coin(SuiString(token))

    return SuiTokenObject

async def get_token_object_from_function(SuiCoinObject):
    try:
        Object_non_zero = []
        Object_zero = []

        coin_objects  = SuiCoinObject.result_data.data

        for Object in SuiCoinObject.result_data.data:

            if int(Object.balance) != 0:
                Object_non_zero.append(Object.coin_object_id)
            if int(Object.balance) == 0:
                Object_zero.append(Object.coin_object_id)

        max_balance_object = max(coin_objects, key=lambda x: int(x.balance))

        if max_balance_object.coin_object_id in Object_non_zero:
            Object_non_zero.remove(max_balance_object.coin_object_id)

        return Object_non_zero, Object_zero, max_balance_object.coin_object_id, max_balance_object.balance
    except Exception as e:
        print(f'Error get_token_object_from_function: {e}')

async def time_expectation():
   await sleeping()

async def get_merge_coin(client, token):
        try:
            token = await get_token(client, token)
            Object_non_zero, Object_zero, wealthy_coin_object_id, max_balance_object = await get_token_object_from_function(token)
            await time_expectation()

            return Object_non_zero, Object_zero, wealthy_coin_object_id, max_balance_object
        except Exception as e:
            print(f'Error merge_coin: {e}')

async def get_wealthy_and_object(client, token, amount, number, address):

    token = await get_token(client, token)

    if token.result_data.data:
        Object_non_zero, Object_zero, wealthy_coin_object_id, max_balance_object = await get_token_object_from_function(token)
        return wealthy_coin_object_id, max_balance_object
    else:
        pass

async def trex_runner(txer):
    Object, balance = await get_wealthy_and_object(client=txer.client, token=sui, amount=None, number=None, address=None)

    await sleeping()
    try:

        result = await txer.execute(gas_budget=gas_budget, use_gas_object=Object)

        if result.result_data.effects.status.status == 'failure':
            logger.error(f"Статус: failure | Ошибка - {result.result_data.effects.status.error}")
        if result.result_data.effects.status.status == 'success':
            logger.success(f"The transaction was successful for {str(txer.client.config.active_address)[0:10]}...{str(txer.client.config.active_address)[-10:]}")
    except Exception as e:
        logger.error(f"Error trex_runner: {e}")


async def split_coin(client, token, amount, number, address):
    amount = to_sui_amount(amount)

    txer = AsyncTransaction(client)

    scoin = await txer.split_coin(coin=bcs.Argument("GasCoin"), amounts=[amount])

    await txer.transfer_objects(transfers=[scoin], recipient=client.config.active_address)
    await trex_runner(txer)


async def merge_coin(client, token, amount, number, address):

    txer = AsyncTransaction(client)

    Object_non_zero, Object_zero, wealthy_coin_object_id, max_balance_object = await get_merge_coin(client=client, token=token)

    async def zero():
        if len(Object_zero):
            logger.info("Попытка merge_coin | Object Zero")
            await txer.merge_coins(merge_to=txer.gas, merge_from=Object_zero) # Make merge coins
            await trex_runner(txer)

    async def non_zero():
        if len(Object_non_zero):
            logger.info("Попытка merge_coin | Object Non Zero")
            await txer.merge_coins(merge_to=txer.gas, merge_from=Object_non_zero) # Make merge coins
            await trex_runner(txer)

    await zero()
    await time_expectation()
    await non_zero()


async def create_gas_object(client, token, amount, number, address):

        txer = AsyncTransaction(client)

        amount = to_sui_amount(amount)
        spcoin = await txer.split_coin(coin=bcs.Argument("GasCoin"), amounts=[amount])
        await txer.transfer_objects(transfers=[spcoin], recipient=client.config.active_address)

        await trex_runner(txer)







async def get_address(client) -> str:

    return str(client.config.active_address)


def to_sui_amount(amount):
    return int(amount*10**9)

def from_sui_amount(amount):
    return float(amount/10**9)
