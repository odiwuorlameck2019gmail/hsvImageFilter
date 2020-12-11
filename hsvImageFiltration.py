import cv2 
import numpy as np 
import time 



#Callback method that  that goes into the  trackbar funtion.
def doNothing(x):
    pass

#Initialize the webcam feed.
cap=cv2.VideoCapture(0)
cap.set(3,12290)
cap.set(4,720)

#Create a window named Trackbar.
cv2.namedWindow("Trackbars")

#Create trackbars to control  the lower and upper range  of  H,S,V  channels  and place them on Trackbars.
cv2.createTrackbar("Lower-Hue","Trackbars",0,179,doNothing)
cv2.createTrackbar("Lower-Saturation","Trackbars",0,255,doNothing)
cv2.createTrackbar("Lower-Value","Trackbars",0,255,doNothing)

cv2.createTrackbar("Upper-Hue","Trackbars",179,179,doNothing)
cv2.createTrackbar("Upper-Saturation","Trackbars",255,255,doNothing)
cv2.createTrackbar("Upper-Value","Trackbars",255,255,doNothing)


while True:
    #Read frames frame the webcam.
    check,frame=cap.read()
    if not check:
        break
    #Flip the frame Horizontally.
    frame=cv2.flip(frame,1)
    #Convert image from BGR to hsv.
    hsvImage=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #Get values from Trackbar .
    lower_hue=cv2.getTrackbarPos("Lower-Hue","Trackbars")
    lower_saturation=cv2.getTrackbarPos("Lower-Saturation","Trackbars")
    lower_value=cv2.getTrackbarPos("Lower-Value","Trackbars")

    higher_hue=cv2.getTrackbarPos("Upper-Hue","Trackbars")
    higher_saturation=cv2.getTrackbarPos("Upper-Saturation","Trackbars")
    higher_value=cv2.getTrackbarPos("Upper-Value","Trackbars")

    #Set the Lower and upper hsv range.
    lower_range=np.array([lower_hue,lower_saturation,lower_value])
    upper_range=np.array([higher_hue,higher_saturation,higher_value])

    #Filter the image and get th binary Mask,where white  space represents  the  target color.
    mask=cv2.inRange(hsvImage,lower_range,upper_range)

    #You can also visualize  the real part of the color .
    result=cv2.bitwise_and(frame,frame,mask=mask)
    #Convert the  binary mask to three color channel  image .
    three_color_channel_mask=cv2.cvtColor(mask,cv2.COLOR_RGB2BGR)
    
    #Stack all of the three images together that is three_color_channel_mask ,frame and  res.
    stacked=np.hstack((three_color_channel_mask,frame,result))

    #show  stacked Image .
    cv2.imshow("Trackbars",cv2.resize(stacked,(1000,400)))
    key=cv2.waitKey(1)
    if key==ord("q"):
        break
    elif key==ord('s'):
        hsvarray=[[lower_hue,lower_saturation,lower_value],[higher_hue,higher_saturation,higher_value]]
        print(hsvarray)

        #Save the array as value.npy
        np.save("value",hsvarray)
        break 
    


cv2.release()
cv2.destroyAllWindows()             





