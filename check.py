#-*- coding:utf-8 -*-
import cv2
import numpy as np

def main():
    
    img = cv2.imread("lena.jpg")

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
      
    ret, th2 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)    

    cv2.imwrite("lena.jpg", th2)

    cv2.imshow('check',th2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
