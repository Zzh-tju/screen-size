# coding=utf-8
from glob import glob
import os, shutil
import math
import random
import numpy  as np
import matplotlib.pyplot as plt


m=0
with open('/home/ubuntu/ZZH/mv/size.txt','r+') as f:
    lines = f.readlines()
    with open('/home/ubuntu/ZZH/mv/size1.txt','a') as ff:
        for line in lines:

            #print(line)
            if line=='-\n':
                ff.write('-')
                ff.write('\n')

                m=0
                continue
            name=line.split("\n", 2)[0]
            if m==0:
                ff.write(name)
                ff.write(' ')
                m=1
                continue
            if m==1:
                ff.write(name)
                ff.write(' ')
                m=2
                continue
            if m==2:
                ff.write(name)
                ff.write('\n')
                m=0
