# -*- coding: utf-8 -*-
""" This is a practice code to learn the concept of OpenCV
while performing the tutorial with python.
"""
__author__ = "Wooongje Han"

import cv2  # import openCV-Python pacage
import numpy as np
from matplotlib import pyplot as plt


def showImage():
    FILENAME = 'images/bus_people.jpg'
    # 이미지 파일을 읽기 위한 객체를 리턴  인자(이미지 파일 경로, 읽기 방식)
    # cv2.IMREAD_COLOR : 투명한 부분 무시되는 컬러
    # cv2.IMREAD_GRAYSCALE : 흑백 이미지로 로드
    # cv2.IMREAD_UNCHANGED : 알파 채컬을 포함한 이미지 그대로 로드
    image = cv2.imread(FILENAME, cv2.IMREAD_GRAYSCALE)
    cv2.namedWindow('model', cv2.WINDOW_NORMAL)  #윈도우 창의 성격 지정 인자 : (윈도우타이틀, 윈도우 사이즈 플래그) , 사용자가 크기 조절할 수 있는 윈도우 생성
    cv2.imshow('model', image)  # 화면에 이미지 띄우기 인자;(윈도우타이틀, 이미지객체)
    cv2.waitKey(5000)  # 지정된 시간 동안 키보드 입력 대기 (ms) , 0이면 key 입력할 때 까지 계속 대기, 입력받은 key 값을 int 로 반환 (아스키코드)
    # 대기시간이 끝나면 아래 코드로 진행
    cv2.destroyAllWindows()  # 생성한 윈도우 제거

def thresholding() :
    FILENAME = 'images/ad_text2.jpg'
    image = cv2.imread(FILENAME, cv2.IMREAD_GRAYSCALE)  # 회색조로 이미지 객체를 생서한다.
    ret, binary_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)  # param : (img, threshold_value, value, flag)
    cv2.imshow('binary image', binary_image)  # 이미지 윈도우 열기
    cv2.imshow('origin image', image)  # 이미지 윈도우 열기
    cv2.waitKey(0)  # 키보드 입력될 때 까지 계속 기다림
    cv2.destroyAllWindows()  # 이미지 윈도우 닫기

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


def otsu_binarization():
    FILENAME = 'images/ad_text2.jpg'
    image = cv2.imread(FILENAME, cv2.IMREAD_GRAYSCALE)  # 회색조로 이미지 객체를 생서한다.
    blur = cv2.GaussianBlur(image, (5, 5), 0)  # Gaussian blur 를 통해 noise 를 제거한 후
    ret3, th3 = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  # global threshold with otsu's binarization

    cv2.namedWindow("global threshold with otsu's binarization", cv2.WINDOW_NORMAL)  # 윈도우 창의 성격 지정 인자 : (윈도우타이틀, 윈도우 사이즈 플래그) , 사용자가 크기 조절할 수 있는 윈도우 생성
    cv2.imshow("global threshold with otsu's binarization", th3)  # ADAPTIVE_THRESH_MEAN_C 적용한 이미지 열기
    cv2.waitKey(0)  # 키보드 입력될 때 까지 계속 기다림
    cv2.destroyAllWindows()  # 이미지 윈도우 닫기


def main():
    thresholding_adaptive()
    return None


if __name__ == "__main__":
    main()