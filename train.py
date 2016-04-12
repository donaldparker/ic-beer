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

  pic_num = 532
  for i in neg_images_urls.split('\n'):
    try:
      print(i)
      img_path = "neg/" + str(pic_num) + ".jpg"
      urllib.request.urlretrieve(i, img_path)
      img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
      resize_image = cv2.resize(img, (100,100))
      cv2.imwrite(img_path, resize_image)
      pic_num += 1
    except Exception as e:
      print(str(e ))
      
store_raw_images()
def find_uglies():
  for file_type in ['neg']:
    for img in os.listdir(file_type):
      for ugly in os.listdir('uglies'):
        try:
          curr_img_path = str(file_type) + '/' + str(img)
          ugly_img = cv2.imread('uglies/' + str(ugly))
          question_img = cv2.imread(curr_img_path)
          
          if ugly_img.shape == question_img.shape and not(np.bitwise_xor(ugly_img, question_img).any()):
            print('removing ' + curr_img_path)
            os.remove(curr_img_path)
            
        except Exception as e:
          print(str(e))
# find_uglies()