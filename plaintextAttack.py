def extractKey(plaintext, ciphertext):
    plainttextHex = [int(pByte) for pByte in plaintext.encode("ascii")]
    ciphertextHex = [int(cByte) for cByte in ciphertext.encode("ascii")]

    recoveredKey = [plain ^ cipher for plain, cipher in zip(plainttextHex, ciphertextHex)]
    return recoveredKey

def lookForKeyLoop(recoveredKey):
    length = len(recoveredKey)
    for loop in range(1, length // 2):
        if recoveredKey[:loop] == recoveredKey[loop:2 * loop]:
            return loop
    return None



if __name__ == "__main__":
    plaintext = """This is the best day ever, and I am really having a good time today."""
    ciphertext = r"""),c!BjXv7JO,/6e`{7>qn[z*R56GX2%Jc$I2Sx$dnY49g"=Z&tV~w\W0;~"""
    recovered_key = extractKey(plaintext, ciphertext)
    loop_size = lookForKeyLoop(recovered_key)

    print(f"Key Period Found: {loop_size}")
    print(f"Recovered Key (first few bytes): {recovered_key[:10]}")