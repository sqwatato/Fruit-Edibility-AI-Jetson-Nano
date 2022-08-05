# Fruit Edibility AI Jetson Nano
See if I like a certain fruit or not.

In the project, I've listed the fruits that I despise, the ones I love, and the ones I've never tried. Based on that information, the AI return whether I should eat it or not. Just to be clear, the AI is not very accurate as I have not trained it long enough. In the future I'm planning on training even more and making it return the fruits instead.

# Prerequisites

1. Jetson nano
2. Python installed
3. USB webcam (For live use)
4. Jetson-inference (Download below)


# Setup

## Install CMake

```
sudo apt-get update,
sudo apt-get install git cmake
```

## Install and Clone Jetson Inference

```
git clone --recursive https://github.com/dusty-nv/jetson-inference,
cd jetson-inference,
git submodule update --init
```

## Install Python Libraries

`sudo apt-get install libpython3-dev python3-numpy`

## Run CMake

```
mkdir build,
cd build,
cmake ../
```
Make sure googlenet and resnet-18 is selected(will have a star next to it).
Others models are optional. No need to install Pytorch.

## More Installations

Make sure your still in the build folder

```
sudo make install,
sudo ldconfigRun
```

## Download/Clone this project

Install it manually or with git clone
`git clone https://github.com/sqwatato/Fruit-Edibility-AI-Jetson-Nano.git`


## Run AI

### Image Input

Replace `<resnet_dir>` with the path of the directory of the resnet18.onnx file
Replace `<label_dir>` with the path of the directory of the labels.txt file
Replace `<img_path>` with the path of the input image
Replace `<output_name>` with the name of the output image you would like. Ex "fruit.jpg" (.jpg already in command)

`python3 fruit.py --model=<resnet_dir>/resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=<label_dir>/labels.txt <img_path> <output_name>.jpg`

Make sure to run it in the same directory as the fruit.py file

### Video Input

Replace `<resnet_dir>` with the path of the directory of the resnet18.onnx file
Replace `<label_dir>` with path of the directory of the labels.txt file
Replace `<camera>` with the path of the camera. Mine is "/dev/video0"
Replace `<output_name>` with the name of the output video you would like. Ex "output.mp4" (.mp4 already in command)

`python3 fruit.py --model=<resnet_dir>/resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=<label_dir>/labels.txt <camera> file://<output_name>.mp4`

Make sure to run it in the same directory as the fruit.py file

## Viewing output (Assuming using headless mode)

The terminal should show the percentage of what fruit it thinks it is.
The output image/video will be in the directory that you ran the AI in.
To view on your own computer, use the `scp` command

Replace `<nanousername>` with the username of your Jetson Nano
Replace `<program_dir>` with the path of the directory the image is in
Replace `<img_name>` with the name of the output file. Ex."fruit.jpg" (.jpg already in command)
Replace `<hostusername>` with the name of the hosting computer

### Windows

`scp <nanousername>@192.168.55.1:/home/<nanousername>/<program_dir>/<img_name>.jpg C:\Users\<hostusername>\Desktop`

### Mac

`scp <nanousername>@192.168.55.1:/home/<nanousername>/<program_dir>/<img_name>.jpg ./`

There you go! Now you can change the fruit categories in fruit.py to make it your own! Have fun!

# Video Demo

some link