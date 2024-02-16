import cv2
import os


path = 'images'

images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        #print(file_name)
               
        images.append(file_name)
count = len(images)
frame = cv2.imread(images[1])
height, width, channels = frame.shape
size = (width,height)

vid = cv2.VideoWriter('friends.mp4',cv2.VideoWriter_fourcc(*'divx'),15,size)

for i in range(0,count,1):
    vid1 = cv2.imread(images[i])
    vid.write(vid1)
