import picamera
import time
import config

camera = picamera.PiCamera()


def snap(folder_file):
    camera.resolution = (1024, 768)
    camera.start_preview()
    time.sleep(2)
    camera.capture(folder_file + '.jpg')
    return None


def snap_raw(folder_file):
    camera.resolution = (1024, 768)
    camera.start_preview()
    time.sleep(2)
    camera.capture(folder_file + '.data', 'rgb')
    return None


def take_picture(folder_file):  # dan, modified
    conf = config.get_config()
    fmt = conf.get('Camera', 'FMT')
    with picamera.PiCamera() as cam:
        cam.hflip = conf.getboolean('Camera', 'HFlip')
        cam.vflip = conf.getboolean('Camera', 'VFlip')
        cam.resolution = (conf.getint('Camera', 'Width'), conf.getint('Camera', 'Height'))
        cam.shutter_speed = conf.getint('Camera', 'Shutter_Speed')
        cam.capture(folder_file + "." + fmt, fmt)

# TODO DAN CODE
# import numpy as np
# import Image
# import os
# import sys
# import argparse
# import glob
#
# def data_to_image(fname, width=1280,height=720, out_fmt='tiff'):
#     print height, width
#     fwidth = (width + 31) // 32 * 32
#     fheight = (height + 15) // 16 * 16
#     stream = open(fname, 'rb')
#     stream.seek(0)
#     array = np.fromfile(stream, dtype=np.uint8).reshape((fheight, fwidth, 3))[:height, :width, :]
#     im = Image.fromarray(array)
#     out_fname = out_name(fname, out_fmt)
#     im.save(out_fname)
#
# def out_name(fname, out_fmt):
#     return os.path.splitext(os.path.basename(fname))[0] + '.' + out_fmt
#
#
# parser = argparse.ArgumentParser(description='Convert PiCam RGB data files to regular image formats.',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
# parser.add_argument('directory', metavar='<image directory>', default='.',
#                    help='the directory containg the .data files')
# parser.add_argument('-x','--width', default=720, type=int,
#                    help='the width of the images')
# parser.add_argument('-y','--height', default=1280, type=int,
#                    help='the height of the images')
# parser.add_argument('-f','--out_format', default='tiff',
#                    help='the target image format')
# args = parser.parse_args()
#
# [data_to_image(fname, args.width, args.height, args.out_format) for fname in glob.glob(args.directory + '/*.data')]
