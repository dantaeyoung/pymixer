import sys
import random
from glob import glob
import pydub
import fnmatch
import os
import time

MP3DIR = "./mp3s/"
MP3DIR = "/Users/provolot/Music/iTunes/iTunes Media/Music/"
#/Users/provolot/Documents/github/pymixer
# pydub does things in milliseconds
SLICE_DURATION = 1 * 1000
DESIRED_LENGTH = 20 * 1000
CROSSFADE_LENGTH = 0.5 * 1000
CROSSFADE = False
#CROSSFADE = True
#OUTPUTFILE = "pymixer-mix.mp3"
OUTPUTFILE = time.strftime("%Y%m%d-%H%M%S") + "_pymixer-mix.mp3"


mp3filelist = []
for root, dirnames, filenames in os.walk(MP3DIR):
	print filenames
	for filename in fnmatch.filter(filenames, '*.mp3'):
		mp3filelist.append(os.path.join(root, filename))


randsong = pydub.AudioSegment.empty()

while True:

	print len(randsong), DESIRED_LENGTH
	if(len(randsong)  >= DESIRED_LENGTH):
		break

	SLICE_DURATION = random.randrange(500, 2000)

	print "=========="

	thisfile = random.choice(mp3filelist)

	print "1. song picked:", thisfile, ", loading..."

	thissong = pydub.AudioSegment.from_mp3(thisfile)

	thislen = len(thissong)

	print "2. song loaded; length is", thislen, "(ms)"

	slice_start = random.randrange(0, thislen - (SLICE_DURATION + CROSSFADE_LENGTH))
	print "   random slice", SLICE_DURATION / 1000.0, "secs long: from", slice_start / 1000.0, "s to", (slice_start + SLICE_DURATION) / 1000.0, "s"

	print "3. adding random slice to total"
	if (CROSSFADE):
		if(len(randsong) > CROSSFADE_LENGTH):
			randsong = randsong.append(thissong[slice_start:(slice_start + SLICE_DURATION + CROSSFADE_LENGTH)], CROSSFADE_LENGTH)
		else:
			randsong += thissong[slice_start:(slice_start + SLICE_DURATION)]
	else:
		randsong += thissong[slice_start:(slice_start + SLICE_DURATION)]

	print "   this song is now", len(randsong) / 1000.0, "seconds"

	del thissong

print "saving.."

randsong.export("./" + OUTPUTFILE, format="mp3")
