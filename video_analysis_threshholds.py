import cv2;
import numpy as np;
# import matplotlib.pylot as plt;

cap = cv2.VideoCapture(0)

while True:
  ret, frame = cap.read()
  # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  retval, threshold = cv2.threshold(frame, 12, 255, cv2.THRESH_BINARY)
  grayscaled = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  retval2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)
  gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
  cv2.imshow('frame', frame)
  cv2.imshow('thresh', threshold)
  cv2.imshow('thresh2', threshold2)
  cv2.imshow('gaus', gaus)
  if cv2.waitKey(0) & 0xFF == ord('q'):
    break
cap.release()
cv2.destroyAllWindows()