# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 16:25:38 2017

@author: Julien Arbellini
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import read
from scipy.fftpack import fft, fftfreq

Sign = read('Do bis.wav')

def affichagesignal(Sign):  
    Fe, signal = Sign
    N = len(signal)  
    Duree = N / Fe 
    
    plt.figure()  
    plt.clf()  
    T = np.linspace(0,Duree, N)  
    plt.subplot(2,1,1)  
    plt.title("Fichier Audio : signal et Spectre")  
    plt.xlabel("Durée (en sec.)")
    plt.plot(T,signal)
    
    tfd_signal = fft(signal)	# TFD du signal
    freq_signal = fftfreq(N, 1./Fe)	# Fréquences
    l=int(len(freq_signal)/2-1)
    plt.subplot(2,1,2)
    plt.xlabel("Fréquence (en Hz)")
    plt.plot(freq_signal[1:l],abs(tfd_signal[1:l]))
    plt.show()
    
affichagesignal(read('Do bis.wav'))    
affichagesignal(read('Re.wav'))

def comparaisondesignal(S1, S2):
    


