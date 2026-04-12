import wave
import entropy_test as et
import wav_key_derive
import plaintextAttack as pta
import replay as re
"""
This Python script tests the wav_key_derive function deriving keys from the WAV files.
Run: python3 wav_key_derive_test_1.py
"""

FILE_W = 25
TEXT_W = 20
STAT_W = 10
PTA_W  = 15
PRE_W  = 12

"""Constant as the number of frames in the WAV file."""
NUMBER_OF_FRAMES : int = 50

def wav_key_derive_test_1():

    simResults = []

    files = ['wav_files/Moderato.wav', 'wav_files/sample-1.wav', 'wav_files/sample-2.wav',
             'wav_files/sample-3.wav', 'wav_files/sample-4.wav', 'wav_files/sample-5.wav']
    
    test = "Test Plaintext"

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

        derived_key = wav_key_derive.wav_key_derive(filename, NUMBER_OF_FRAMES)

        # Perform entropy test on the KEYSTREAM
        testResults = et.randomness_simulations(derived_key, filename, test)
        replayandpredict = re.replayAndPredict(derived_key, filename, test)
        recoveredKey = pta.lookForKeyLoop(derived_key)
        testResults.update({
                "replay": replayandpredict['replay'],
                "predict": replayandpredict['predictability'],
                "pta": recoveredKey
            })
        simResults.append(testResults)

    print("Simulation Report\n")
    header = f"{'WAV File':<{FILE_W}} | {'Plaintext':<{TEXT_W}} | {'Status':<{STAT_W}} | {'PTA (Period)':<{PTA_W}} | {'Replay':<{PRE_W}} | {'Predictability':<{PRE_W}}"
    print(header)
    for res in simResults:
            display = ((res['text'][:TEXT_W-3] + "...") if len(res['text']) > TEXT_W else res['text'])
            print(f"{res['file']:<{FILE_W}} | "f"{display:<{TEXT_W}} | "f"{str(res['status']):<{STAT_W}} | "f"{str(res['pta']):<{PTA_W}} | "f"{str(res['replay']):<{PRE_W}} | "f"{str(res['predict']):<{PRE_W}}")
        
            
if __name__ == '__main__':
    wav_key_derive_test_1()
