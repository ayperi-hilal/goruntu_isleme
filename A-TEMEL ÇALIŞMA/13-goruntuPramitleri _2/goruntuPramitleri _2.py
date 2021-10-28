import cv2
import numpy as np
#öncelikle bir matris ile resim oluşturacağız

resim=np.zeros((300,300,3),dtype="uint8")
print(resim)


cv2.waitKey()
cv2.destroyAllWindows()