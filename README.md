# ic-beer
brew install opencv3 --with-contrib --with-cuda --with-ffmpeg --with-gphoto2 --with-gstreamer --with-tbb

train
/usr/local/Cellar/opencv3/3.1.0_2/bin/opencv_createsamples -img ./training/beer/positive/racer5.jpg -bg bg.txt -info ./info/info.lst -pngoutput ./info -maxxangle 0.5 -maxyangle -0.5 -maxzangle 0.5 -num 1000