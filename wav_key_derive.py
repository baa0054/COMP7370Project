import wave
"""
This module consists of the method to derive the key from the wav file.
"""
def wav_key_derive(wav_file : str, nbr_audio_frames : int):
    """
    This method derives a secret symmetric key from the audio frames of the WAV file.

    :param wav_file (str): WAV file name
    :param nbr_audio_frames (int): number of audio frames in a WAV file
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
            key += '\\x' + data[i][0] + data[i][1]

    return key