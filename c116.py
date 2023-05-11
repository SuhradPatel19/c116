import cv2


image=cv2.imread("solar-system.jpg")
cv2.putText(image,"Sun",(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
cv2.putText(image,"Mercury",(115,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
cv2.putText(image,"Venus",(185,275),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
cv2.putText(image,"Earth",(285,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
cv2.putText(image,"Mars",(370,275),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
cv2.putText(image,"Jupiter",(550,150),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
cv2.putText(image,"Saturn",(750,150),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
cv2.putText(image,"Uranus",(950,150),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
cv2.putText(image,"Neptune",(1125,150),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255),1)
cv2.imwrite("planets.png",image)
cv2.imshow("image",image)
cv2.waitKey(0)
