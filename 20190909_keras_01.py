import os
import cv2


classifier = cv2.CascadeClassifier('lbpcascade_animeface.xml')


image = cv2.imread('sample.jpg')

gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
faces = classifier.detectMultiScale(gray_image)
print(faces)


output_dir = 'faces'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for i, (x,y,w,h) in enumerate(faces):
    face_image = image[y:y+h, x:x+w]
    output_path = os.path.join(output_dir,'{0}.jpg'.format(i))
    cv2.imwrite(output_path,face_image)

'''
for x,y,w,h in faces:
    cv2.rectangle(image, (x,y), (x+w,y+h), color=(0,0,255), thickness=3)

cv2.imwrite('faces.jpg',image)
'''