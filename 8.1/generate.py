from time import time
import base64
import ecdsa
import json
import os


def generate_ECDSA_keys():
    sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1) #this is your sign (private key)
    private_key = sk.to_string().hex() #convert your private key to hex
    vk = sk.get_verifying_key() #this is your verification key (public key)
    public_key = vk.to_string().hex()
    public_key = base64.b64encode(bytes.fromhex(public_key))
    return public_key.decode(),private_key

if __name__ == '__main__':
    public_key,private_key = generate_ECDSA_keys()
    print ("")
    print ("address:{0}".format(public_key))
    print ("")
    print ("private_key:{0}".format(private_key))
    print ("")
