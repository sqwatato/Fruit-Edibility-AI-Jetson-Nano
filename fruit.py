#!/usr/bin/env python3
#Code based on https://github.com/Futruo/jetsonai/blob/main/program.py

#Imports
import jetson.inference
import jetson.utils
import argparse
import sys

"""
Start of Lists to change
Replace the list with your own output of fruit sorter
"""
like = ['acai', 'apple', 'banana', 'bell pepper', 'black berry', 'cashew', 'coconut', 'corn kernel', 'dragonfruit', 'goji', 'guava', 'jalapeno', 'jasmine', 'kiwi', 'longan', 'lychee', 'mango', 'nectarine', 'olive', 'papaya', 'pea', 'persimmon', 'pineapple', 'raspberry', 'vanilla', 'watermelon', 'yuzu']
hate = ['apricot', 'avocado', 'black cherry', 'blueberry', 'cherry', 'clementine', 'cocoa bean', 'coffee', 'cranberry', 'date', 'durian', 'eggplant', 'fig', 'grape', 'grapefruit', 'jackfruit', 'kumquat', 'lemon', 'lemon aspen', 'lime', 'macadamia', 'mandarine', 'orange', 'passion fruit', 'peanut', 'pear', 'pomegranate', 'pomelo', 'pumpkin', 'strawberry', 'strawberry guava', 'tomato', 'zucchini']
new = ['abiu', 'acerola', 'ackee', 'alligator apple', 'ambarella', 'araza', 'bael', 'barbadine', 'barberry', 'bayberry', 'beach plum', 'bearberry', 'betel nut', 'bignay', 'bilimbi', 'bitter gourd', 'black currant', 'black mullberry', 'black sapote', 'bolwarra', 'bottle gourd', 'brazil nut', 'bread fruit', "buddha's hand", 'buffaloberry', 'burdekin plum', 'burmese grape', 'caimito', 'camu camu', 'canistel', 'cantaloupe', 'cape gooseberry', 'carambola', 'cardon', 'cedar bay cherry', 'cempedak', 'ceylon gooseberry', 'che', 'chenet', 'cherimoya', 'chico', 'chokeberry', 'cloudberry', 'cluster fig', 'common buckthorn', 'cornelian cherry', 'crab apple', 'crowberry', 'cupuacu', 'custard apple', 'damson', 'desert fig', 'desert lime', 'dewberry', 'elderberry', 'elephant apple', 'emblic', 'entawak', 'etrog', 'feijoa', 'fibrous satinash', 'finger lime', 'galia melon', 'gandaria', 'genipap', 'gooseberry', 'goumi', 'greengage', 'grenadilla', 'guanabana', 'guarana', 'guavaberry', 'hackberry', 'hard kiwi', 'hawthorn', 'hog plum', 'honeyberry', 'honeysuckle', 'horned melon', 'illawarra plum', 'indian almond', 'indian strawberry', 'ita palm', 'jaboticaba', 'jamaica cherry', 'jambul', 'japanese raisin', 'jatoba', 'jocote', 'jostaberry', 'jujube', 'juniper berry', 'kaffir lime', 'kahikatea', 'kakadu plum', 'keppel', 'kundong', 'kutjera', 'lablab', 'langsat', 'lapsi', 'leucaena', 'lillipilli', 'lingonberry', 'loganberry', 'loquat', 'lucuma', 'lulo', 'mabolo', 'malay apple', 'mamey apple', 'mangosteen', 'manila tamarind', 'marang', 'mayhaw', 'maypop', 'medlar', 'melinjo', 'melon pear', 'midyim', 'miracle fruit', 'mock strawberry', 'monkfruit', 'monstera deliciosa', 'morinda', 'mountain papaya', 'mountain soursop', 'mundu', 'muskmelon', 'myrtle', 'nance', 'nannyberry', 'naranjilla', 'native cherry', 'native gooseberry', 'neem', 'nungu', 'nutmeg', 'oil palm', 'old world sycomore', 'oregon grape', 'otaheite apple', 'pawpaw', 'pequi', 'pigeon plum', 'pigface', 'pili nut', 'pineberry', 'pitomba', 'plumcot', 'podocarpus', 'prikly pear', 'pulasan', 'pupunha', 'purple apple berry', 'quandong', 'quince', 'rambutan', 'rangpur', 'red mulberry', 'redcurrant', 'riberry', 'ridged gourd', 'rimu', 'rose hip', 'rose myrtle', 'rose-leaf bramble', 'saguaro', 'salak', 'salal', 'salmonberry', 'sandpaper fig', 'santol', 'sapodilla', 'saskatoon', 'sea buckthorn', 'sea grape', 'snowberry', 'soncoya', 'sugar apple', 'surinam cherry', 'sycamore fig', 'tamarillo', 'tangelo', 'tanjong', 'taxus baccata', 'tayberry', 'texas persimmon', 'thimbleberry', 'toyon', 'ugli fruit', 'velvet tamarind', 'wax gourd', 'white aspen', 'white currant', 'white mulberry', 'white sapote', 'wineberry', 'wongi', 'yali pear', 'yellow plum', 'zigzag vine']



