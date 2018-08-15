import time
import requests
import base64
import ecdsa

def generate_ECDSA_keys():
    """This function takes care of creating your private and public (your address) keys.
    It's very important you don't lose any of them or those wallets will be lost
    forever. If someone else get access to your private key, you risk losing your coins.
    private_key: str
    public_ley: base64 (to make it shorter)
    """
    sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1) #this is your sign (private key)
    private_key = sk.to_string().hex() #convert your private key to hex
    vk = sk.get_verifying_key() #this is your verification key (public key)
    public_key = vk.to_string().hex()
    public_key = base64.b64encode(bytes.fromhex(public_key))
    return public_key,private_key

def sign_ECDSA_msg(private_key):
    """Sign the message to be sent
    private_key: must be hex
    return
    signature: base64 (to make it shorter)
    message: str
    """
    # Get timestamp, round it, make it into a string and encode it to bytes
    message = str(round(time.time()))
    bmessage = message.encode()
    sk = ecdsa.SigningKey.from_string(bytes.fromhex(private_key), curve=ecdsa.SECP256k1)
    signature = base64.b64encode(sk.sign(bmessage))
    return signature, message

def send_transaction(addr_from, private_key, addr_to, amount):
    if len(private_key) == 64:
        signature, message = sign_ECDSA_msg(private_key)
        url = 'http://localhost:5000/send'
        payload = {"from": addr_from,
                   "to": addr_to,
                   "amount": amount,
                   "signature": signature.decode(),
                   "message": message}
        headers = {"Content-Type": "application/json"}

        res = requests.post(url, json=payload, headers=headers)
        print(res.text)
    else:
        print("Wrong address or key length! Verify and try again.")


def validate_signature(public_key, signature, message):
    public_key = (base64.b64decode(public_key)).hex()
    signature = base64.b64decode(signature)
    vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(public_key), curve=ecdsa.SECP256k1)
    try:
        return vk.verify(signature, message.encode())
    except:
        return False

def transaction(new_txion):
    if validate_signature(new_txion['from'], new_txion['signature'], new_txion['message']):


        print("New transaction")
        print("FROM: {0}".format(new_txion['from']))
        print("TO: {0}".format(new_txion['to']))
        print("AMOUNT: {0}\n".format(new_txion['amount']))

        return "Transaction submission successful\n"
    else:
        return "Transaction submission failed. Wrong signature\n"

public_key,private_key = generate_ECDSA_keys()

signature,message = sign_ECDSA_msg(private_key)

payload = {"from": "addr_from",
           "to": "addr_to",
           "amount": 5,
           "signature": signature,
           "message": message}

print (transaction(payload))
