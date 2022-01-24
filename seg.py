import os
import cv2
from tqdm import tqdm

ori_list = os.listdir("./original")

txt_list = os.listdir("./labels")

image = cv2.imread("./original/" + ori_list[0])

for i in tqdm(ori_list):
    img = cv2.imread('./original/' + str(i))
    
    a, b = i.split(".")

    with open("./labels/" + str(a) + "." + str(b) + ".txt", "r") as f:
        for line in f.read().split("\n"):
            if len(line) == 0:
                continue
            
            name, part, x, y, w, h, blank = line.split(" ")
            # box1 = x * (image.shape[0]//416)
            # box2 = y * (image.shape[1]//416)
            # box3 = w * (image.shape[0]//416)
            # box4 = h * (image.shape[1]//416)
            # print(box1, box2, box3, box4)
            # print(x,y,w,h)
            # print(image.shape[0]//416, image.shape[1]//416)
            
            if int(part) == 0:
                head_part = img[int(x) * (int(image.shape[0])//416):int(w) * (int(image.shape[0])//416), int(y) * (int(image.shape[1])//416): int(h)* (int(image.shape[1])//416)]
                cv2.imwrite("./head/" + str(i), head_part)
            
            if int(part) == 1:
                body_part = img[int(x) * (int(image.shape[0])//416):int(w) * (int(image.shape[0])//416), int(y) * (int(image.shape[1])//416): int(h)* (int(image.shape[1])//416)]
                cv2.imwrite("./body/" + str(i), body_part)
                
            if int(part) == 2:
                leg_part = img[int(x) * (int(image.shape[0])//416):int(w) * (int(image.shape[0])//416), int(y) * (int(image.shape[1])//416): int(h)* (int(image.shape[1])//416)]
                cv2.imwrite("./leg/" + str(i), leg_part)
            
