#coding=gbk
from glob import glob
import os, shutil
import math
import random
import numpy  as np
import matplotlib.pyplot as plt
import cv2
from matplotlib import colors
from PIL  import ImageColor, ImageFont, ImageDraw, Image

res = 4 # resolution
n=0
m=0
position=0
file=0

font = ImageFont.truetype('./MSYHL.TTC', int(12.5*res))

color = ['black', 'red', 'orange','blue','hotpink',
        'olivedrab','cornflowerblue','lawngreen','cyan','tomato',
        'darkorchid','magenta','yellowgreen','navy','crimson',
        'slategrey','midnightblue','wheat','teal','lightblue',
        'peru','sandybrown','purple','orangered','royalblue',
        'darkmagenta','deeppink','pink','deepskyblue','dodgerblue',
        'green','gold','tan','gray','darkred',
        'lightcoral','black', 'red', 'orange','blue','hotpink',
        'olivedrab','cornflowerblue','lawngreen','cyan','tomato',
        'darkorchid','magenta','yellowgreen','navy','crimson',
        'slategrey','midnightblue','wheat','teal','lightblue',
        'peru','sandybrown','purple','orangered','royalblue',
        'darkmagenta','deeppink','pink','deepskyblue','dodgerblue',
        'green','gold','tan','gray','darkred',
        'lightcoral']


def RGB2BGR(rgb_tuple):
    assert isinstance(rgb_tuple, tuple)
    assert len(rgb_tuple) == 3
    r = int(rgb_tuple[0]*255)
    g = int(rgb_tuple[1]*255)
    b = int(rgb_tuple[2]*255)
    return (b, g, r)

x=np.zeros((50,3),dtype=np.float)
y=np.zeros(shape=(50,2)).astype(np.str_)

with open('/home/ubuntu/ZZH/mv/name.txt','r+') as ff:
    names = ff.readlines()

with open('/home/ubuntu/ZZH/mv/size1.txt','r+') as f:
    lines = f.readlines()
    #print(lines[1][1])
    for j, (line,name) in enumerate(zip(lines,names)):
        position = position+1
        if line=='-\n':


            if m>0:
                ind = np.argsort(-x[:,2])
                place_x = 1000*res*0.5-int(max(x[ind][:,0])/32*(1000*res-200*res)*0.5)
                place_y = 1000*res-50*res-int(max(x[ind][:,1])/32*(1000*res-200*res))
                for i in range(m):
                    w=x[ind][i,0]
                    h=x[ind][i,1]
                    area=x[ind][i,2]
                    half_w=int(w/32*(1000*res-200*res)*0.5)
                    hh=int(h/32*(1000*res-200*res))
                    x1=int(1000*res*0.5-half_w)
                    x2=int(1000*res*0.5+half_w)
                    y1=int(1000*res-50*res-hh)
                    y2=int(1000*res-50*res)

                    #print(x[ind])
                    #print(y[ind])
                    if w<1:
                        break
                    #print(color[i])

                    img_pil = Image.fromarray(img)
                    draw = ImageDraw.Draw(img_pil)
                    if y[ind][i][1]=='IMAX':
                        ss=str(i+1) + '. ' + y[ind][i][0] + ' - 数字IMAX (' + str(w) +'m × ' + str(h) +'m = ' + str(area) + 'm^2)'
                    if y[ind][i][1]=='GT':
                        ss=str(i+1) + '. ' + y[ind][i][0] + ' - 一代激光IMAX GT (' + str(w) +'m × ' + str(h) +'m = ' + str(area) + 'm^2)'
                    if y[ind][i][1]=='cola':
                        ss=str(i+1) + '. ' + y[ind][i][0] + ' - 二代激光IMAX Commercial Laser (' + str(w) +'m × ' + str(h) +'m = ' + str(area) + 'm^2)'
                    if y[ind][i][1]=='xt':
                        ss=str(i+1) + '. ' + y[ind][i][0] + ' - 三代激光IMAX XT (' + str(w) +'m × ' + str(h) +'m = ' + str(area) + 'm^2)'

                    draw.text((place_x, place_y-5*res-13*res*(m+1)+i*13*res),ss, font=font, fill=RGB2BGR(colors.hex2color(colors.cnames[color[i]])))
                    if (i==0) | (i==int(m*0.25)) | (i==int(m*0.5)) | (i==int(m*0.75)) | (i==m-1):
                        draw.text((x1, y2+5*res),str(i+1), font=font, fill=RGB2BGR(colors.hex2color(colors.cnames[color[i]])))

                    img = np.array(img_pil)
                    cv2.rectangle(img, (x1, y1), (x2, y2), color=RGB2BGR(colors.hex2color(colors.cnames[color[i]])), thickness=3)
                city = list(y[ind][0][0])
                cv2.imwrite('./size/' + city[0] + city[1]+'.png',img)

            x=np.zeros((50,3),dtype=np.float)
            y=np.zeros(shape=(50,2)).astype(np.str_)
            m=0
            n=1
            file=file+1
            img = np.ones((1000*res,1000*res,3),np.uint8)*255 
            continue
        if n==1:
            m=m+1
            name1=line.split("\n", 2)[0]
            name2=name1.split(" ", 3)
            x[m-1,0]=name2[0]
            x[m-1,1]=name2[1]
            x[m-1,2]=name2[2]
            nn1 = name.split("\n", 2)[0]
            nn2=nn1.split(" ", 2)

            y[m-1,0] = nn2[0]
            y[m-1,1] = nn2[1]
