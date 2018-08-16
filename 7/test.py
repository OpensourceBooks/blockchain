import time
import requests
import base64
import ecdsa

def send_transaction(addr_from, addr_to, amount, private_key):
    if len(private_key) == 64:
        signature, message = sign_ECDSA_msg(private_key)

        payload = {"from": addr_from,
                   "to": addr_to,
                   "amount": amount,
                   "signature": signature.decode(),
                   "message": message}

        return transaction(payload)
    else:
        return ("Wrong address or key length! Verify and try again.")




def generate_ECDSA_keys():

    sk = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1) #this is your sign (private key)
    private_key = sk.to_string().hex() #convert your private key to hex
    vk = sk.get_verifying_key() #this is your verification key (public key)
    public_key = vk.to_string().hex()
    #we are going to encode the public key to make it shorter
    public_key = base64.b64encode(bytes.fromhex(public_key))

    # filename = input("Write the name of your new address: ") + ".txt"
    # with open(filename, "w") as f:
    #     f.write("Private key: {0}\nWallet address / Public key: {1}".format(private_key, public_key.decode()))
    # print("Your new address and private key are now in the file {0}".format(filename))
    return public_key.decode(),private_key

def sign_ECDSA_msg(private_key):
    message = str(round(time.time()))
    bmessage = message.encode()
    sk = ecdsa.SigningKey.from_string(bytes.fromhex(private_key), curve=ecdsa.SECP256k1)
    signature = base64.b64encode(sk.sign(bmessage))
    return signature, message

def validate_signature(public_key, signature, message):
    public_key = (base64.b64decode(public_key)).hex()
    signature = base64.b64decode(signature)
    vk = ecdsa.VerifyingKey.from_string(bytes.fromhex(public_key), curve=ecdsa.SECP256k1)
    try:
        return vk.verify(signature, message.encode())
    except:
        return False

def transaction(new_txion):
        # Then we add the transaction to our list
        if validate_signature(new_txion['from'], new_txion['signature'], new_txion['message']):

            #print("New transaction")
            #print("FROM: {0}".format(new_txion['from']))
            # print("TO: {0}".format(new_txion['to']))
            # print("AMOUNT: {0}\n".format(new_txion['amount']))

            return "Transaction submission successful\n"
        else:
            return "Transaction submission failed. Wrong signature\n"



public_key,private_key = generate_ECDSA_keys()

print ("public_key:{0}".format(public_key))
print ("private_key:{0}".format(private_key))

state = send_transaction(public_key, public_key, 1, private_key)
print (state)
