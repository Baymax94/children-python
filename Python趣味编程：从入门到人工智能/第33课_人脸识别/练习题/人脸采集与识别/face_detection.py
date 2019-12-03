import cv2

#创建人脸检测器和识别器
names = ('None', 'Baba', 'Mama')
file = 'lbpcascade_frontalface_improved.xml'
face_cascade = cv2.CascadeClassifier(file)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner.yml')

#打开摄像头
cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)

while True:
    ret, frame_img = cam.read()
    gray_img = cv2.cvtColor(frame_img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img, 1.2, 5)
        
    #对检测出的每一个人脸图像进行测试
    for (x, y, w, h) in faces:
        face = gray_img[y:y+w, x:x+h]
        face = cv2.resize(face, (512, 512))
        #使用人脸识别器预测图像
        label, confidence = recognizer.predict(face)
        confidence = 100 - confidence
        print(label, confidence)
        if label > 0 and confidence > 50 :
            cv2.rectangle(frame_img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            text = '%s:%d' % (names[label], confidence)
            font = cv2.FONT_HERSHEY_PLAIN
            cv2.putText(frame_img, text, (x, y), font, 1.5, (0, 255, 0), 1)

    cv2.imshow('Camera', frame_img)
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break

#关闭摄像头和窗口
cam.release()
cv2.destroyAllWindows()
