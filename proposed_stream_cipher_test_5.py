import proposed_stream_cipher as psc
import wav_key_derive as w
import entropy_test as et
import plaintextAttack as pta
import replay as re

#print out padding
FILE_W = 25
TEXT_W = 25
STAT_W = 10
PTA_W  = 15
PRE_W = 10

"""
This Python script tests encryption and decryption of multiple plaintexts.
"""
NUMBER_OF_FRAMES : int = 1

def proposed_stream_cipher_test_5():


    files = ['wav_files/Moderato.wav', 'wav_files/sample-5.wav']

    PLAINTEXT = ["PassTest123!"]

    simResults = []

    for p in PLAINTEXT:
        print(f"Plaintext: {p}")
        for filename in files:
            print(f"\n\tWAV File: {filename}")
            print("\tEncryption")
            formatted_key = w.wav_key_derive(filename, NUMBER_OF_FRAMES, p)
            #Store and print test results
            testResults = et.randomness_simulations(formatted_key, filename, p)
            replayandpredict = re.replayAndPredict(w.wav_key_derive, filename, p)
            ciphertext = psc.proposed_stream_cipher_encrypt(p, formatted_key)

            recoveredBytes = pta.extractKey(p, ciphertext)
            recoveredKey = pta.lookForKeyLoop(recoveredBytes)
            testResults.update({
                "replay": replayandpredict['replay'],
                "predict": replayandpredict['predictability'],
                "pta": recoveredKey
            })
            simResults.append(testResults)

            print(f"\tCiphertext: {ciphertext}")
            print("\tDecryption")
            plaintext = psc.proposed_stream_cipher_decrypt(ciphertext, formatted_key)
            print(f"\tPlaintext After Decryption: {plaintext}")
        print("----------------------------------------------------------------------------------------------")
        print("----------------------------------------------------------------------------------------------")


    #Shows the test results
    print("Simulation Report\n")
    header = f"{'WAV File':<{FILE_W}} | {'Plaintext':<{TEXT_W}} | {'Status':<{STAT_W}} | {'PTA (Period)':<{PTA_W}} | {'Replay':<{PRE_W}} | {'Predictability':<{PRE_W}}"
    print(header)
    for res in simResults:
            display = ((res['text'][:TEXT_W-3] + "...") if len(res['text']) > TEXT_W else res['text'])
            print(f"{res['file']:<{FILE_W}} | "f"{display:<{TEXT_W}} | "f"{str(res['status']):<{STAT_W}} | "f"{str(res['pta']):<{PTA_W}} | "f"{str(res['replay']):<{PRE_W}} | "f"{str(res['predict']):<{PRE_W}}")
        
if __name__ == "__main__":
    proposed_stream_cipher_test_5()
