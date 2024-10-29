'''
문제 출처 : 폴리텍 수업자료 연습문제
'''

# 1) 서로 다른 영상 2개를 읽어 각각 img1과 img2 변수에 저장하고 서로 다른 윈도우에 디스플레이하는 프로그램을 작성하시오
# import cv2 as cv
# import sys

# img1 = cv.imread("./img/lane.jpg")
# img2 = cv.imread("./img/soccer.jpg")

# if img1 is None:
#     sys.exit("파일을 찾을 수 없습니다.")
# if img2 is None:
#     sys.exit("파일을 찾을 수 없습니다.")


# cv.imshow('img1', img1)
# cv.imshow('img2', img2)

# cv.waitKey()
# cv.destroyAllWindows()


# 2) 0.1, 0.3, 0.5, 0.8의 비율로 축소한 영상 4개를 서로 다른 윈도우에 디스플레이하는 프로그램을 작성하시오.
# import cv2 as cv
# import sys

# rate = [0.1, 0.3, 0.5, 0.8]

# img1 = cv.imread('./img/soccer.jpg')
# if img1 is None:
#     sys.exit("파일을 찾을 수 없습니다.")

# for i in range(len(rate)):
#     resize_img = cv.resize(img1, (0,0), fx=rate[i], fy=rate[i])
    
#     cv.imshow(f'resize {rate[i]}', resize_img)

# cv.waitKey(0)
# cv.destroyAllWindows()


# 3) 동영상 재생 중 사용자가 'g'를 입력하면 명암영상(grayscale)을 디스플레이하고,
# 'c'를 입력하면 컬러영상(원본)을 디스플레이하도록 프로그램을 작성하시오.

# import cv2 as cv
# import sys

# video = cv.VideoCapture('img/surfing.mp4')

# if not video.isOpened():
#     print("비디오 파일을 열 수 없습니다.")
#     exit()

# is_gray = False

# while True:
#     ret, frame = video.read()
#     if not ret:
#         print("프레임을 읽어오지 못했습니다.")
#         break

#     if is_gray:
#         gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#         cv.imshow('frame', gray_frame)
#     else:
#         cv.imshow('frame', frame)

#     key = cv.waitKey(30)

#     if key == ord('g'):
#         is_gray = True
#     elif key==ord('c'):
#         is_gray = False
#     elif key==ord('q'):
#         cv.destroyAllWindows()
#         break

# video.release()
# cv.destroyAllWindows()


# 4) 'cv.arrowedLine'를 이용하여 'laugh'글자가 직사각형을 가리키도록 프로그램을 작성(수정)하시오.
# 유인물 프로그램 2-6 참고

import cv2 as cv
import sys

img = cv.imread('./img/girl_laughing.jpg')

if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

cv.rectangle(img,(830,30),(1000,200),(0,0,255),2)
cv.putText(img,'laugh',(700,24),cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
cv.arrowedLine(img, (780,30), (820,50),(0,0,255), 3)

cv.imshow('Draw', img)

while(True):
    if cv.waitKey() == ord('q'):
        cv.destroyAllWindows()
        break


# 5) 왼쪽 버튼을 클릭하면 직사각형, 오른쪽 버튼을 클릭하면 원이 그려지도록 프로그램을 작성하시오.
# cv.circle

# import cv2 as cv
# import sys

# img=cv.imread('img/girl_laughing.jpg')

# if img is None:
#     sys.exit('파일을 찾을 수 없습니다.')

# def draw(event, x, y, flags, param):
#     global ix, iy

#     if event == cv.EVENT_LBUTTONDOWN: # 마우스 왼쪽 버튼 클릭했을 때 초기 위치 저장
#         ix, iy = x,y
#     elif event == cv.EVENT_LBUTTONUP:
#         cv.rectangle(img,(ix,iy),(x,y),(0,0,255),2)

#     elif event == cv.EVENT_RBUTTONDOWN:
#         ix, iy = x,y
#     elif event == cv.EVENT_RBUTTONUP:
#         radius = int(((x-ix)**2+(y-iy)**2)**0.5) # 반지름 계산
#         cv.circle(img,(ix,iy),radius,(255,0,0), 2)

#     cv.imshow('Drawing', img)

# cv.namedWindow('Drawing')
# cv.imshow('Drawing', img)

# cv.setMouseCallback("Drawing", draw)

# while(True):
#     if cv.waitKey(1) == ord('q'):
#         cv.destroyAllWindows()
#         break