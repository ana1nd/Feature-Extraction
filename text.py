# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 23:18:33 2017

@author: anand
"""
from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioFeatureExtraction
import numpy as np
import pandas as pd


def function(path,str):
    
    #[Fs,x] = audioBasicIO.readAudioFile("/home/anand/Desktop/2/ASR-CS753/Project/Data/TIMIT/TRAIN/DR2/MSAT0/SX86.WAV")
    [Fs,x] = audioBasicIO.readAudioFile(path)

    """ARGUMENTS
            signal:       the input signal samples
            Fs:           the sampling freq (in Hz)
            Win:          the short-term window size (in samples)
            Step:         the short-term window step (in samples)
        RETURNS
            stFeatures:   a numpy array (numOfFeatures x numOfShortTermWindows)
        """
    F = audioFeatureExtraction.stFeatureExtraction(x,Fs,0.050*Fs,0.025*Fs)
    
    Ft = np.transpose(F)
    
    sz = Ft.shape
    frames = sz[0]
    
    
    for i in range(0,frames,1):
    
        mfcc = Ft[i][8:20]     #mfcc feature
        energy = Ft[i][1:2]
    
        mfcc = np.append(mfcc,energy)
        if i==0:
            temp = mfcc
        else :
            temp = np.vstack((temp,mfcc))
        
    
    
    
    
    for i in range(0,frames,1):
        
        if i==0 :
            delta = temp[i]
        elif i!=(frames-1):
            sub = temp[i+1] - temp[i-1]
            delta = np.vstack((delta,sub))
        else:
            delta = np.vstack((delta,sub))
            
    #rint delta.shape[1]
    
    for i in range(0,frames,1):
        
        if i==0 :
            doubledelta = delta[i]
        elif i!=(frames-1):
            sub = delta[i+1] - delta[i-1]
            doubledelta = np.vstack((doubledelta,sub))
        else:
            doubledelta = np.vstack((doubledelta,sub))
    
    tempt = np.transpose(temp)
    deltat = np.transpose(delta)
    doubledeltat = np.transpose(doubledelta)
    
    answer = tempt
    answer = np.vstack((answer,deltat))
    answer = np.vstack((answer,doubledeltat))
    answer = np.transpose(answer)
    #print answer.shape
        
    for i in range(1,frames-1,1):
        
        current = np.concatenate((answer[i-1],answer[i]))
        current = np.concatenate((current,answer[i+1]))
        
        if i==1 :            
            biganswer = current
        else:
            biganswer = np.vstack((biganswer,current))
            #doubledelta = np.vstack((doubledelta,sub))
    
    #print biganswer.shape
    
    df = pd.DataFrame(biganswer)
    df.to_csv(str+".csv")
    
#print sys.argv
#print type(sys.argv[0])



    
    


