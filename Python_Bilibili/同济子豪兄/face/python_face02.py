#导入opencv
import cv2

# 导入人脸级联分类器引擎，'.xml'文件里包含训练出来的人脸特征，cv2.data.haarcascades即为存放所有级联分类器模型文件的目录
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
# 导入人眼级联分类器引擎吗，'.xml'文件里包含训练出来的人眼特征
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')

# 读入一张图片，引号里为图片的路径，需要你自己手动设置
img = cv2.imread('image1.png')

# 用人脸级联分类器引擎进行人脸识别，返回的faces为人脸坐标列表，1.3是放大比例，5是重复识别次数
faces = face_cascade.detectMultiScale(img, 1.3, 5)

# 对每一张脸，进行如下操作
for (x,y,w,h) in faces:
    # 画出人脸框，蓝色（BGR色彩体系），画笔宽度为2
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    # 框选出人脸区域，在人脸区域而不是全图中进行人眼检测，节省计算资源
    face_area = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(face_area)
    # 用人眼级联分类器引擎在人脸区域进行人眼识别，返回的eyes为眼睛坐标列表
    for (ex,ey,ew,eh) in eyes:
        #画出人眼框，绿色，画笔宽度为1
        cv2.rectangle(face_area,(ex,ey),(ex+ew,ey+eh),(0,255,0),1)
        
# 在"img2"窗口中展示效果图
cv2.imshow('img2',img)
# 监听键盘上任何按键，如有案件即退出并关闭窗口，并将图片保存为output.jpg
cv2.waitKey(0)
cv2.destroyAllWindows()
# cv2.imwrite('output.jpg',img)