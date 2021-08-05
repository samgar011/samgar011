import cv2
import numpy as np
cap = cv2.VideoCapture(0)
sinirlar = [ 
        
    ([17,15,100],[50,56,200]),
    ([86,31,4],[220,88,50]),
    ([25,146,190],[62,174,250]),
    ([103,86,65],[145,133,128]),
]
while True:
    ret,frame = cap.read() # 30 fps 
    buyumeFaktor = 0.3
    interpolation = cv2.INTER_AREA
    frame = cv2.resize(frame,None,fx=buyumeFaktor,fy=buyumeFaktor,interpolation=interpolation)
    sonuc = None
    dusuk = np.array(sinirlar[3][0],dtype="uint8")
    yuksek = np.array(sinirlar[3][1],dtype="uint8")
    mask = cv2.inRange(frame,dusuk,yuksek)
    cv2.imshow(f"maske",mask)
    sonuc = cv2.bitwise_or(frame,frame,mask=mask)
    cv2.imshow("sonuc",np.hstack([frame,sonuc]))
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()