import asyncio
import time

from .Withdraw_scallo_protocol import Withdraw_scallo_protocol
from .GetBalance import get_balance
from .modul import merge_coin, split_coin, create_gas_object, get_wealthy_and_object
from .GetBalance import Excel

class Modul:

    print()
    print("""Select modul:
  1 - Tools
  2 - dApps
  3 - Balance
  4 - Custom route""")
    print()
    modul = int(input(" --> "))

    match modul:
        case 1:
            print("""You've chosen Tools
 select tools :
   1 - Merge coin
   2 - Split coin
   3 - Create gas object
   4 - Wealthy and object""")
            print()
            tools = int(input(" --> "))

            match tools:
                case 1:
                    print("You've chosen - Merge coin -")
                    time.sleep(2)
                    run_modul = merge_coin

                case 2:
                    print("You've chosen - Split coin -")
                    time.sleep(2)
                    run_modul = split_coin

                case 3:
                    print("You've chosen - Create gas object -")
                    time.sleep(2)
                    run_modul = create_gas_object

                case 4:
                    print("You've chosen - Wealthy and object -")
                    time.sleep(2)
                    run_modul = get_wealthy_and_object

        case 2:
            print("""You've chosen dApps
 select dApps :
   1 - Withdraw scallop protocol""")
            print()
            dApps = int(input(" --> "))
            match dApps:

                case 1:
                    print("You've chosen - Withdraw scallop protocol -")
                    time.sleep(2)
                    run_modul = Withdraw_scallo_protocol

        case 3:
            print("You've chosen - Balance -")
            time.sleep(2)
            excel = Excel()
            run_modul = get_balance

        case 4:
            print("You've chosen - Custom route")
            time.sleep(2)
            run_modul = 'Custom route'