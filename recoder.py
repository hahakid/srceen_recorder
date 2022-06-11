import cv2
import os
import time
import sys
from PyQt5.QtWidgets import QApplication
import win32gui
import numpy as np
import qimage2ndarray as q2nd
# from pynput import keyboard
from skimage import data, img_as_float
from skimage.metrics import structural_similarity as ssim
from skimage.metrics import peak_signal_noise_ratio as psnr
from skimage.metrics import mean_squared_error

sim_thresh = 0.90
slot = 5

def make_folder():
    local_time = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))
    print("Stored in: ", local_time)
    os.mkdir(local_time)
    return local_time

#make_folder()

def record(path='2022_06_10_18_28_32'):
    hwnd = win32gui.FindWindow(None, 'C:/Windows/system32/cmd.exe')
    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    img = screen.grabWindow(hwnd).toImage()
    img_nd = q2nd.imread(img)
    #print(type(img), type(img_nd))
    #img_nd = np.asarray(img_nd)
    img_nd = cv2.cvtColor(img_nd, cv2.COLOR_BGR2RGB)
    w, h, c = img_nd.shape
    if w > 1000:
        img_nd = cv2.resize(img_nd, (int(h/2), int(w/2)), cv2.INTER_LINEAR)
    #cv2.imshow("", img_nd)
    #cv2.waitKey()
    return img_nd
    #fullpath = os.path.join(path, "screenshot.jpg")
    #img.save(fullpath)
''' # for test
im1 = './2022_06_10_18_28_32/0.jpg'
im2 = './2022_06_10_18_28_32/1.jpg'
im3 = './2022_06_10_18_28_32/2.jpg'

im1 = cv2.imread(im1)
im1 = cv2.cvtColor(im1, cv2.COLOR_RGB2GRAY)
im2 = cv2.imread(im2)
im2 = cv2.cvtColor(im2, cv2.COLOR_RGB2GRAY)
im3 = cv2.imread(im3)
im3 = cv2.cvtColor(im3, cv2.COLOR_RGB2GRAY)
'''
def compare(img1, img2):
    # psnr ...
    # ssim_none = ssim(img1, img2, data_range=img1.max() - img1.min())
    if img1.shape == img2.shape:
        ssim_none = ssim(img1, img2)  # range 0-1
        print("ssim: ", ssim_none)
        # psnr_none = psnr(img1, img2)  # non normalized
        # print("psnr: ", psnr_none)
        if ssim_none >= sim_thresh:  # 0.95:  # threshold control the similarity, the larger the similar
            return 0
        else:
            return 1
    else:
        return 1
# compare(im1, im2)
# compare(im1, im3)

if __name__ == '__main__':

    cur_path = make_folder()  # folder path for storage

    last_gray = np.array([])
    count = 0
    #for i in range(10):
    while 1:
        if last_gray.size == 0:
            last_gray = record()
            last_gray = cv2.cvtColor(last_gray, cv2.COLOR_RGB2GRAY)
        img = record()
        img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        if compare(img_gray, last_gray):  # only when imgs are dif, store
            #cv2.imshow("1", img_gray)
            #cv2.imshow("2", last_gray)
            #cv2.waitKey()
            path = os.path.join(cur_path, str(count)+".jpg")
            cv2.imwrite(path, img)
            last_gray = img_gray
            count += 1
        time.sleep(slot)  # 无论是否变化，间隔采样等待
