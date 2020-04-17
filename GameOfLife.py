# -*- coding: utf-8 -*-
import numpy as np
from GameOfLife_utils import readRLE, plotcells, get_history, makeMovie

''' Initial board '''

## Random board 60x60 with 20% alive
#B = np.random.choice(2,(60,60),p=[0.8,0.2]).astype(bool)

################################

def do_it(pattern,shapeY,pos,T,trim=False,rH=False, rV=False, tp=False):
    ''' Load a pattern from an RLE file, run evolution and make a movie
    Options :
    * pos = where to position the pattern on the board
    * rH, rV and tp to reverse horizontal, vertical or transpose the dimensions    
    * trim : trim edges for nicer plot    
    '''
    # 16/9 ratio
    shape = (int(1.78*shapeY),shapeY)
    
    # Read RLE file in the rle folder
    B = readRLE("rle/"+pattern+".rle", shape, pos,rH=rH,rV=rV, tp=tp)    
    history = get_history(B,T)
    
    plotcells(history[0,:,:],"output/"+pattern+"_init.png")
    plotcells(history[-1,:,:],"output/"+pattern+"_end.png")
    makeMovie(history,"output/"+pattern+".mp4",trim=trim)

################################

#pattern = "example1"
#shapeY = 10
#pos = (6,4)
#T = 15
#do_it(pattern,shapeY,pos,T)

#pattern = "blinker"
#shapeY = 9
#pos = (6,4)
#T = 30
#do_it(pattern,shapeY,pos,T)

#pattern = "four"
#shapeY = 9
#pos = (6,4)
#T = 10
#do_it(pattern,shapeY,pos,T)

#pattern = "five"
#shapeY = 18
#pos = (13,8)
#T = 20
#do_it(pattern,shapeY,pos,T)
    
#pattern = "example2"
#shapeY = 10
#pos = (7,4)
#T = 15
#do_it(pattern,shapeY,pos,T)

#pattern = "stills"
#shapeY = 24
#pos = (8,2)
#T = 4
#do_it(pattern,shapeY,pos,T)
    
#pattern = "oscillos"
#shapeY = 16
#pos = (4,2)
#T = 30
#do_it(pattern,shapeY,pos,T)
    
#pattern = "beehiveplus"
#shapeY = 20
#pos = (15,7)
#T = 30
#do_it(pattern,shapeY,pos,T)

#pattern = "stairs6"
#shapeY = 28
#pos = (22,13)
#T = 100
#do_it(pattern,shapeY,pos,T)

pattern = "Rpento"
shapeY = 100
pos = (70,55)
T = 1500
do_it(pattern,shapeY,pos,T,trim=True)

#pattern = "cthulhu"
#shapeY = 17
#pos = (9,2)
#T = 10
#do_it(pattern,shapeY,pos,T,rV=True)
    
#pattern = "exploder"
#shapeY = 20
#pos = (15,7)
#T = 100
#do_it(pattern,shapeY,pos,T)
    
#pattern = "ten"
#shapeY = 15
#pos = (8,7)
#T = 100
#do_it(pattern,shapeY,pos,T)

#pattern = "104P177"
#shapeY = 70
#pos = (40,12)
#T = 1000
#do_it(pattern,shapeY,pos,T)
    
#pattern = "spaceships"
#shapeY = 40
#pos = (60,9)
#T = 130
#do_it(pattern,shapeY,pos,T,rH=True)
    
#pattern = "canadagoose"
#shapeY = 50
#pos = (50,35)
#T = 150
#do_it(pattern,shapeY,pos,T,rV=True,rH=True)
    
#pattern = "60P5H2V0"
#shapeY = 50
#pos = (3,16)
#T = 200
#do_it(pattern,shapeY,pos,T,rV=True,rH=True, tp=True)
    
#pattern = "puffer1"
#shapeY = 150
#pos = (5,65)
#T = 600
#do_it(pattern,shapeY,pos,T,rV=True,tp=True)

#pattern = "backrake3"
#shapeY = 200
#pos = (5,90)
#T = 500
#do_it(pattern,shapeY,pos,T,rV=True,tp=True, trim=True)

#pattern = "linepuffer"
#shapeY = 300
#pos = (50,65)
#T = 800
#do_it(pattern,shapeY,pos,T,rV=True,tp=True)
    
#pattern = "gosperglidergun"
#shapeY = 60
#pos = (5,5)
#T = 200
#do_it(pattern,shapeY,pos,T)

#pattern = "10cellinfinitegrowth"
#shapeY = 360
#pos = (400,300)
#T = 4000
#do_it(pattern,shapeY,pos,T,trim=True)
    
#pattern = "breeder1"
#shapeY = 1080
#pos = (10,400)
#T = 2500
#do_it(pattern,shapeY,pos,T,rV=True, trim=True )   
    
#pattern = "max"
#shapeY = 720
#pos = (640,360)
#T = 1000 # 1000
#do_it(pattern,shapeY,pos,T, trim=True)   
    
#pattern = "p41660p5h2v0gun"
#shapeY = 1200
#pos = (500,100)
#T = 5000 # 1000
#do_it(pattern,shapeY,pos,T, trim=True)   
    
#pattern = "otcametapixeloff"
#shapeY = 2200
#pos = (800,50)
#T = 1000 # 1000
#do_it(pattern,shapeY,pos,T)   




## Random 20% alive
#for s in range(100):
#    np.random.seed(s)
#    B = np.random.choice(2,(3*16,3*9),p=[0.85,0.15]).astype(bool)
#    T = 300
#    history = get_history(B,T)
#    #plotcells(history[0,:,:],"output/random"+str(s)+"_init.png")
#    plotcells(history[-1,:,:],"output/random"+str(s)+"_end.png")
#    #makeMovie(history,"output/random"+str(s)+".mp4")
 
#s = 1
#np.random.seed(s)
#B = np.random.choice(2,(3*16,3*9),p=[0.85,0.15]).astype(bool)
#T = 100
#history = get_history(B,T)
#plotcells(history[0,:,:],"output/random"+str(s)+"_init.png")
#plotcells(history[-1,:,:],"output/random"+str(s)+"_end.png")
#makeMovie(history,"output/random"+str(s)+".mp4")


