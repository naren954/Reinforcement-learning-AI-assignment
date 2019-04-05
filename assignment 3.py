import copy
import numpy as np

def valueiter(gridn,endx,endy):
    global s
    util=[0]*s
    utild=[0]*s
    pol=[0]*s
    for i in range(s):
        util[i]=[0]*s
        utild[i]=[0]*s
        pol[i]=[0]*s
    #utild[endy][endx]=99
    k=0
    while(1):
        k+=1
        delta=0
        util=copy.deepcopy(utild)
        for x in range(s):
            for y in range(s):
                #if(gridn[x][y]==99):
                  #  continue
                nx=x-1
                ry=y+1
                sx=x+1
                ly=y-1
                if nx<0:
                    nx=0
                if ry==s:
                    ry=s-1
                if sx==s:
                    sx=s-1
                if ly<0:
                    ly=0
                for i in range(4):
                    if i==0:
                        su=np.float64(0.7*util[nx][y]+0.1*util[x][ry]+0.1*util[sx][y]+0.1*util[x][ly])
                        maxs=su-1
                    elif i==1:
                        su=np.float64(0.1*util[nx][y]+0.7*util[x][ry]+0.1*util[sx][y]+0.1*util[x][ly])
                    elif i==2:
                        su=np.float64(0.1*util[nx][y]+0.1*util[x][ry]+0.7*util[sx][y]+0.1*util[x][ly])
                    elif i==3:
                        su=np.float64(0.1*util[nx][y]+0.1*util[x][ry]+0.1*util[sx][y]+0.7*util[x][ly])
                    if(su>maxs):
                        maxs=su
                        pol[x][y]=i
                    if su==maxs:
                        if i==2 and pol[x][y]==1:
                            pol[x][y]=2
                if(gridn[x][y]!=99):
                    utild[x][y]=gridn[x][y]+0.9*maxs
                else:
                    utild[x][y]=gridn[x][y]
                if abs(utild[x][y]-util[x][y])>delta:
                    delta=abs(utild[x][y]-util[x][y])
        val=np.float64(1)/9
        if delta<0.1*val:
            break
    print util
    return pol

f=open("input.txt","r")
out=open("output.txt","w")
s=int(f.readline())
n=int(f.readline())
o=int(f.readline())
start=[]
end=[]
grid=[-1]*s
utild=[0]*s
for i in range(s):
    grid[i]=[-1]*s
    utild[i]=[0]*s
for i in range(o):
    pos=f.readline().rstrip()
    intpos=pos.split(',')
    intx=int(intpos[0])
    inty=int(intpos[1])
    grid[inty][intx]-=100
for i in range(n):
    start.append(f.readline().rstrip())
for i in range(n):
    end.append(f.readline().rstrip())

for i in range(n):
    startpos=start[i].split(',')
    startx=int(startpos[0])
    starty=int(startpos[1])
    endpos=end[i].split(',')
    endx=int(endpos[0])
    endy=int(endpos[1])
    gridn=[-1]*s
    for m in range(s):
        gridn[m]=[-1]*s
    gridn=copy.deepcopy(grid)
    gridn[endy][endx]+=100
    pol=valueiter(gridn,endx,endy)
    mon=0
    for j in range(10):
            pos=[starty,startx]
            np.random.seed(j)
            sw=np.random.random_sample(1000000)
            k=0
            if pos==[endy,endx]:
                mon+=100
            while pos!=[endy,endx]:
                x=pos[0]
                y=pos[1]
                mov=pol[x][y]
                if sw[k]>0.7:
                    if sw[k]>0.8:
                        if sw[k]>0.9:
                            mov=(mov+2)%4
                        else:
                            mov=(mov+1)%4
                    else:
                        mov=(mov-1)%4
                k+=1
                nx=x-1
                ry=y+1
                sx=x+1
                ly=y-1
                if nx<0:
                    nx=0
                if ry==s:
                    ry=s-1
                if sx==s:
                    sx=s-1
                if ly<0:
                    ly=0
                if mov==0:
                    pos=[nx,y]
                elif mov==1:
                    pos=[x,ry]
                elif mov==2:
                    pos=[sx,y]
                elif mov==3:
                    pos=[x,ly]
                mon+=gridn[pos[0]][pos[1]]
            #print mon-mon1
    mon=np.floor(mon/10)
    mon=int(mon)
    print mon
    out.write(str(int(mon))+'\n')