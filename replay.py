import math
import wav_key_derive as w

def replayAndPredict(getKey, wavfile, plaintext):
    #Gets the key streams
    keystream1 = w.wav_key_derive(wavfile, 1 , plaintext)
    keystream2 = w.wav_key_derive(wavfile, 1 , plaintext)

    #Checks to see if the key streams are equal
    isReplayVul = (keystream1 == keystream2)
    replayStatus = "Replay Risk" if isReplayVul else "Secure"

    #Gets the bits and see if they have a correlation
    keystream1Bytes = [ord(c) for c in keystream1] if isinstance(keystream1, str) else keystream1
    keystream2Bytes = [ord(c) for c in keystream2] if isinstance(keystream2, str) else keystream2

    match = sum(1 for a, b in zip(keystream1Bytes, keystream2Bytes) if a == b)
    correlation = (match / len(keystream1Bytes)) * 100 if len(keystream1Bytes) > 0 else 100

    predictability = "High" if correlation > 90 else "Low"

    return {
        "replay": replayStatus,
        "predictability": predictability,
        "correlation": f"{correlation:.2f}%"
    }

