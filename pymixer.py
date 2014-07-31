import copy
import random
from glob import glob
from pydub import AudioSegment

mp3dir = "./mp3s/"
# pydub does things in milliseconds
slice_duration = 0.5 * 1000;
segment_count = 50


print "loading all songs"
allsongs = []
for mp3_file in glob(mp3dir + "*.mp3"):
	print "loading", mp3_file
	allsongs.append(AudioSegment.from_mp3(mp3_file))

#randsong = None
randsong = AudioSegment.empty()

for i in xrange(segment_count):

	print "#pick a song"
	#pick a song
	thissong = random.choice(allsongs)
	print "we picked", thissong

	print "#get its length (in milliseconds)"
	#get its length (in milliseconds)
	thislen = len(thissong)
	print "len is", thislen

	print "#get slice randomly"
	#get slice randomly
	slice_start = random.randrange(0, thislen - slice_duration)
	print "slice is from", slice_start / 1000.0, "to", (slice_start + slice_duration) / 1000.0, "secs"

	print "#add random slice to total"
	#add random slice to total
	print "adding another song"
	randsong += thissong[slice_start:(slice_start + slice_duration)]

	print "this song is now", len(randsong) / 1000, "seconds"


print "saving"
# save the result
randsong.export("./mixed_sounds.mp3", format="mp3")