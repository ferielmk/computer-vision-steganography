import cv2
import numpy as np
#opencv se base sur numpy,je crois il a des fonctionnalites de numpy
img2=cv2.imread("fifi-angry.png",cv2.IMREAD_GRAYSCALE)
if img2 is None:
    print ("Erreur de chargement")
    exit(0)
h,w=img2.shape
print(h,w)

img = np.zeros((h,w),np.uint8)# unsigned integer 8 bits : non signe donc de 0 a 255 au lieu de -127 a 128
img[:]=128#changer pixels de tte l image
#img[100:300,200:600] =128 veut dire les pixels de la ligne 100 a 300 et de la colonne 200 a 600 sont changes a 128

img3=np.zeros(img2.shape,img2.dtype)
img3=img2.copy()
img3[:]=0
for y in range(img2.shape[0]):
   for x in range(img2.shape[1]):
       img3[y,x]=255 - img2[y,x]
cv2.imwrite('test.png',img3)
cv2.imshow("image2",img2)
cv2.imshow("image3",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()

