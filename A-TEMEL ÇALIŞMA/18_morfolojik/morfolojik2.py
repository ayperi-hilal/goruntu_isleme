from os import close
import cv2
import numpy as np

image=cv2.imread("yazi.jpg")
#gürültü giderme diration genişletme
kernel=np.ones((5,5),np.uint8)

erosion=cv2.erode(image,kernel,iterations=1)
dilation=cv2.dilate(erosion,kernel,iterations=1)

opening=cv2.morphologyEx(image,cv2.MORPH_OPEN,kernel)#erosion + dilation işlemini yapıyor
closing=cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel)#dilation + erosion işlemini yapıyor

gradyan=cv2.morphologyEx(image,cv2.MORPH_GRADIENT,kernel)#dilation - erosion işlemini yapıyor


tophat=cv2.morphologyEx(image,cv2.MORPH_TOPHAT,kernel)#image-opening=image-erosion - dilation yani sadece gürültü kısmını veriyoru

blachat=cv2.morphologyEx(image,cv2.MORPH_BLACKHAT,kernel)#İMAGE-CLOSİNG

cv2.imshow("dilation",dilation)
cv2.imshow("orjinal resim",image)
cv2.imshow("opening",opening)
cv2.imshow("closing",closing)
cv2.imshow("Gradyan",gradyan)
cv2.imshow("tophat",tophat)
cv2.imshow("blacha",blachat)

cv2.waitKey(0)
cv2.destroyAllWindows()

#SONUÇ OLARAK BENİM RESMİM ÇOK FAZLA GÜRÜLTÜLÜ OLDUĞU İİN ÇOK SAĞLIKLI SONUÇ ALAMADIM AMA GÜZEL RESİMLERDE GÜZEL SONUÇLKAR ALINIR.
