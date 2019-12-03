'''
程序：人脸检测与识别
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
import cv2

#创建人脸检测器和识别器
names = ('None', 'Spider Man', 'Iron Man')
file = 'lbpcascade_frontalface_improved.xml'
face_cascade = cv2.CascadeClassifier(file)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner.yml')

#读取测试的人脸图像
test_img = cv2.imread('testing/test1.jpg')
gray_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_img, 1.2, 5)

#对检测出的每一个人脸图像进行测试
for (x, y, w, h) in faces:
    face = gray_img[y:y+w, x:x+h]
    face = cv2.resize(face, (256, 256))
    #使用人脸识别器预测图像
    label, confidence = recognizer.predict(face)
    confidence = 100 - confidence
    #取最大值
    if label > 0 and confidence > 50 :
        cv2.rectangle(test_img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        text = '%s:%d' % (names[label], confidence)
        print(text)
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(test_img, text, (x, y), font, 2.5, (0, 255, 0), 2)

#显示图像并等待
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.imshow('Image', test_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
