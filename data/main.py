from web3 import Web3
from web3.middleware import geth_poa_middleware
from  contract_info import abi, addres_contract

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.middleware_onion.inject(geth_poa_middleware,layer=0)

contract = w3.eth.contract(address=addres_contract,abi=abi)

print(addres_contract)
print(f"Баланс смарт-контракта: {w3.eth.get_balance(addres_contract)}")
print(f"Баланс первого аккаунта {w3.eth.get_balance('0xaAe6319551C749af3ffcc394EEC18dAB97D08A8f')}")
print(f"Баланс второго аккаунта {w3.eth.get_balance('0x62A1994a62F9976403a1773aD81edEC9e6107A9a')}")
print(f"Баланс третьего аккаунта {w3.eth.get_balance('0xc0FD3A81D5271615650aecaC52Dc2D4fb8e3e910')}")
print(f"Баланс четвертого аккаунта {w3.eth.get_balance('0xe63F52cf99f6E4e6C36b1882F7A280E4B9d7B132')}")
print(f"Баланс пятого аккаунта {w3.eth.get_balance('0x716A499E47f9Bb9453491a6b82966860273043d0')}")
