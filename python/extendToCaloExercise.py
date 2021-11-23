import json
import sys

# copy-paste your extrapolate function here

# reading the input data
data = json.load("Put your file name here")

# loop over events in the file
for eventName in data:
    # first get the longtracks
    longTracks = ...
    # loop over the tracks
    for track in longTracks:
        # extract list of positions for the track
        positions = ...
        # extract positions of 2 last hits
        pos1 = ...
        pos2 = positions[-1]
        # call your extrapolation function
        newPos = ...
        # append new hit to positions
        positions.append(newPos)


# dump result to a new file
json.dump(data, open('Put nam eof new file here', 'w'), indent='  ')
