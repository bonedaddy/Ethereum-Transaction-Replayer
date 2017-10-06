from web3 import Web3, HTTPProvider, IPCProvider
import web3
import sys
import json

# Example command invocation
# python3.5 transactionReplay.py 0x0E06725F9D6b4766740D99533Ad65D9fb2028c93 0x61d7C02120bF9215aB541DCf0d658C9FBA96F75c password123 transactions.txt contract_abi.json /home/a/.ethereum/geth.ipc

# test account password is password123 (account 6 on rinkeby)
if len(sys.argv) < 7:
    msg = "Usage\npython3.5 transactionReplay.py <token-contract-address> <eth-acct> <eth-acct-pass> <transaction-file> <abi-json-file> <ipc-path>"
    print('Incorrect command invokation\n%s' % msg)
    exit()

tokenContractAddress = sys.argv[1]
ethereumAccountAddress = sys.argv[2]
ethereumAccountPassword = sys.argv[3]
fileName = sys.argv[4]
tokenContractAbiDefinition = sys.argv[5]
gethIpcPath = sys.argv[6]
usdPerToken = 0.35
tokenDict = {}


with open(tokenContractAbiDefinition, 'r') as abi_definition:
    abi = json.load(abi_definition)

# Attach an object to the local geth instance
web3ctl = Web3(IPCProvider(gethIpcPath))

# creates a handler to interact with the contract
tokenContractHandler = web3ctl.eth.contract(abi, tokenContractAddress)

# unlock the account
web3ctl.personal.unlockAccount(ethereumAccountAddress, ethereumAccountPassword)


# open transactions.txt, storing a file handler in fh
with open(fileName, 'r') as fh:
    # iterate over each line of the file
    for line in fh.readlines():
        try:
            # split the line into three fields (address, amount of ethereum, dollar value of eth at time of transaction)
            addr, eth, usd = line.split()
            # calculate the amount of VZT tokens to receive
            amountVZTReceive = float(usd) / float(usdPerToken)
            # truncate float to 2 decimal places
            amountVZTReceive = '%0.2f' % float(amountVZTReceive)
            # change to base wei
            vztAmount = Web3.toWei(amountVZTReceive, 'ether')
            # change to base addr
            address = Web3.toChecksumAddress(address)
            try:
                tokenContractHandler.transact({'from': ethereumAccountAddress}).transactionReplay(address, vztAmount)
            except Exception as e:
                print("Error", e)
        except Exception as e:
            print(e)