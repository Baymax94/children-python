import cv2
img=cv2.imread("image1.png",0)
cv2.imshow("Lenna",img)
k=cv2.waitKey(0)
if k==27:
    cv2.destroyWindow("Lenna")
elif k==115:
    cv2.imwrite(r"002.jpg",img)
    cv2.destroyWindow("Lenna")