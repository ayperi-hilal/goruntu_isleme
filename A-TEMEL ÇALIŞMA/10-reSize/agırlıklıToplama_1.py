import cv2
import numpy as np
# pikseller toplandı
kelebek=cv2.imread("kelebek.jpg")
kus=cv2.imread("kus.jpg")

print(kelebek[100,150])
print(kus[50,60])

cv2.imshow("kelebek",kelebek)
cv2.imshow("kus",kus)

print([kelebek[100,150]+kus[50,60]])




cv2.waitKey(0)
cv2.destroyAllWindows()