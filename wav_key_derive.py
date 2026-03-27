import wave
import random
"""
This module consists of the method to derive the key from the wav file.
"""
def wav_key_derive(wav_file : str, nbr_audio_frames : int, plaintext : str = ""):
    """
    This method derives a secret symmetric key from the audio frames of the WAV file.

    :param wav_file (str): WAV file name
    :param nbr_audio_frames (int): number of audio frames in a WAV file
    :param plaintext (str, optional): The plaintext
    :return: The key as string
    """
    if not wav_file.endswith('.wav'):
        return 0

    """Opening and reading the raw data of the WAV file"""
    with wave.open(wav_file, 'rb') as w:
        raw_data = w.readframes(nbr_audio_frames)

    """Reformatting the raw data of the WAV file into a string of hex values."""
    data = str(raw_data).removeprefix('b\'').removesuffix('\'')
    data = data.split('\\x')
    key = ''
    for i in range(1, len(data)):
        """If the hex value has less than 2 characters, skip it."""
        if len(data[i]) > 1:
            key += '\\x' + format(int(data[i][0], 16) % 8, 'x') + format(int(data[i][1], 16) % 16, 'x')

    if len(plaintext) != 0:
        plaintext_hex = '\\x' + plaintext.encode('ascii').hex(' ').replace(' ', '\\x')

        kh = key.split('\\x')
        ph = plaintext_hex.split('\\x')
        kh.remove('')
        ph.remove('')

        """
        If the key length is less than the plaintext length (in number of hex bytes), implement random ASCII hex byte 
        padding.
        """
        if len(kh) < len(ph):
            d = len(ph) - len(kh)
            for i in range(d):
                h1 = random.randint(0, 7)
                h2 = random.randint(0, 15)
                h3 = '' + format(int(h1), 'x') + format(int(h2), 'x')
                key += '\\x' + h3
    return key