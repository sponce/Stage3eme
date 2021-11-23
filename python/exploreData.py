import json
import sys

if (len(sys.argv) != 2):
    print ("Wrong number of arguments")
    print ("Syntax:")
    print (sys.argv[0], "<filename>")
    sys.exit(1)

data = json.load(open(sys.argv[1]))

# Try to print the keys of the top level dictionnary
print ("Keys (top level) :", data.keys())

# Get event 0 and print its keys (it's also a dictionnary)
event0 = data['EVENT6002']
print ("Keys (event level) :", event0.keys())

# Get tracks of event 0 and print their keys (yes, again a dictionnary)
tracks = event0["Tracks"]
print ("Keys (track level) :", tracks.keys())

# Get the first long track and ... print its keys (of course it's a dictionnary)
lt = tracks["LongTracks"][0]
print ("Keys (long track) :", lt.keys())

# Get the first hit of the first track, print last 2 positions. This time it's a list
positions = lt["pos"]
print ("First item of first position :", positions[-2])
print ("First item of first position :", positions[-1])
