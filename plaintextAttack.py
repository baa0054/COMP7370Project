def extractKey(plaintext, ciphertext):
    plainttextHex = [int(pByte) for pByte in plaintext.encode("ascii")]
    ciphertextHex = [int(cByte) for cByte in ciphertext.encode("ascii")]

    recoveredKey = [plain ^ cipher for plain, cipher in zip(plainttextHex, ciphertextHex)]
    return recoveredKey

def lookForKeyLoop(recoveredKey):
    length = len(recoveredKey)
    for loop in range(1, length // 2 + 1):
        if recoveredKey[:loop] == recoveredKey[loop:2 * loop]:
            return f"Loop found: {loop}"
    return None
