from __future__ import print_function

from matplotlib import image
from cv2 import resize

import numpy 
import tifffile as tiff 
import os
import numpy as np
import cv2

from skimage.io import imsave, imread

data_path = './data/'

image_rows = 256
image_cols = 256

# Resize Function
def resize_image(img, size=(28,28)):

    h, w = img.shape[:2]
    c = img.shape[2] if len(img.shape)>2 else 1

    if h == w: 
        return cv2.resize(img, size, cv2.INTER_AREA)

    dif = h if h > w else w

    interpolation = cv2.INTER_AREA if dif > (size[0]+size[1])//2 else cv2.INTER_CUBIC

    x_pos = (dif - w)//2
    y_pos = (dif - h)//2

    if len(img.shape) == 2:
        mask = np.zeros((dif, dif), dtype=img.dtype)
        mask[y_pos:y_pos+h, x_pos:x_pos+w] = img[:h, :w]
    else:
        mask = np.zeros((dif, dif, c), dtype=img.dtype)
        mask[y_pos:y_pos+h, x_pos:x_pos+w, :] = img[:h, :w, :]


    return cv2.resize(mask, size, interpolation)

#histogram equalization
def hist_equalization(img):
    hist, bins = np.histogram(img.flatten(), 256, [0,256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * hist.max() / cdf.max()
    cdf_m = np.ma.masked_equal(cdf,0)
    cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
    cdf = np.ma.filled(cdf_m,0).astype('uint8')
    img2 = cdf[img]

    return img2

def create_train_data():
    train_data_path = os.path.join(data_path, 'train')
    images = os.listdir(train_data_path)
    total = len(images)

    imgs = np.ndarray((total, image_rows, image_cols), dtype=np.uint8)
    imgs_mask = np.ndarray((total, image_rows, image_cols), dtype=np.uint8)

    i = 0
    print('-'*30)
    print('Creating training images...')
    print('-'*30)
    for image_name in images:
        if 'mask' in image_name:
            continue
        image_mask_name = image_name.split('.')[0] + '_mask.tiff'
        # Prostate; do pre-process here: 
        img = imread(os.path.join(train_data_path, image_name), as_gray=True) # read prostate
        img = resize_image(img, (256,256)) # resize to 256x256
        img = hist_equalization(img) # histogram equalization
        # Mask; do pre-process here:
        img_mask = imread(os.path.join(train_data_path, image_mask_name), as_gray=True) # read mask and turn to grayscale
        img_mask = resize_image(img_mask, (256, 256)) # resize to 256x256

        img = np.array([img]) 
        img_mask = np.array([img_mask])

        imgs[i] = img
        imgs_mask[i] = img_mask

        if i % 100 == 0:
            print('Done: {0}/{1} images'.format(i, total))
        i += 1
    print('Loading done.')

    np.save('imgs_train.npy', imgs)
    np.save('imgs_mask_train.npy', imgs_mask)
    print('Saving to .npy files done.')

def create_test_data():
    test_data_path = os.path.join(data_path, 'test')
    images = os.listdir(test_data_path)
    total = len(images)

    imgs = np.ndarray((total, image_rows, image_cols), dtype=np.uint8)
    imgs_mask = np.ndarray((total, image_rows, image_cols), dtype=np.uint8)

    i = 0
    print('-'*30)
    print('Creating validation images...')
    print('-'*30)
    for image_name in images:
        if 'mask' in image_name:
            continue
        image_mask_name = image_name.split('.')[0] + '_mask.tiff'
        # Prostate; do pre-process here: 
        img = imread(os.path.join(test_data_path, image_name), as_gray=True) # read prostate
        img = resize_image(img,(256,256)) # resize to 256x256
        img = hist_equalization(img) # histogram equalization
        # Mask; do pre-process here:
        img_mask = imread(os.path.join(test_data_path, image_mask_name), as_gray=True) # read mask and turn to grayscale
        img_mask = resize_image(img_mask,(256,256)) # resize to 256x256

        img = np.array([img])
        img_mask = np.array([img_mask])

        imgs[i] = img
        imgs_mask[i] = img_mask

        if i % 100 == 0:
            print('Done: {0}/{1} images'.format(i, total))
        i += 1
    print('Loading done.')

    np.save('imgs_test.npy', imgs)
    np.save('imgs_mask_test.npy', imgs_mask)
    print('Saving to .npy files done.')



if __name__ == '__main__':
    create_train_data()
    create_test_data()