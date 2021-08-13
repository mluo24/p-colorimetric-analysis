import imutils
import numpy as np
import cv2
import math
import os

# get directories
directories_in_str = ["blank", "10mg", "20mg", "40mg", "60mg"]
directories = []
for directory in directories_in_str:
    directories.append(os.fsencode(directory))


def get_images():
    array = []
    for i, directory in enumerate(directories_in_str):
        array.append([])
        for image_path in os.listdir(directory):
            input_path = os.path.join(directory, image_path)
            array[i].append(input_path)
    return array


def display_images(images):
    for index, img in enumerate(images):
        cv2.imshow(directories_in_str[index], img)
        cv2.waitKey(0)


def crop_image(img, x_start, y_start, x_end, y_end):
    return img[y_start:y_end, x_start:x_end]


def fix_image(image):
    rotated = imutils.rotate_bound(image, 90)
    W = 400
    height, width, depth = rotated.shape
    imgScale = W / width
    newX, newY = rotated.shape[1] * imgScale, rotated.shape[0] * imgScale
    newimg = cv2.resize(rotated, (int(newX), int(newY)))
    return newimg


def get_red_val(img):
    avg_color_per_row = np.average(img, axis=0)
    avg_color = np.average(avg_color_per_row, axis=0)
    return int(round(avg_color[2]))