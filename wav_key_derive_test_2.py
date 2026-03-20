import time
import wav_key_derive
import wave
"""
This Python script measures the time (in seconds) to generate a key from each WAV file from 1 audio frame to its total 
number of audio frames.
Run: python3 wav_key_derive_test_2
"""

"""Variable for the number of frames"""
number_of_frames : int

def wav_key_derive_test_2():

    test_audioframe_lengths = [1, 10, 100, 1000, 10000, 100000, 1000000]

    files = ['wav_files/Moderato.wav', 'wav_files/sample-1.wav', 'wav_files/sample-2.wav',
             'wav_files/sample-3.wav', 'wav_files/sample-4.wav', 'wav_files/sample-5.wav']

    for filename in files:
        with wave.open(filename, 'rb') as w:
            number_of_frames = w.getnframes()

        """Getting the key generation time as the number of frames increases by 10^x (0 >= x <= 6) up to the WAV file's 
           total number of frames.
        """
        print(f"WAV File: {filename}")
        for i in test_audioframe_lengths:
            if i <= number_of_frames:
                start_time = time.time()
                cipertext = wav_key_derive.wav_key_derive(filename, i)
                end_time = time.time()
                elapsed_time = end_time - start_time

                print(f"Number of audio frames: {i}")
                print(f"Ciphertext Length as number of hex bytes: {len(cipertext)}")
                print(f"Key Generation Time: {elapsed_time} seconds\n")

        """Key Generation Time with the WAV file's total number of frames."""
        start_time = time.time()
        cipertext = wav_key_derive.wav_key_derive(filename, number_of_frames)
        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f"Total Number of audio frames: {number_of_frames}")
        print(f"Ciphertext Length as number of hex bytes: {len(cipertext)}")
        print(f"Key Generation Time: {elapsed_time} seconds")
        print("----------------------------------------------------------------------------------------------")
        print("----------------------------------------------------------------------------------------------")

if __name__ == '__main__':
    wav_key_derive_test_2()