# Photo to Video Generator
CLI Program that iterates over folders that contain images and joins them in a video, adding text in the left corner and logo image on the bottom right.

## Example usage

*images* folder that contains folders with images:

```
images
|_	image folder 1
		image1.jpg
		image2.jpg
|_	image folder 2
		image1.jpg
		image2.jpg
```

When the program runs, it will join all photos in *image folder 1* while adding text and logo into a video ***image folder 1/image folder 1.mp4***, same for all folders.

Running the script:

```bash
python videobuilder.py --images 'path/to/images/folder' --font 'path/to/font.otf' --logo 'path/to/logo.png'
```

Optional arguments include width and height of the video, and all images will be resized to that size. Default is 1250x800.

## Todo

- test and optimize