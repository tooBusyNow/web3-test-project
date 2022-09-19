from audioop import add
from web3 import Web3

w3_provider = Web3(Web3.HTTPProvider(
    'https://goerli.infura.io/v3/94ce000a015b47f3adb990a6e0e505a0'))

contract_addr = '0x8850D82D75BE542820b325422572C9121e08C375'
contract_abi = [
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "someStartingCapital",
                                "type": "uint256"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "owner",
                                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "spender",
                                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "value",
                                "type": "uint256"
            }
        ],
        "name": "Approval",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "spender",
                                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                                "type": "uint256"
            }
        ],
        "name": "approve",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "account",
                                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                                "type": "uint256"
            }
        ],
        "name": "burn",
        "outputs": [],
        "stateMutability": "nonpayable",
                "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "spender",
                                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "subtractedValue",
                                "type": "uint256"
            }
        ],
        "name": "decreaseAllowance",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "destroy",
                "outputs": [],
                "stateMutability": "nonpayable",
                "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "spender",
                                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "addedValue",
                                "type": "uint256"
            }
        ],
        "name": "increaseAllowance",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "account",
                                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                                "type": "uint256"
            }
        ],
        "name": "mint",
        "outputs": [],
        "stateMutability": "nonpayable",
                "type": "function"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "previousOwner",
                                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newOwner",
                                "type": "address"
            }
        ],
        "name": "OwnershipTransferred",
        "type": "event"
    },
    {
        "inputs": [],
        "name": "renounceOwnership",
                "outputs": [],
                "stateMutability": "nonpayable",
                "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "to",
                                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                                "type": "uint256"
            }
        ],
        "name": "transfer",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "from",
                                "type": "address"
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "to",
                                "type": "address"
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "value",
                                "type": "uint256"
            }
        ],
        "name": "Transfer",
        "type": "event"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "from",
                                "type": "address"
            },
            {
                "internalType": "address",
                "name": "to",
                                "type": "address"
            },
            {
                "internalType": "uint256",
                "name": "amount",
                                "type": "uint256"
            }
        ],
        "name": "transferFrom",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "newOwner",
                                "type": "address"
            }
        ],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
                "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "owner",
                                "type": "address"
            },
            {
                "internalType": "address",
                "name": "spender",
                                "type": "address"
            }
        ],
        "name": "allowance",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "account",
                                "type": "address"
            }
        ],
        "name": "balanceOf",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "decimals",
                "outputs": [
            {
                "internalType": "uint8",
                "name": "",
                "type": "uint8"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "name",
                "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "owner",
                "outputs": [
            {
                "internalType": "address",
                "name": "",
                "type": "address"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "symbol",
                "outputs": [
            {
                "internalType": "string",
                "name": "",
                "type": "string"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [],
        "name": "totalSupply",
                "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    }
]

contract_obj = w3_provider.eth.contract(
    address=contract_addr, abi=contract_abi)

print(contract_obj.functions.totalSupply().call())  # returns 10050000

print(contract_obj.functions.name().call())  # returns AnotherUselessOne
