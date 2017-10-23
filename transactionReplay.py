from web3 import Web3, IPCProvider
from getpass import getpass
import web3
import sys
import json
from getpass import getpass
from time import sleep

# Author: Postables
# Version: 1.0
# Description: Used to replay transactions for ICOs to push out tokens to backers after closure
#              Solidity function it calls is "replayTransaction"
# Example Solidity Code
###########################################################
#    function replayTransaction(address _backer)
#        public
#        onlyAdmin
#        withdrawalEnabled
#        returns (bool _withdrawn)
#    {
#        require(balances[_backer] > 0);
#        uint256 _rewardAmount = balances[_backer];
#        balances[_backer] = 0;
#        bearToken.transfer(_backer, _rewardAmount);
#        TokenTransfer(this, _backer, _rewardAmount);
###########################################################

if len(sys.argv) < 6:
    msg = "Usage\npython3.5 transactionReplay.py <token-contract-address> <eth-acct> <transaction-file> <abi-json-file> <ipc-path>"
    print('Incorrect command invokation\n%s' % msg)
    exit()


tokenContractAddress = sys.argv[1]
ethereumAccountAddress = sys.argv[2]
fileName = sys.argv[3]
tokenContractAbiDefinition = sys.argv[4]
gethIpcPath = sys.argv[5]
tokenDict = {}

ethereumAccountPassword = getpass("Enter your ethereum account password: ")

with open(tokenContractAbiDefinition, 'r') as abi_definition:
    abi = json.load(abi_definition)

web3ctl = Web3(IPCProvider(gethIpcPath))

tokenContractHandler = web3ctl.eth.contract(abi, tokenContractAddress)

web3ctl.personal.unlockAccount(ethereumAccountAddress, ethereumAccountPassword)


# open transactions.txt, storing a file handler in fh
with open(fileName, 'r') as fh:
    # iterate over each line of the file
    for line in fh.readlines():
        try:
            addr = line.strip('\n')
            address = Web3.toChecksumAddress(address)
            try:
                tokenContractHandler.transact({'from': ethereumAccountAddress}).replayTransaction(address)
            except Exception as e:
                print("Error", e)
        except Exception as e:
            print(e)
