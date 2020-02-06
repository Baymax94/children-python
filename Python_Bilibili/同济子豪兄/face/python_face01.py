import cv2

# 读入一张图片，引号里为图片的路径，需要你自己手动设置
img = cv2.imread('image6.png',1)

# 导入人脸级联分类器引擎，'.xml'文件里包含训练出来的人脸特征
face_engine = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
# 用人脸级联分类器引擎进行人脸识别，返回的faces为人脸坐标列表，1.3是放大比例，5是重复识别次数
faces = face_engine.detectMultiScale(img,scaleFactor=1.3,minNeighbors=5)

# 对每一张脸，进行如下操作
for (x,y,w,h) in faces:
    # 画出人脸框，蓝色（BGR色彩体系），画笔宽度为2
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

# 在"img2"窗口中展示效果图
cv2.imshow('img2',img)
# 监听键盘上任何按键，如有按键即退出并关闭窗口，并将图片保存为output.jpg
cv2.waitKey(0)
cv2.destroyAllWindows()
# cv2.imwrite('output.jpg',img)