#Parse command line
parser = argparse.ArgumentParser(description="Classify a fruit to determine if it's edible or not.", 
                                 formatter_class=argparse.RawTextHelpFormatter, epilog=jetson.inference.imageNet.Usage() +
                                 jetson.utils.videoSource.Usage() + jetson.utils.videoOutput.Usage() + jetson.utils.logUsage())
parser.add_argument("input_URI", type=str, default="", nargs='?', help="URI of the input stream")
parser.add_argument("output_URI", type=str, default="", nargs='?', help="URI of the output stream")
parser.add_argument("--network", type=str, default="googlenet", help="pre-trained model to load (see below for options)")
parser.add_argument("--camera", type=str, default="0", help="index of the MIPI CSI camera to use (e.g. CSI camera 0)\nor for VL42 cameras, the /dev/video device to use.\nby default, MIPI CSI camera 0 will be used.")
parser.add_argument("--width", type=int, default=1280, help="desired width of camera stream (default is 1280 pixels)")
parser.add_argument("--height", type=int, default=720, help="desired height of camera stream (default is 720 pixels)")
parser.add_argument('--headless', action='store_true', default=(), help="run without display")

is_headless = ["--headless"] if sys.argv[0].find('console.py') != -1 else [""]

try:
	opt = parser.parse_known_args()[0]
except:
	print("")
	parser.print_help()
	sys.exit(0)


# load the recognition network
net = jetson.inference.imageNet(opt.network, sys.argv)

# create video sources & outputs
input = jetson.utils.videoSource(opt.input_URI, argv=sys.argv)
output = jetson.utils.videoOutput(opt.output_URI, argv=sys.argv+is_headless)
font = jetson.utils.cudaFont()

# process frames until the user exits
while True:
	# capture the next image
	img = input.Capture()

	# classify the image
	class_id, confidence = net.Classify(img)

	# find the object description
	class_desc = net.GetClassDesc(class_id)

	text = ""
	if class_desc in like:
		text = "Eat It! You'll love it!"
	elif class_desc in hate:
		text = "Don't Eat It! You won't like it!"
	else:
		text = "Try it! You've never tried it before!"
	# overlay the result on the image	
	font.OverlayText(img, img.width, img.height, "{:05.2f}% {:s}".format(confidence * 100, class_desc), 5, 5, font.White, font.Gray40)
	font.OverlayText(img, img.width, img.height, "{:05.2f}% {:s}".format(confidence * 100, class_desc), 5, 120, font.White, font.Gray40)
	
	# render the image
	output.Render(img)

	# update the title bar
	output.SetStatus("{:s} | Network {:.0f} FPS".format(net.GetNetworkName(), net.GetNetworkFPS()))

	# print out performance info
	net.PrintProfilerTimes()

	# exit on input/output EOS
	if not input.IsStreaming() or not output.IsStreaming():
		break