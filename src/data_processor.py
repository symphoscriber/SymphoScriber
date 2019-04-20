import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.io import wavfile

def spectrogram(samples:np.ndarray, sample_rate:int, interval:int):
    """
    convert the input 1d array to its spectrogram form
    """
    return plt.specgram(x=samples, Fs=sample_rate, NFFT=sample_rate//64)

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