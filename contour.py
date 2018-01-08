# -*- coding: utf-8 -*-
""" This is a practice code to learn the concept of opencv - contour
"""
__author__ = "Wooongje Han"
import cv2
import numpy as np

def thresholding_adaptive():
    FILENAME = 'images/ad_text2.jpg'
    image = cv2.imread(FILENAME, cv2.IMREAD_GRAYSCALE)  # 회색조로 이미지 객체를 생서한다.

    block_size = 15  # 픽셀에 적용할 threshold값을 계산하기 위한 블럭 크기. 적용될 픽셀이 블럭의 중심이 됨. 따라서 blocksize 는 홀수여야 함
    subtract_val = 2  #  보정 상수

    adaptive_gaussian_image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, \
                                              block_size, subtract_val)

    adaptive_mean_image = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, \
                                              block_size, subtract_val)

    cv2.namedWindow('adaptive threshold gaussian', cv2.WINDOW_NORMAL)  # 윈도우 창의 성격 지정 인자 : (윈도우타이틀, 윈도우 사이즈 플래그) , 사용자가 크기 조절할 수 있는 윈도우 생성
    cv2.imshow('adaptive threshold gaussian', adaptive_gaussian_image)  # ADAPTIVE_THRESH_GAUSSIAN_C 적용한 이미지 열기
    cv2.namedWindow('adaptive threshold mean', cv2.WINDOW_NORMAL)  # 윈도우 창의 성격 지정 인자 : (윈도우타이틀, 윈도우 사이즈 플래그) , 사용자가 크기 조절할 수 있는 윈도우 생성
    cv2.imshow('adaptive threshold mean', adaptive_mean_image)  # ADAPTIVE_THRESH_MEAN_C 적용한 이미지 열기
    cv2.waitKey(0)  # 키보드 입력될 때 까지 계속 기다림
    cv2.destroyAllWindows()  # 이미지 윈도우 닫기


def draw_contour():
    filename = 'C:/Users/viva/PycharmProjects/opencv-practice/images/test3.jpg'
    image_origin = cv2.imread(filename)
    image_copy_grey = cv2.cvtColor(image_origin, cv2.COLOR_BGR2GRAY)  # grey scale 로 복사합니다.

    # threshold를 이용하여 binary image로 변환
    ret, image_thresholded = cv2.threshold(image_copy_grey, 127, 255, 0)  # Gray Scale 한 이미지에 Threshold 적용하기

    # contours는 point의 list형태.
    # hierarchy는 contours line의 계층 구조
    # Threshold 적용한 이미지에서 contour 들을 찾아서 contours 변수에 저장하기
    _, contours, _ = cv2.findContours(image_thresholded, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    # 찾은 contours 를 원본 이미지에 그리기
    image_origin = cv2.drawContours(image_origin, contours, -1, (0, 255, 0), 2)

    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image', image_origin)  # contour 그린 원본 이미지를 열기
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    draw_contour()
    return None


if __name__ == "__main__":
    main()
