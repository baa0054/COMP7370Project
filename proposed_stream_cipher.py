"""
This Python module consists of encryption and decryption methods of the proposed stream cipher.
"""

def proposed_stream_cipher_encrypt(plaintext : str, key : str):
    """
    This function performs simple stream cipher encryption.
    :param plaintext (str): The plaintext
    :param key (str): The key derived from the WAV file as a hex value.
    :return: The ciphertext as string
    """
    if len(plaintext) == 0:
        return ""
    # Encoding the plaintext via ASCII.
    plaintext_hex = '\\x' + plaintext.encode('ascii').hex(' ').replace(' ','\\x')

    # Splitting the plaintext and key hex bytes by their delimiter '\x' creating lists of them respectively.
    plaintext_list = plaintext_hex.split('\\x')
    key_list = key.split('\\x')
    plaintext_list.remove('')
    key_list.remove('')

    # Perform XOR operation between the plaintext hex value and key hex value byte by byte.
    ciphertext = ""
    for i in range(len(plaintext_list)):
        ciphertext_hex = ('' + format(int(plaintext_list[i], 16) ^ int(key_list[i], 16), 'x'))
        ciphertext += ''.join([chr(int(ciphertext_hex[i:i + 2], 16)) for i in range(0, len(ciphertext_hex), 2)])

    return ciphertext

def proposed_stream_cipher_decrypt(ciphertext : str, key : str):
    """
        This function performs simple stream cipher decryption.
        :param ciphertext (str): The ciphertext
        :param key (str): The key derived from the WAV file as a hex value.
        :return: The plaintext as string
    """
    if len(ciphertext) == 0:
        return ""
    # Encoding the ciphertext via ASCII.
    ciphertext_hex = '\\x' + ciphertext.encode('ascii').hex(' ').replace(' ', '\\x')

    # Splitting the ciphertext and key hex values.
    ciphertext_list = ciphertext_hex.split('\\x')
    key_list = key.split('\\x')
    ciphertext_list.remove('')
    key_list.remove('')

    # Perform XOR operations between the plaintext hex value and key hex value byte by byte.
    plaintext = ""
    for i in range(len(ciphertext_list)):
        plaintext_hex = ('' + format(int(ciphertext_list[i], 16) ^ int(key_list[i], 16), 'x'))
        plaintext += ''.join([chr(int(plaintext_hex[i:i + 2], 16)) for i in range(0, len(plaintext_hex), 2)])

    return plaintext