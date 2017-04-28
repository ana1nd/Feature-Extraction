# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 02:25:49 2017

@author: anand
"""

import os 
from text import function
import shutil
import sys

def list_files(dir):                                                                                                  
    r = []                                                                                                            
    subdirs = [x[0] for x in os.walk(dir)]                                                                            
    for subdir in subdirs:                                                                                            
        files = os.walk(subdir).next()[2]                                                                             
        if (len(files) > 0):                                                                                          
            for file in files:                                                                                        
                r.append(subdir + "/" + file)                                                                         
    return r
    
def find_second_last(text, pattern):
    return text.rfind(pattern, 0, text.rfind(pattern))   

def makeFeature(data):

    home = "/home/anand/Desktop/2/ASR-CS753/Project/Data/TIMIT/"     
    dir = home + data
    files = list_files(dir)
    
    ans = []
    for f in files : 
        if f[-3:]=='WAV':
            ans.append(f)
  
    dest = dir + "_features"
    os.makedirs(dest)      
    
    for a in ans:
        print a
        
        mk_dir = a[:a.rfind("/")]
        x = find_second_last(mk_dir, "/")
        remaining = mk_dir[x:]
        
        if os.path.isdir(dest+remaining)== False:            
            os.makedirs(dest+remaining)      
        
        wav = a[a.rfind("/")+1:]
        name = wav[:wav.rfind(".")]
    
        function(a,name) 
    
        shutil.move(home+name+".csv",dest+remaining)
    
    
data = sys.argv[1]
makeFeature(data)
    
    
    
    