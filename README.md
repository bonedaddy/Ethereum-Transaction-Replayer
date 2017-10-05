# Ethereum Transaction Replayer

This python script can be used to replay any number of Ethereum transactions (ERC20, or plain Ether) to a particular smart contract.   

This can be used should you need to mirror transactions from one smart contract to another, or if you simply wish to make a large number of transactions at once.

It's primarily intended to be used for ICOs and crowdfunding campaigns to quickly calculate the amount of tokens to send (to 2 decimal places) based on the amount of ethereum provided.

With a little b it of modification (i will eventually include the generalized python file) this could be use for generalized, bulk transactions.

## How To Use

To use this, on the very last line of the python file replace the word 'transactionReplay' with whatever transfer function you will be using

You must also replace the value for the variable 'usdPerToken' with the appropriate value for your campaign

You must also create a transaction text file with 3 columns:
1) Address
2) Amount of Ethereum (or other tokens to send)
3) USD cost of Ethereum at time of transaction

Transaction file example:
0x0E06725F9D6b4766740D99533Ad65D9fb2028c93 0.93508444 283.12

## Dependencies
* web3py
* sys
* json
* python3.5

## To Do
1) Create generalized transaction replayer script
2) Optimize transaction replay script to minimize gas costs

## Eth Donations
* 0xb6182cd68324f42d8548428c8c04e270e7ca4968