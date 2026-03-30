import proposed_stream_cipher as psc
import wav_key_derive as w
import entropy_test as et
"""
This Python script tests encryption and decryption of a simple plaintext.
"""
NUMBER_OF_FRAMES : int = 1

def proposed_stream_cipher_test_1():


    files = ['wav_files/Moderato.wav', 'wav_files/sample-1.wav', 'wav_files/sample-2.wav',
             'wav_files/sample-3.wav', 'wav_files/sample-4.wav', 'wav_files/sample-5.wav']

    PLAINTEXT = "Test"

    simResults = []

    for filename in files:
        print(f"WAV File: {filename}")
        print(f"Plaintext: {PLAINTEXT}")
        print("Encryption")
        wav_derived_key = w.wav_key_derive(filename, NUMBER_OF_FRAMES, PLAINTEXT)
        #Store and print test results
        testResults = et.randomness_simulations(wav_derived_key, filename, PLAINTEXT)
        simResults.append(testResults)

        ciphertext = psc.proposed_stream_cipher_encrypt(PLAINTEXT, wav_derived_key)
        print(f"Ciphertext: {ciphertext}")
        print("Decryption")
        plaintext = psc.proposed_stream_cipher_decrypt(ciphertext, wav_derived_key)
        print(f"Plaintext: {plaintext}")
        print("----------------------------------------------------------------------------------------------")
        print("----------------------------------------------------------------------------------------------")
    #Shows the test results
    print("Simulation Report\n")
    print(f"{'WAV File':<25} | {'Plaintext':<20} | {'Status'}")
    for res in simResults:
            print(f"{res['file']:<25} | {res['text']:<20} | {res['status']}")

if __name__ == "__main__":
    proposed_stream_cipher_test_1()
