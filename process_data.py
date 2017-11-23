import numpy as np
import matplotlib.pyplot as plt
import cv2
import argparse
import os
import time
import re

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    return args.path

def collectData(img_path, file_path):
    largeIm = cv2.imread(img_path)
    img = cv2.resize(largeIm, (500, 500))
    if img is not None:
        cv2.imshow("image", img)
        cv2.waitKey(0)
        
        while True:
            try:
                attractiveRating = int(raw_input("Attractive? (type 1) else (type 0)"))
            except ValueError:
                print("Please type either 1 for attractive or 0 for unattractive.")
                continue
            else:
                if attractiveRating != 0 and attractiveRating != 1:
                    print("Please type either 1 for attractive or 0 for unattractive.")
                else:
                    with open(file_path, 'a') as file:
                        file.write(img_path + ',' + str(attractiveRating) + '\n')
                        break


def labelImages(img_folder_path):
    #read in images from all the subfolders
    count = 0
    file_name = "labeled_data_"+ str(time.time()) + ".txt"
    file_path = os.path.join(os.path.join(img_folder_path, "Labeled_Data"), file_name)
    with open(file_path,'a') as file:
        file.write('img_name,attractionRating\n')
    for path,subdirs,files in os.walk(img_folder_path):
        for s in subdirs:
            if re.match(r'\wM',s):
                print s
                img_path = os.path.join(path,s)
                list = os.listdir(os.path.join(path,s))
                if '.DS_Store' in list:
                    list.remove('.DS_Store')
                f = list[0]
                if f.endswith('.jpg'):
                    img_path = os.path.join(img_path,f)
                    count += 1
                    collectData(img_path,file_path)

return file

if __name__ == '__main__':
    img_folder_path = parse_args()
    file = labelImages(img_folder_path)
    cv2.destroyAllWindows()
    file.close()

