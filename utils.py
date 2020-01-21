import re
from PIL import Image
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys

def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)

def add_text(img, text, img_copy, font_path): 
    img = Image.open(img)
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype("Arial.ttf", 30)
    font = ImageFont.truetype(font_path, 45)

    # x_pos = img.size[0] - 50
    x_pos = 50
    y_pos = img.size[1] - 80

    draw.text((x_pos, y_pos), text, (255, 255, 255), font=font, align='left')
    img.save(img_copy)

def add_logo(mfname, lfname, outfname):
    # outframe = mfname
    mimage = Image.open(mfname)
    limage = Image.open(lfname)

    # resize logo
    wsize = int(min(mimage.size[0], mimage.size[1]) * 0.25)
    wpercent = (wsize / float(limage.size[0]))
    hsize = int((float(limage.size[1]) * float(wpercent)))

    simage = limage.resize((wsize + 20, hsize + 10))
    mbox = mimage.getbbox()
    sbox = simage.getbbox()

    # right bottom corner
    box = (mbox[2] - sbox[2] - 40, mbox[3] - sbox[3] - 40)

    mimage.paste(simage, box, mask=simage)
    mimage.save(outfname)
