# Fruit Edibility AI Jetson Nano
See if I like a certain fruit or not.

In the project, I've listed the fruits that I despise, the ones I love, and the ones I've never tried. Based on that information, the AI return whether I should eat it or not. Just to be clear, the AI is not very accurate as I have not trained it long enough. In the future I'm planning on training even more and making it return the fruits instead.

# Prerequisites

1. Jetson nano
2. Python installed
3. USB webcam
4. Jetson-inference (Download below)


# Setup

## Install CMake (For AI models)

```sudo apt-get update,
sudo apt-get install git cmake```

## Install and Clone Jetson Inference

```git clone --recursive https://github.com/dusty-nv/jetson-inference,
cd jetson-inference,
git submodule update --init```


sudo apt-get install libpython3-dev python3-numpy

mkdir build,
cd build,
cmake ../

sudo make install,
sudo ldconfigRun

Download and run "program.py" using
python3 program.py

# Video Demo
https://youtu.be/X12Wrr88GGM