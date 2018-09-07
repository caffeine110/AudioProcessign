#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 20:48:44 2018

@author : gaurav gahukar
        : caffeine110
        
Aim : primary   : Speech to text generation using deep learning.
    : secondary : To plot wav file into Spectrogram

"""


#Importing libraries
#to process wav file
from scipy import signal
from scipy.io import wavfile
#to plot spectrogram
import matplotlib.pyplot as plt


#reading the  wav file
sample_rate, samples = wavfile.read('yes3.wav')
#generating values
frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)

#consturcting Spectrogram
plt.pcolormesh(times, frequencies, spectrogram)
plt.imshow(spectrogram)
# assign labels
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()

#print values
print(frequencies)
len(frequencies)
len(times)
len(spectrogram)
print(times)
print(spectrogram)