# ic-beer
Currently nevative images are 100 x 100, positives at 50 x 50 and trained at 20 x 20
### install opencv3 on osx via brew
```
brew install opencv3 --with-contrib --with-cuda --with-ffmpeg --with-gphoto2 --with-gstreamer --with-tbb
```
### build neg match
run the various method to load images from image-net, run ugly to remove any manually copied files in the uglies directory
```
python train.py
```
before training
```
mkdir data; makdir info;
```


Start Training
#### 1. positive images
```
/usr/local/Cellar/opencv3/3.1.0_2/bin/opencv_createsamples -img ./training/beer/positive/racer5.jpg -bg bg.txt -info ./info/info.lst -pngoutput ./info -maxxangle 0.5 -maxyangle -0.5 -maxzangle 0.5 -num 1000
```

#### 2. output vector
```
/usr/local/Cellar/opencv3/3.1.0_2/bin/opencv_createsamples -info ./info/info.lst -num 1000 -w 25 -h 25 -vec positives.vec 
```

#### 3. train network
something to note, I was trying 10 stages but since my step 2 crapped out at 1000 (even thought I have 1650 Images)
```
/usr/local/Cellar/opencv3/3.1.0_2/bin/opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 900 -numNeg 450 -numStages 10 -w 25 -h 25
```