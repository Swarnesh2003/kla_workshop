import math
f = open("Workshop2024\Milestone1\Input\Testcase4.txt", "r")
fout = open("output1.txt", "w")
data = f.read()
data=data.split()
diameter = int(data[0][14:])
print(diameter)
n_points = int(data[1][15:])
print(n_points)
angle=int(data[2][6:])%180
print(angle)
rad= diameter/2
first_angle=180+angle
first_x= round(rad*math.cos(math.radians(first_angle)),4)
first_y = round(rad*math.sin(math.radians(first_angle)), 4)
last_x = round(rad*math.cos(math.radians(angle)), 4)
last_y = round(rad*math.sin(math.radians(angle)) , 4)
print(first_x, first_y)
print(last_x, last_y)

dist= round(diameter/(n_points-1), 4)
arr=[[first_x, first_y]] 

temp_x=first_x
temp_y=first_y
if(first_x>last_x):
    first_x, last_x = last_x, first_x
if(first_y>last_y):
    first_y, last_y = last_y, first_y
fout.write(str((temp_x, temp_y)))
fout.write('\n')
print(n_points)
for i in range(n_points):
    new_x = temp_x + dist*math.cos(math.radians(angle))
    new_y = temp_y + dist*math.sin(math.radians(angle))
    print(first_x, first_y)
    print(new_x, new_y)
    print(last_x, last_y)
    fout.write('\n')
    if(first_x<=round(new_x, 2)<=last_x and first_y<=round(new_y, 2)<=last_y):
        arr.append([round(new_x,4), round(new_y, 4)])
        temp_x = new_x
        temp_y = new_y
        fout.write(str((round(new_x,4), round(new_y, 4))))
print(len(arr))
print(arr)
xs = [x[0] for x in arr]
ys = [x[1] for x in arr]
f.close()