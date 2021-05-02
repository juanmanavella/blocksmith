#!/usr/bin/python3

import blocksmith

with open('keys.txt') as fp:
    key = fp.readline()
    cnt = 1
    while key:
        print(key.strip())
        address = blocksmith.EthereumWallet.generate_address(key.strip())
        print("No checksum: ",address)
        checksum_address = blocksmith.EthereumWallet.checksum_address(key.strip())
        print("Checksumed:  ",checksum_address," \n")
        key = fp.readline()
        cnt += 1

