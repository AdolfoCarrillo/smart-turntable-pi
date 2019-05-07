from PIL import Image

im = Image.open('cam1.jpg') # Can be many different formats.
pix = im.load()
print (im.size)  # Get the width and hight of the image for iterating over
w = im.size[0]
h = im.size[1]
band = 20
bandw = band*2 + 1
numOfPix = w*h
s = 0
highBound = int(h/2) - band
lowBound = int(h/2) + band
leftBound = 60
rightBound = w-250
mergeW = 3

hi = 0
lo = 255
#grayscale
for i in range(leftBound, rightBound+1):
    for j in range(highBound,lowBound):
        (a,b,c) = pix[i,j]
        z = (a+b+c)/3
        z = int(z)
        if(z>hi): hi = z
        elif(z<lo): lo = z
        pix[i,j] = (z,z,z)

rat = 255/(hi-lo)

#################################################
## Should try area based contrast in next version
#################################################

#bump contrast
for i in range(leftBound, rightBound+1):
    for j in range(highBound,lowBound):
        z = pix[i,j][0] - lo
        z = z*rat
        z = int(z)
        pix[i,j] = (z,z,z)

hi = 0
lo = 255
#horizontal contrast
for i in range(leftBound, rightBound):
    for j in range(highBound,lowBound):
        z = pix[i,j][0] - pix[i+1,j][0]
        if(z>255): z=255
        elif(z<0): z=0
        if(z>hi): hi = z
        elif(z<lo): lo = z
        pix[i,j] = (z,z,z)

rat = 255/(hi-lo)
print(lo)
print(hi)
print(rat)
#bump contrast
for i in range(leftBound, rightBound):
    for j in range(highBound,lowBound):
        z = pix[i,j][0] - lo
        z = z*rat
        z = int(z)
        pix[i,j] = (z,z,z)

#vertical merge
for i in range(leftBound, rightBound):
    s = 0
    count = 0
    for j in range(highBound,lowBound):
        s += pix[i,j][0]
        count += 1
    s = int(s/count * rat)
    if(s > 255): s = 255
    for j in range(highBound,lowBound):
        pix[i,j] = (s,s,s)

tc = 1
tl = [0,0,0]
tl = []
tl.append(0)
#select
for i in range(leftBound, rightBound):
    j = h/2
    z = pix[i,j][0]
    if(z>200):
        pix[i,j] = (255,0,0)
        if(tc == 1):
            tc += 1
            tl.append(i)
        elif(i - tl[tc-1] < 10):
            tl[tc-1] = i
        else:
            tc += 1
            tl.append(i)
            
for i in range(len(tl)):
    tl[i] = int(tl[i]*1.2 +165+9*i)

print(tl)
print(tc)
    

        

##im.save('contrast2.png')  # Save the modified pixels as .png
print('Done')
