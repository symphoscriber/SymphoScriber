import math

import librosa
import matplotlib.pyplot as plt


def spectrogram(filepath: str, interval: int) -> tuple:
    """
    read a .wav audio and extracts its sample rate and audio data, and convert to spectrogram
    only keeping 1 channel if multiple channels exist in the .wav
    :param filepath: the filepath to the wavefile
    :param interval: the interval parameter used for the interval
    :return: the spectrogram components of the input files
    """
    samples, fs = librosa.core.load(filepath, sr=None, mono=True)
    # TODO: Use `scipy.signal.spectrogram` instead
    return plt.specgram(x=samples, Fs=fs, NFFT=fs // interval)


def windowing(spec: tuple, n_window: int) -> tuple:
    """
    Decompose the input spectrogram into separate windows to prepare the training data.
    :param spec: the spectrogram components of the input files
    :param n_window: the number of windows
    :return: a tuple consist of ( samples in the window, frequency of the windows, time frame)
    """
    # TODO: Use `scipy.signal.spectrogram` instead
    spec_size = len(spec[2])  # time points
    window_size = math.ceil(spec_size / n_window)

    for i in range(n_window):
        try:
            window_sample = spec[0][:, i * window_size:(i + 1) * window_size]
            window_freq = spec[1]
            window_t = spec[2][i * window_size:(i + 1) * window_size]
            yield (window_sample, window_freq, window_t)
        except GeneratorExit:
            raise Exception("Something wrong with generator")
