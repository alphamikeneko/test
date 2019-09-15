import os
import cv2

import glob

# list = glob.glob("/Users/katasugirupan/Desktop/test2/data/HITAGI/*")
# list = glob.glob("/Users/katasugirupan/Desktop/test2/data/scrin/*")
list = glob.glob("/Users/katasugirupan/Desktop/test2/fate6/*")

classifier = cv2.CascadeClassifier('lbpcascade_animeface.xml')

output_dir = 'faces_fate6'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

n = 0
for i in list:
    print(i)
    image = cv2.imread(i)
    gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces = classifier.detectMultiScale(gray_image)
    # print(faces)

    for j, (x,y,w,h) in enumerate(faces):
        face_image = image[y:y+h, x:x+w]
        resize_image = cv2.resize(face_image,(64,64),interpolation = cv2.INTER_AREA)
        # output_path = os.path.join(output_dir,str(n) + 'h{0}.jpg'.format(j))
        output_path = os.path.join(output_dir,str(n)+'.jpg'.format(j))
        cv2.imwrite(output_path,resize_image)
    
    n += 1

