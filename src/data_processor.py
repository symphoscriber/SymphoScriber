import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.io import wavfile

def spectrogram(filepath:str, interval: int) -> tuple:
    """
    read a .wav audio and extracts its sample rate and audio data, and convert to spectrogram
    only keeping 1 channel if multiple channels exist in the .wav
    TODO: might use librosa to get mono channel 1d array
    """
    fs, samples = wavfile.read(filepath)
    if samples.shape[1] > 1:
        samples = samples[:,0]
    return plt.specgram(x=samples, Fs=fs, NFFT=fs//interval)

def windowing(spec:tuple, n_window:int) -> tuple:
    """
    break the input spectrogram into separate windows to prepare training data
    """
    spec_size = len(spec[1])
    window_size = math.ceil(spec_size/n_window)
    
    for i in range(n_window):
        try:
            window_spec = spec[0][i*window_size:(i+1)*window_size]
            window_t = spec[1][i*window_size:(i+1)*window_size]
            yield (window_spec, window_t)
        except GeneratorExit:
            raise Exception("Something wrong with generator")