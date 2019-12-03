import cv2, numpy, os

labels, faces = [], []
file = 'lbpcascade_frontalface_improved.xml'
face_cascade = cv2.CascadeClassifier(file)
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

def detect_face(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5, minSize=(20, 20))
    if (len(faces) == 0):
        return None, None
    (x, y, w, h) = faces[0]
    return gray[y:y+w, x:x+h], faces[0]

def read_face(face_id):
    path = 'dataset/' + str(face_id)
    print('trainning:', face_id)
    files = os.listdir(path)
    for file in files:
        if file.startswith('.'):
            continue
        image = cv2.imread(path + '/' + file)
        face, rect = detect_face(image)
        if face is not None:
            face = cv2.resize(face, (512, 512))
            labels.append(face_id)
            faces.append(face)
        break

if __name__ == '__main__':
    #读取人脸图像
    read_face(1)
    #read_face(2)
    #训练人脸识别器
    face_recognizer.train(faces, numpy.array(labels))
    #保存人脸特征数据
    face_recognizer.save('trainner.yml')
