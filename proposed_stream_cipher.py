import random
"""
This Python module consists of encryption and decryption methods of the proposed stream cipher.
"""
# The key derived from the WAV file.
wav_derived_key : str
def proposed_stream_cipher_encrypt(plaintext : str, key : str):
    """
    This function performs simple stream cipher encryption.
    :param plaintext (str): The plaintext
    :param key (str): The key derived from the WAV file as a hex value.
    :return: The ciphertext as string
    """
    # Encoding the plaintext via UTF-8.
    plaintext_hex = '\\x' + plaintext.encode('utf-8').hex(' ').replace(' ','\\x')

    # Splitting the plaintext and key hex bytes by their delimiter '\x' creating lists of them respectively.
    plaintext_list = plaintext_hex.split('\\x')
    key_list = key.split('\\x')

    # Perform XOR operation between the plaintext hex value and key hex value byte by byte.
    ciphertext_hex = ""
    padding = ""
    for i in range(len(plaintext_list)):
        if i < len(key_list):
            ciphertext_hex += ('' + format(int(plaintext_list[i][0], 16) ^ int(key_list[i][0], 16), 'x')
                                  + format(int(plaintext_list[i][1], 16) ^ int(key_list[i][1], 16), 'x'))
        else:
            # Padding of random hex bytes if key's length is less than the plaintext length.
            h1 = random.randrange(0, 15)
            h2 = random.randrange(0, 15)
            padding += '\\x' + format(h1, 'x') + format(h2, 'x')
            ciphertext_hex += ('' + format(int(plaintext_list[i][0], 16) ^ h1, 'x')
                                  + format(int(plaintext_list[i][1], 16) ^ h2, 'x'))
    # Add padding to the key.
    key += padding
    wav_derive_key = key

    # Decoding the ciphertext via UTF-8 and then return it.
    ciphertext = ''.join([chr(int(ciphertext_hex[i:i + 2], 16)) for i in range(0, len(ciphertext_hex), 2)])
    return ciphertext

def proposed_stream_cipher_decrypt(ciphertext : str, key : str):
    """
        This function performs simple stream cipher decryption.
        :param ciphertext (str): The ciphertext
        :param key (str): The key derived from the WAV file as a hex value (it may be extended with padding
                          from encryption).
        :return: The plaintext as string
    """
    # Encoding the ciphertext via UTF-8.
    ciphertext_hex = '\\x' + ciphertext.encode('utf-8').hex(' ').replace(' ', '\\x')

    # Splitting the ciphertext and key hex values.
    ciphertext_list = ciphertext_hex.split('\\x')
    key_list = key.split('\\x')


    # Perform XOR operations between the plaintext hex value and key hex value byte by byte.
    plaintext_hex = ""
    for i in range(len(ciphertext_list)):
        plaintext_hex += ('' + format(int(ciphertext_list[i][0], 16) ^ int(key_list[i][0], 16), 'x')
                             + format(int(ciphertext_list[i][1], 16) ^ int(key_list[i][1], 16), 'x'))

    # Decoding the plaintext via UTF-8 and then return it.
    plaintext = ''.join([chr(int(plaintext_hex[i:i + 2], 16)) for i in range(0, len(plaintext_hex), 2)])
    return plaintext