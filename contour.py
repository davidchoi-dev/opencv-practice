# -*- coding: utf-8 -*-
""" This is a practice code to learn the concept of opencv - contour
"""
__author__ = "Wooongje Han"
import cv2
import numpy as np


def draw_contour():
    filename = 'C:/Users/viva/PycharmProjects/opencv-practice/images/globe.png'
    image_origin = cv2.imread(filename)
    image_copy_grey = cv2.cvtColor(image_origin, cv2.COLOR_BGR2GRAY)  # grey scale 로 복사합니다.

    # threshold를 이용하여 binary image로 변환
    ret, image_thresholded = cv2.threshold(image_copy_grey, 127, 255, 0)

    # contours는 point의 list형태. 예제에서는 사각형이 하나의 contours line을 구성하기 때문에 len(contours) = 1. 값은 사각형의 꼭지점 좌표.
    # hierarchy는 contours line의 계층 구조
    image_origin, contours, hierarchy = cv2.findContours(image_thresholded, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    image_origin = cv2.drawContours(image_origin, contours, -1, (0, 250, 0), 1)

    cv2.imshow('image', image_origin)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    draw_contour()
    return None


if __name__ == "__main__":
    main()
