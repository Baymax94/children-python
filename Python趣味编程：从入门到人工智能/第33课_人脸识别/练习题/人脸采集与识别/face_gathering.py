import cv2, os, time

#创建人脸检测器
file = 'lbpcascade_frontalface_improved.xml'
face_detector = cv2.CascadeClassifier(file)

# 输入用户ID，采集用户人脸图像
face_id = input('请输入用户ID：')
path = 'dataset/' + face_id
if os.path.exists(path):
    print('用户ID %s 已存在.' % face_id)
    exit()
else:
    os.mkdir(path)

#打开摄像头
cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)

print('请看着摄像头，1秒后开始采集人脸...')
ret, img = cam.read()
time.sleep(1)

#采集30张人脸图像
count = 0
while(count < 30):
    #读取视频帧，检测出人脸
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    if len(faces) == 0: continue
    
    (x,y,w,h) = faces[0]
    #标注矩形框
    cv2.rectangle(img, (x,y), (x+w,y+h), (255, 0, 0), 2)     
    count += 1
    #保存人脸图像
    cv2.imwrite(path + '/' + str(count) + '.jpg', gray[y:y+h, x:x+w])
    cv2.imshow('Image', img)

    cv2.waitKey(100)
 
#采集完毕
print('采集完毕')
cam.release()
cv2.destroyAllWindows()
