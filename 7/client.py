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
@click.option('-a', help='action: n/s')
@click.option('-m', help='memo')
@click.option('-f', help='from address')
@click.option('-t', help='to address')
@click.option('-p', help='private_key')

def client(a,m,f,t,p):
    if a:
        if a=="n":
            public_key,private_key = generate_ECDSA_keys()
            click.echo("")
            click.echo("address:{0}".format(public_key))
            click.echo("")
            click.echo("private_key:{0}".format(private_key))
            click.echo("")
        if a=="s":
            if (m and f and t and p):
                print (send_transaction(f, t, m, p))

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

def send_transaction(from_address, to_address, memo, private_key):
    if len(private_key) == 64:
        signature, message = sign_ECDSA_msg(private_key)

        url = "http://localhost:8080/post"

        d = {"from_address": from_address, "to_address": to_address,"memo":memo,"signature":signature,"message":message}
        r = requests.post(url, data=d)
        return r.text
    else:
        return ("Wrong address or key length! Verify and try again.")

# public_key,private_key = generate_ECDSA_keys()
#
# state = send_transaction(public_key, public_key, "hello", private_key)
# print (state)

if __name__ == '__main__':
    client()
