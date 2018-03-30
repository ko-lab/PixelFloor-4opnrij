import pixelvloer
import random
from time import sleep

vloerarray = [random.randint(0,150) for _ in range(122)]


kolab = [0,3,7,8,9,11,13,17,21,22,23,28,32,33,35,39,43,44,47,51,52,53,66,71,74,75,77,81,83,85,87,88,92,93,94,96,97,99,103,105,107,109,110,111,112,114,116,118,119]
kolab90 = [110,77,33,22,11,111,89,45,1,112,101,46,2,113,91,47,3,114,81,37,26,15,116,61,28,17,117,73,51,29,7,118,74,63,52,30,19,119,75,53,31,9,120,109,98,76,54,32,21]
teller = 0

fade=[0,0,0,1]

while 1:
    for i in range(0,121):
        vloerarray[i] -= fade[random.randint(0,3)]
        if vloerarray[i] < 0:
            vloerarray[i] = random.randint(50,175)
        pixelvloer.zetveel(i,0,vloerarray[i],0)
    for j in kolab:
        if teller < 1000:
             pixelvloer.zetveel(120-j,255,random.randint(0,vloerarray[j]/2),random.randint(0,vloerarray[j+1]/2))
        if (teller > 2000) and (teller < 3000):
             pixelvloer.zetveel(j,255,random.randint(0,vloerarray[j]/2),random.randint(0,vloerarray[j+1]/2))

    for j in kolab90:
        if (teller > 1000) and (teller < 2000):
             pixelvloer.zetveel(120-j,255,random.randint(0,vloerarray[j]/2),random.randint(0,vloerarray[j+1]/2))
        if teller > 3000:
             pixelvloer.zetveel(j,255,random.randint(0,vloerarray[j]/2),random.randint(0,vloerarray[j+1]/2))

    if teller > 4000:
        teller=0

    pixelvloer.updatevloer()
    teller+=1
