import random
import base64

def keyAlgo(key):
    keyLength = len(key)
    sbox = list(range(256))
    j = 0
    for i in range(256):
        j = (j + sbox[i] + key[i % keyLength]) % 256
        sbox[i], sbox[j] = sbox[j], sbox[i]
    return sbox

def randomGen(sbox, num):
    i = 0
    j = 0
    keyStream = []
    for  in range(num):
        i = (i + 1) % 256
        j = (j + sbox[i]) % 256
        sbox[i], sbox[j] = sbox[j], sbox[i]
        key = sbox[(sbox[i] + sbox[j]) % 256]
        keyStream.append(key)
    return keyStream

def rc4Stream(key, data):
    if isinstance(key, str):
        key = [ord(char) for char in key]

    if isinstance(data, str):
        data = [ord(char) for char in data]
    sbox = keyAlgo(key)
    keyStream = randomGen(sbox, len(data))
    output = [b ^ k for b, k in zip(data, keyStream)]
    return bytes(output)



def generateKeyStream(length, key):
random.seed(key)
return [random.randint(0, 255) for
 in range(length)]

def encrypt(plaintext, key):
plaintextBytes = plaintext.encode("utf-8")
keyStream = generateKeyStream(len(plaintextBytes), key)
ciphertext =  bytes([b ^ k for b, k in zip(plaintextBytes, keyStream)])
return ciphertext
def decrypt(ciphertext, key):
keyStream = generateKeyStream(len(ciphertext), key)
plaintextBytes = bytes([b ^ k for b, k in zip(ciphertext, keyStream)])
return plaintextBytes.decode("utf-8")
key = "testkey"
message = "Testing the functions."


ciphertext = rc4Stream(key, message)
b64_ciphertext = base64.b64encode(ciphertext)
print("Ciphertext (base64):", b64_ciphertext.decode())

plaintext = rc4Stream(key, ciphertext)
print("Plaintext:", plaintext.decode())
