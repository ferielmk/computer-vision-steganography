import cv2
#from taceback import print_tb
import numpy as np
import matplotlib.pyplot as plt

'''img_avant=cv2.imread("background_dinosaurs.jpg",cv2.IMREAD_GRAYSCALE)
img_avant[:] = img_avant[:]/2
cv2.imwrite("background.jpg",img_avant)'''

img_avant=cv2.imread("background.jpg",cv2.IMREAD_GRAYSCALE)
if img_avant is None:
    print("erreur de chargement")
    exit(0)

min,max=255,0
h,w = img_avant.shape

for y in range(h):
    for x in range(w):
        if img_avant[y,x]<min:
            min = img_avant[y,x]
        if img_avant[y,x]>max:
            max= img_avant[y,x]

img_apres = np.zeros(img_avant.shape,img_avant.dtype)
for y in range(h):
    for x in range(w):
        img_apres[y,x]=(img_avant[y,x]-min)*255/(max-min)

hist_avant = np.zeros((256,1),np.uint16)
hist_apres=cv2.calcHist([img_apres],[0],None,[256],[0,255])
for y in range(h):
    for x in range(w):
        hist_avant[img_avant[y,x]]+=1 #niveau de degres = img_avant[y,x]

print("min:",min,"max:",max)

plt.figure()
plt.title("image Normalisee")
plt.xlabel("NG")
plt.ylabel("Nb pixels")
plt.plot(hist_avant)
plt.plot(hist_apres)
plt.xlim([0,255])
plt.show()

cv2.imshow("image avant",img_avant)
cv2.imshow("image apres",img_apres)
cv2.waitKey(0)
cv2.destroyAllWindows
