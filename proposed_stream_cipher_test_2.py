import proposed_stream_cipher as psc
import wav_key_derive as w
"""
This Python script tests encryption and decryption of multiple plaintexts.
"""
NUMBER_OF_FRAMES : int = 1

def proposed_stream_cipher_test_2():


    files = ['wav_files/Moderato.wav', 'wav_files/sample-1.wav', 'wav_files/sample-2.wav',
             'wav_files/sample-3.wav', 'wav_files/sample-4.wav', 'wav_files/sample-5.wav']

    PLAINTEXT = ["Hello World!", "Python has a great day!", "#$$^^**", "122390"]

    for p in PLAINTEXT:
        print(f"Plaintext: {p}")
        for filename in files:
            print(f"\n\tWAV File: {filename}")
            print("\tEncryption")
            wav_derived_key = w.wav_key_derive(filename, NUMBER_OF_FRAMES, p)
            ciphertext = psc.proposed_stream_cipher_encrypt(p, wav_derived_key)
            print(f"\tCiphertext: {ciphertext}")
            print("\tDecryption")
            plaintext = psc.proposed_stream_cipher_decrypt(ciphertext, wav_derived_key)
            print(f"\tPlaintext After Decryption: {plaintext}")
        print("----------------------------------------------------------------------------------------------")
        print("----------------------------------------------------------------------------------------------")
if __name__ == "__main__":
    proposed_stream_cipher_test_2()