from web3 import Web3
from solcx import compile_source


web3_prov = Web3(Web3.HTTPProvider(
    'https://goerli.infura.io/v3/94ce000a015b47f3adb990a6e0e505a0'))


with open('contract.sol') as fh:
    contract_data = fh.read()

compiled = compile_source(contract_data,  output_values=['abi', 'bin'])
contract_id, contract_interface = compiled.popitem()

abi = contract_interface['abi']
bytecode = contract_interface['bin']


with open('secret.key') as fh:
    private_key = fh.read()

account_addr = '0xD49Fc38f055DC84cE40Cf3b8E958072CDE40B903'

UselessContract = web3_prov.eth.contract(abi=abi, bytecode=bytecode)

deploy_tr = UselessContract.constructor(111333777).build_transaction(
    {
        'from': account_addr,
        'nonce' : web3_prov.eth.get_transaction_count(account_addr),
    }
)

deploy_signed = web3_prov.eth.account.sign_transaction(deploy_tr, private_key)

print('Signed and send to the ETH network')
tx_hash = web3_prov.eth.send_raw_transaction(deploy_signed.rawTransaction)
tx_receipt = web3_prov.eth.wait_for_transaction_receipt(tx_hash)

print(f'Successfully deployed at: { tx_receipt.contractAddress }')


DeployedInstance = web3_prov.eth.contract(address=tx_receipt.contractAddress, abi=abi)

print("Token Name: ", DeployedInstance.functions.name().call())
print("Token Symbol:",  DeployedInstance.functions.symbol().call())