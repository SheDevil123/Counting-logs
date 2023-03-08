import cv2
import numpy as np

max,min=0,0
input_img=cv2.imread("test_img2.jpg")
#while True:
gray=cv2.cvtColor(input_img,cv2.COLOR_BGR2GRAY)
#cv2.imshow("",input_img)
blur=cv2.GaussianBlur(gray,(9,9),0)
#cv2.imshow("blur",blur)
while True:
    res,frame=cv2.threshold(blur,45,210,cv2.THRESH_BINARY)
    #cv2.imshow("bw",frame)
    frame=cv2.Canny(blur,40,120,L2gradient=False)
    cv2.imshow("canny",frame)
    circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,20,param1=120,param2=40,minRadius=0,maxRadius=100)
    #print(circles)
    circles = np.uint16(np.around(circles))
    print("number of tubes: ", len(circles[0]),end="\r")
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(input_img,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        #cv2.waitKey(50)
        cv2.circle(input_img,(i[0],i[1]),2,(0,0,255),3)
        cv2.imshow("",input_img)
    x=cv2.waitKey(20)
    if x==ord("e"):
        break
    elif x==ord("w"):
        min+=5
        print("min: ",min,"max: ",max)
    elif x==ord("s"):
        min-=5
        print("min: ",min,"max: ",max)
    elif x==ord("i"):
        max+=5
        print("min: ",min,"max: ",max)
    elif x==ord("k"):
        max-=5
        print("min: ",min,"max: ",max)
print("number of tubes: ", len(circles[0]))