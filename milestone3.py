
import itertools
from itertools import product

from matplotlib import pyplot as plt 
f = open("Workshop2024\Milestone3\Input\Testcase1.txt", "r")
fout = open("m3t1.txt", "w")
data = f.read()
data=data.split()
diameter = int(data[0][14:])
print(diameter)
die_size = [int(x) for x in data[1][8:].split('x')]
print(die_size)
dieShift=[int(x) for x in data[2][16:-1].split(',')]
print(dieShift)
reference=[int(x) for x in data[3][14:-1].split(",")]
print(reference)
dieStreet= [int(x) for x in data[4][25:-1].split(",")]
print(dieStreet)
reticleStreet=[int(x) for x in data[5][30:-1].split(",")]
print(reticleStreet)
dpr=[int(x) for x in data[6][15:].split('x')]
print(dpr)
rad= diameter/2
x_l=-dieShift[0]-diameter/2
y_b=-dieShift[1]-diameter/2
#x_r=x_l + die_size[0]
#y_t =y_b + die_size[1]
print(x_l)
print(y_b)
xArr=[]
yArr=[]
xCount=0
yCount=0

while(x_l<diameter):
    xCount+=1
    if(xCount>dpr[0]):
        
    xArr.append(x_l)
    x_l=x_l+die_size[0]+dieStreet[0]
while(y_b<diameter):
    yArr.append(y_b)
    y_b=y_b+die_size[1]+dieStreet[1]

lld=[]
for x in xArr:
    for y in yArr:
        lld.append([x, y])
#print(lld)
finPoints=[]
for x, y in lld:
    check1=((x)**2 + (y)**2 < rad**2) 
    check2= ((x+die_size[0])**2 + (y)**2 <rad**2)
    check3=((x)**2 +(y+die_size[1])**2<rad**2)
    check4=((x+die_size[0])**2 + (y+die_size[1])**2<rad**2)
    arr=[check1, check2, check3, check4]
    tr=arr.count(True)
    if(tr>=1):
        finPoints.append([x, y])

zind=[]
for x,y in finPoints:
    if(x<reference[0]<x+die_size[0] and y<reference[1]<y+die_size[1]):
        zind= [x, y]
print("zind: ",zind)
for val in finPoints:
    x=val[0]
    y=val[1]
    dx = x - zind[0]
    dy = y - zind[1]
    xind = dx/die_size[0]
    yind = dy/die_size[1]
    val.append([int(xind), int(yind)])
xv= [finPoints[x][0] for x in range(len(finPoints))]
yv = [finPoints[y][1] for y in range(len(finPoints))]
plt.plot(xv, yv)

for points in finPoints:
    st = "("+str(points[2][0])+","+ str(points[2][1])+"):("+str(points[0])+','+str(points[1])+")"
    if(points[2][0]==-11):    
        print(st)
    fout.write(st)
    fout.write('\n')
fout.close()


'''
x=-150
y=-120

print(rad**2)
print(x**2 + y**2)
print((x+die_size[0])**2 + (y)**2)
print((x)**2 + (y+die_size[1])**2)
print((x+die_size[0])**2 + (y+die_size[1])**2)
'''
print(len(finPoints))