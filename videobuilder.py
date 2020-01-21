import os
import cv2
import argparse

from pathlib import Path
from utils import *

parser = argparse.ArgumentParser(description='Join folders of images into videos, adding a logo.\nText is title folder name.\nImages need to be in .jpg format.')
parser.add_argument('--images', help='Images folder - contains folders with images', type=Path, required=True)
parser.add_argument('--font', help='Path to font to be used in text', type=Path, required=True)
parser.add_argument('--logo', help='Path to logo', default='logo.png', type=Path)
parser.add_argument('--imgwidth', help='Width resolution (optional)', type=int, default=1250)
parser.add_argument('--imgheight', help='Height resolution (optional)', type=int, default=800)

args = parser.parse_args()

logo_path = os.path.abspath(args.logo)
font_path = os.path.abspath(args.font)
if os.path.exists(logo_path):
    if not logo_path.endswith('.png'):
        print('Logo needs to be in .png format.')
else:
    print('Logo file does not exist.')
    exit()

if not os.path.exists(font_path):
    print('Font file does not exist.')
    exit()

shape = args.imgwidth, args.imgheight
img_folder = os.path.abspath(args.images)

fps = .65

folders = natural_sort(os.listdir(img_folder))
lgo_img = logo_path

fourcc = cv2.VideoWriter_fourcc(*'mp4v')

for folder in folders:
    name = folder.title()
    folder = os.path.join(img_folder, folder)
    if '.' in folder:
        continue
        
    full_path_folder = os.path.abspath(folder)
    video_path = os.path.join(full_path_folder, name + '.mp4')
    video = cv2.VideoWriter(video_path, fourcc, fps, shape)

    for image in natural_sort(os.listdir(full_path_folder)):
        if image.endswith('.mp4'):
            continue
        image_path = os.path.abspath(os.path.join(full_path_folder, image))
        icopy = image_path.replace('.jpg', '-copied.jpg')

        add_logo(image_path, lgo_img, icopy)
        add_text(icopy, name, icopy, font_path)

        image = cv2.imread(icopy)
        resized = cv2.resize(image, shape) 

        video.write(resized)
        os.remove(icopy)
    video.release()
    print('Folder {0} processed. Video {0}.mp4 created at path: {1}'.format(name, video_path))

