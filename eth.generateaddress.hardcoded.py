#!/usr/bin/python3

import blocksmith

#key = '0000000000000000000000000000000000000000000000000000000000000000'
#key = '0000000000000000000000000000000000000000000000000000000000000001'
key = '7077da4a47f6c85a21fe6c6cf1285c0fa06915871744ab1e5a5b741027884d00'

address = blocksmith.EthereumWallet.generate_address(key)
checksum_address = blocksmith.EthereumWallet.checksum_address(address)
print(checksum_address)
