import json
import sys

zAtCalo = 20000

if (len(sys.argv) != 2):
    print ("Wrong number of arguments")
    print ("Syntax:")
    print (sys.argv[0], "<filename>")
    sys.exit(1)

def extrapolate(pos1, pos2):
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]
    dz = pos2[2] - pos1[2]
    xslope = dx / dz
    yslope = dy / dz
    newDz = zAtCalo - pos2[2]
    newDx = xslope*newDz
    newDy = yslope*newDz
    return (pos2[0] + newDx, pos2[1] + newDy, zAtCalo)
    
data = json.load(open(sys.argv[1]))
for eventName in data:
    longTracks = data[eventName]["Tracks"]["LongTracks"]
    for track in longTracks:
        positions = track['pos']
        pos1 = positions[-2]
        pos2 = positions[-1]
        newPos = extrapolate(pos1, pos2)
        positions.append(newPos)

def addExt(fileName):
    return fileName.replace('.json', 'Ext.json')

json.dump(data, open(addExt(sys.argv[1]), 'w'), indent=2)
