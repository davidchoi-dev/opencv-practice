# -*- coding: utf-8 -*-
""" This is a practice code to learn the concept of OpenCV
while performing the tutorial with python.
"""
__author__ = "Wooongje Han"

import cv2  # import openCV-Python pacage
import numpy as np
from matplotlib import pyplot as plt


def erosion_dilation():
    filename = 'images/ad_text2.jpg'
    image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 회색조로 이미지 객체를 생서한다.

    # make kernel matrix for dilation and erosion (Use Numpy)
    kernel_size_row = 3
    kernel_size_col = 3
    kernel = np.ones((kernel_size_row, kernel_size_col), np.uint8)

    erosion_image = cv2.erode(image, kernel, iterations=1)  # make erosion image
    dilation_image = cv2.dilate(image, kernel, iterations=1)  # make dilation image

    # open image window
    cv2.namedWindow('erosion_image',
                    cv2.WINDOW_NORMAL)  # 윈도우 창의 성격 지정 인자 : (윈도우타이틀, 윈도우 사이즈 플래그) , 사용자가 크기 조절할 수 있는 윈도우 생성
    cv2.imshow('erosion_image', erosion_image)  # ADAPTIVE_THRESH_GAUSSIAN_C 적용한 이미지 열기

    # open image window
    cv2.namedWindow('dilation_image',
                    cv2.WINDOW_NORMAL)  # 윈도우 창의 성격z 지정 인자 : (윈도우타이틀, 윈도우 사이즈 플래그) , 사용자가 크기 조절할 수 있는 윈도우 생성
    cv2.imshow('dilation_image', dilation_image)  # ADAPTIVE_THRESH_MEAN_C 적용한 이미지 열기

    # final process
    cv2.waitKey(0)  # 키보드 입력될 때 까지 계속 기다림
    cv2.destroyAllWindows()  # 이미지 윈도우 닫기


def morph_opening_closing():
    filename = 'images/ad_text2.jpg'
    image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 회색조로 이미지 객체를 생서한다.

    # make kernel matrix for dilation and erosion (Use Numpy)
    kernel_size_row = 3
    kernel_size_col = 3
    kernel = np.ones((kernel_size_row, kernel_size_col), np.uint8)

    # opening 적용
    opening_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    # closing 적용
    closing_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

    # open image window
    cv2.namedWindow('opening_image',
                    cv2.WINDOW_NORMAL)  # 윈도우 창의 성격 지정 인자 : (윈도우타이틀, 윈도우 사이즈 플래그) , 사용자가 크기 조절할 수 있는 윈도우 생성
    cv2.imshow('opening_image', opening_image)  # ADAPTIVE_THRESH_GAUSSIAN_C 적용한 이미지 열기

    # open image window
    cv2.namedWindow('closing_image',
                    cv2.WINDOW_NORMAL)  # 윈도우 창의 성격z 지정 인자 : (윈도우타이틀, 윈도우 사이즈 플래그) , 사용자가 크기 조절할 수 있는 윈도우 생성
    cv2.imshow('closing_image', closing_image)  # ADAPTIVE_THRESH_MEAN_C 적용한 이미지 열기

    # final process
    cv2.waitKey(0)  # 키보드 입력될 때 까지 계속 기다림
    cv2.destroyAllWindows()  # 이미지 윈도우 닫기


def main():
    morph_opening_closing()
    return None


if __name__ == "__main__":
    main()