from six.moves import urllib
import cv2
import numpy as np
import os
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def store_raw_images():
  neg_images_links = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n04285008'
  neg_images_urls = urllib.request.urlopen(neg_images_links).read().decode()
  
  pos_images_links = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02823428'
  if not os.path.exists('neg'):
    os.makedirs('neg')
  print('ready')
  pic_num = 1
  for i in neg_images_urls.split('\n'):
    try:
      print(i)
      # urllib.request
    except Exception as e:
      print(str(e ))
      
store_raw_images()