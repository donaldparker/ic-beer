# ic-beer
Currently nevative images are 100 x 100, positives at 50 x 50 and trained at 20 x 20
### install opencv3 on osx via brew
```
brew install opencv3 --with-contrib --with-cuda --with-ffmpeg --with-gphoto2 --with-gstreamer --with-tbb
```
### build neg match
run the various method to load images from image-net, run ugly to remove bad images
```
/usr/local/Cellar/opencv3/3.1.0_2/bin/opencv_createsamples -img ./training/beer/positive/racer5.jpg -bg bg.txt -info ./info/info.lst -pngoutput ./info -maxxangle 0.5 -maxyangle -0.5 -maxzangle 0.5 -num 1000
```

### output vector
```
/usr/local/Cellar/opencv3/3.1.0_2/bin/opencv_createsamples -info info/info.lst -num 1000 -w 20 -h 20 -vec positives.vec
```