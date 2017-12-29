### This code is work in progress - not usable at the moment

import urllib2
import json

actualBalance = 0.0

#API-Calls
baseUrlCall = "https://dogechain.info/api/v1/"
#Last Block
lastBlockCall = "block/"
#Transaction
transactionAPI = "transaction/"
#Last Block number
getLastBlockCall = "https://dogechain.info/chain/Dogecoin/q/getblockcount"


def main():
    print("##########################")
    data = urllib2.urlopen("https://dogechain.info/chain/Dogecoin/q/addressbalance/DDogepartyxxxxxxxxxxxxxxxxxxw1dfzr")
    print("Balance: " + data.read())

    lastBlockNumber = urllib2.urlopen(getLastBlockCall)
    blockNumber = lastBlockNumber.read()

    print("Blocknumber: " + blockNumber)

    lastBlock = urllib2.urlopen(baseUrlCall+lastBlockCall+blockNumber)
    #print("Block: " + lastBlock.read())

    jsonData = json.load(lastBlock)

    print(jsonData)





if __name__ == '__main__':
    main()