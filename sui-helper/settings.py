from modules.constant import sui

rpc = "https://sui-mainnet-rpc.allthatnode.com"     # Input rpc sui
token = sui                                         # Select active token
amount = 0.01                                       # Input amount token
custom_route = ['merge_coin', 'split_coin']         # Input module route. Available: [merge_coin, split_coin, create_gas_object, get_balance, Withdraw_scallo_protocol]
