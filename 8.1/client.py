from time import time
import requests
import base64
import ecdsa

import click
import json
import os

@click.command()
# @click.option('--count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name',
#               help='The person to greet.')
@click.option('-host', help='host')
@click.option('-port', help='port')
@click.option('-r', help='consignor')
@click.option('-e', help='consignee')
@click.option('-memo', help='memo')
@click.option('-pk', help='private_key')

def client(host,port,r,e,memo,pk):
    if (host and port and r and e and memo and pk):
        if len(pk) == 64:
            signature, message = sign_ECDSA_msg(pk)
            url = "http://{0}:{1}/post".format(host,port)
            d = {"consignor": r, "consignee": e,"memo":memo,"signature":signature,"message":message}
            r = requests.post(url, data=d)
            print(r.text)
        else:
            print("Wrong address or key length! Verify and try again.")

##

def generate_ECDSA_keys():
    sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1) #this is your sign (private key)
    private_key = sk.to_string().hex() #convert your private key to hex
    vk = sk.get_verifying_key() #this is your verification key (public key)
    public_key = vk.to_string().hex()
    public_key = base64.b64encode(bytes.fromhex(public_key))
    return public_key.decode(),private_key


def sign_ECDSA_msg(private_key):
    message = str(round(time()))
    bmessage = message.encode()
    sk = ecdsa.SigningKey.from_string(bytes.fromhex(private_key), curve=ecdsa.SECP256k1)
    signature = base64.b64encode(sk.sign(bmessage))
    return signature, message


if __name__ == '__main__':
    client()
