import math
import numpy as np
from collections import Counter
import zlib



def randomness_simulations(keystreamBytes, fileName, plaintext):
    print("\n\tKeystream Randomness Analysis")

    #Entropy Calculation
    counter = Counter(keystreamBytes)
    length = len(keystreamBytes)
    entropy = -sum((count/length) * math.log2(count/length) for count in counter.values())

    #Nist Frequency Test
    bitString = ''.join(format(ord(b) if isinstance(b, str) else b, '08b') for b in keystreamBytes) 
    nlength = len(bitString)
    one = bitString.count('1')
    zero = bitString.count('0')
    sObs = abs(one - zero) / math.sqrt(nlength)
    pValue = math.erfc(sObs / math.sqrt(2))

    #Compression test
    dataToCompress = keystreamBytes.encode('utf-8') if isinstance(keystreamBytes, str) else keystreamBytes
    compressedLength = len(zlib.compress(dataToCompress))
    compressedRatio = compressedLength / length

    #Ideal 8.0
    print(f"\tEntropy: {entropy:.4f} bits/bytes")
    #Ideal > 0.01
    print(f"\tP-Value: {pValue:.4f}")
    #Ideal > 1.0
    print(f"\tCompression Ratio: {compressedRatio:.4f}")


    if pValue > 0.01 and entropy > 2.5 and compressedRatio > 0.75:
        status = "PASS"
    else:
        status = "FAIL"

    return {
        "file": fileName,
        "text": plaintext,
        "entropy": round(entropy, 4),
        "p_value": round(pValue, 4),
        "status": status
    }
