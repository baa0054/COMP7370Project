import wave

import wav_key_derive
"""
This Python script tests the wav_key_derive function deriving keys from the WAV files.
Run: python3 wav_key_derive_test_1.py
"""

"""Constant as the number of frames in the WAV file."""
NUMBER_OF_FRAMES : int = 50

def wav_key_derive_test_1():

    files = ['wav_files/Moderato.wav', 'wav_files/sample-1.wav', 'wav_files/sample-2.wav',
             'wav_files/sample-3.wav', 'wav_files/sample-4.wav', 'wav_files/sample-5.wav']

    for filename in files:
        with wave.open(filename, 'rb') as wave_file:
            total_frames = wave_file.getnframes()
        if total_frames <= NUMBER_OF_FRAMES:
            print("WAV filename: ", filename)
            ciphertext = wav_key_derive.wav_key_derive(filename, total_frames)
            print(f"\nDerived key: \n{ciphertext}\n\n")
        else:
            print("WAV filename: ", filename)
            ciphertext = wav_key_derive.wav_key_derive(filename, NUMBER_OF_FRAMES)
            print(f"\nDerived key: \n{ciphertext}\n\n")

if __name__ == '__main__':
    wav_key_derive_test_1()