import wave
import entropy_test as et
import wav_key_derive
import plaintextAttack as pta
import replay as re
import time
"""
This Python script measures the time (in seconds) to generate a key from each WAV file from 1 audio frame to its total 
number of audio frames.
Run: python3 wav_key_derive_test_2
"""

FILE_W = 25
TEXT_W = 20
STAT_W = 10
PTA_W  = 15
PRE_W  = 12

"""Variable for the number of frames"""
number_of_frames : int

def wav_key_derive_test_2():

    test_audioframe_lengths = [1, 10, 100, 1000, 10000, 100000, 1000000]

    files = ['wav_files/Moderato.wav', 'wav_files/sample-1.wav', 'wav_files/sample-2.wav',
             'wav_files/sample-3.wav', 'wav_files/sample-4.wav', 'wav_files/sample-5.wav']
    
    simResults = []
    
    test = "Test plaintext"

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
                key = wav_key_derive.wav_key_derive(filename, i)
                end_time = time.time()
                elapsed_time = end_time - start_time

                print(f"Number of audio frames: {i}")
                print(f"Key Length as number of hex bytes: {len(key.split('\\x')) - 1}")
                print(f"Key Generation Time: {elapsed_time} seconds\n")
                derived_key = wav_key_derive.wav_key_derive(filename, i)

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

        """Key Generation Time with the WAV file's total number of frames."""
        start_time = time.time()
        key = wav_key_derive.wav_key_derive(filename, number_of_frames)
        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f"Total Number of audio frames: {number_of_frames}")
        print(f"Key Length as number of hex bytes: {len(key.split('\\x')) - 1}")
        print(f"Key Generation Time: {elapsed_time} seconds")
        print("----------------------------------------------------------------------------------------------")
        print("----------------------------------------------------------------------------------------------")


    print("Simulation Report\n")
    header = f"{'WAV File':<{FILE_W}} | {'Plaintext':<{TEXT_W}} | {'Status':<{STAT_W}} | {'PTA (Period)':<{PTA_W}} | {'Replay':<{PRE_W}} | {'Predictability':<{PRE_W}}"
    print(header)
    for res in simResults:
         display = ((res['text'][:TEXT_W-3] + "...") if len(res['text']) > TEXT_W else res['text'])
         print(f"{res['file']:<{FILE_W}} | "f"{display:<{TEXT_W}} | "f"{str(res['status']):<{STAT_W}} | "f"{str(res['pta']):<{PTA_W}} | "f"{str(res['replay']):<{PRE_W}} | "f"{str(res['predict']):<{PRE_W}}")


if __name__ == '__main__':
    wav_key_derive_test_2()
