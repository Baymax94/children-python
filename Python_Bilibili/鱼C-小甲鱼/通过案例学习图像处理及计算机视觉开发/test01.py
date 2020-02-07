import cv2
img=cv2.imread('image1.png',0)
#print(img)
print(img.shape)
cv2.imshow("lenna",img)
cv2.imwrite(r"001.png",img)