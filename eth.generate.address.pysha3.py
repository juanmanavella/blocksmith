#!/usr/bin/python3 

from secrets import token_bytes
from coincurve import PublicKey
from sha3 import keccak_256

with open('keys.txt') as fp:
    key = fp.readline()
    
    # Debug
    print("readed key: ",key)

    encoded_key = key.encode()
    print("encoded_key: ", encoded_key.decode())
    
    striped_key = encoded_key.strip()
    print("striped_key: ",striped_key.strip())

    cnt = 1
    while key:
        # private_key = keccak_256(token_bytes(32)).digest()
        public_key = PublicKey.from_valid_secret(striped_key).format(compressed=False)[1:]
        addr = keccak_256(public_key).digest()[-20:]

        print('private_key:', striped_key.hex())
        print('eth addr: 0x' + addr.hex())
        key = fp.readline()
        cnt += 1

