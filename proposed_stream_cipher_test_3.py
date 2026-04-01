import proposed_stream_cipher as psc
import wav_key_derive as w
import entropy_test as et
import plaintextAttack as pta

#print out padding
FILE_W = 25
TEXT_W = 25
STAT_W = 10
PTA_W  = 15

"""
This Python script tests encryption and decryption of multiple plaintexts.
"""
NUMBER_OF_FRAMES : int = 1

def proposed_stream_cipher_test_2():


    files = ['wav_files/Moderato.wav', 'wav_files/sample-1.wav', 'wav_files/sample-2.wav',
             'wav_files/sample-3.wav', 'wav_files/sample-4.wav', 'wav_files/sample-5.wav']

    PLAINTEXT = ["This is the best day ever, and I am really having a good time today. "]

    simResults = []

    for p in PLAINTEXT:
        print(f"Plaintext: {p}")
        for filename in files:
            print(f"\n\tWAV File: {filename}")
            print("\tEncryption")
            formatted_key = w.wav_key_derive(filename, NUMBER_OF_FRAMES, p)
            #Store and print test results
            testResults = et.randomness_simulations(formatted_key, filename, p)
            
            ciphertext = psc.proposed_stream_cipher_encrypt(p, formatted_key)

            recoveredBytes = pta.extractKey(p, ciphertext)
            recoveredKey = pta.lookForKeyLoop(recoveredBytes)
            testResults['PTA'] = recoveredKey if recoveredKey else "None"
            simResults.append(testResults)

            print(f"\tCiphertext: {ciphertext}")
            print("\tDecryption")
            plaintext = psc.proposed_stream_cipher_decrypt(ciphertext, formatted_key)
            print(f"\tPlaintext After Decryption: {plaintext}")
        print("----------------------------------------------------------------------------------------------")
        print("----------------------------------------------------------------------------------------------")


    #Shows the test results
    print("Simulation Report\n")
    header = f"{'WAV File':<{FILE_W}} | {'Plaintext':<{TEXT_W}} | {'Status':<{STAT_W}} | {'PTA (Period)'}"
    print(header)
    for res in simResults:
            display = ((res['text'][:TEXT_W-3] + "...") if len(res['text']) > TEXT_W else res['text'])
            print(f"{res['file']:<{FILE_W}} | "f"{display:<{TEXT_W}} | "f"{str(res['status']):<{STAT_W}} | "f"{str(res['PTA']):<{PTA_W}}")
        
if __name__ == "__main__":
    proposed_stream_cipher_test_2()