import cv2
import dlib
from face_recognition.api import face_encodings
import numpy as np
import face_recognition
#from face_recognition.api import face_encodings,face_locations

#bu kısımda işlem yapabilmek için önce
# cmake indilirdi ve kuruldu. ardından dlib kuruldu ve son olarakta face_recognition import edildi. 
# ben araştırarak yaptım ve neredeyse bir günümü aldı. cmake kendi sitesinden ndirirken dlib için 
# paylaştığım derleyiciyi kullanmanızı tavsiye ederim zaten face_recognition kolay oluyor. 
# bu arada wheel kurmakta gerekecek en başta. onu söylemeyi unuttum :)

detector=dlib.get_frontal_face_detector()

#bir resim yükleyip adını verelim.
#yüklediğimiz resmi encoding yapalım

ayperi=face_recognition.load_image_file("ayperi.jpg")
ayperi_enc=face_recognition.face_encodings(ayperi)[0]



# opencv metodu olan VideoCapture ile webcam'den görüntü almayı başlatıyoruz
# 0 default webcam video_capture = cv2.VideoCapture(0)



video=cv2.VideoCapture(0)






while True:
    # Videodan anlık bir kare yakalıyoruz
    ret, frame = video.read()

    face_loc=[]


    faces=detector(frame)
    for face in faces:
        x=face.left()
        y=face.top()
        w=face.right()
        h=face.bottom()

        face_loc.append((y,w,h,x))



    #face_loc=face_recognition.face_locations(frame)
    face_encoding=face_recognition.face_encodings(frame,face_loc)


    i=0


    for face in face_encoding:

        y,w,h,x=face_loc[i]





        sonuc=face_recognition.compare_faces([ayperi_enc],face)
        print(sonuc)


        if sonuc[0]==True:
            cv2.rectangle(frame,(x,y),(w,h),(255,0,0),2)
            cv2.putText(frame,"ayperi",(x,h+35),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)

        else:
            
            cv2.rectangle(frame,(x,y),(w,h),(255,0,0),2)
            cv2.putText(frame,"bilinmeyeni",(x,h+35),cv2.FONT_HERSHEY_COMPLEX,3,(0,250,255),4)

    cv2.imshow("görsel",frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Kamerayı kapat
video.release()
cv2.destroyAllWindows()