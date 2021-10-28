import cv2
import numpy as np

resim1=cv2.imread("kelebek.jpg")

#resmiiki kat büyüteceğiz
ikikat=cv2.pyrUp(resim1)
cv2.imshow("orjinal resim",resim1)
cv2.imshow("buyutulmuş resim",ikikat)

print("orjinal resim",resim1.shape)
print("büyümüş",ikikat.shape)

#küçültme işlemi yapalım.
yarim=cv2.pyrDown(resim1)
cv2.imshow("küçüktülmüş",yarim)
print("küçüktülmüş",yarim.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()