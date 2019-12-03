'''
程序：训练人脸识别器，生成人脸特征数据
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
import cv2, numpy, os

#创建人脸检测器和识别器
labels, faces = [], []
file = 'lbpcascade_frontalface_improved.xml'
face_cascade = cv2.CascadeClassifier(file)
recognizer = cv2.face.LBPHFaceRecognizer_create()

def detect_face(image):
    '''检测人脸区域'''
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5, minSize=(20, 20))
    if (len(faces) == 0):
        return None
    (x, y, w, h) = faces[0]
    return gray[y:y+w, x:x+h]

def read_face(label, images_path):
    '''读取人脸图像'''
    print('trainning:', label, images_path)
    files = os.listdir(images_path)
    for file in files:
        if file.startswith('.'):
            continue
        #从文件中读取图像
        image = cv2.imread(images_path + '/' + file)
        #检测图像中的人脸区域
        face = detect_face(image)
        if face is not None:
            face = cv2.resize(face, (256, 256))
            faces.append(face)
            labels.append(label)

if __name__ == '__main__':
    #读取人脸图像
    read_face(1, 'training/spider_man/')
    read_face(2, 'training/iron_man/')
    #训练人脸识别器
    recognizer.train(faces, numpy.array(labels))
    #保存人脸特征数据
    recognizer.save('trainner.yml')
