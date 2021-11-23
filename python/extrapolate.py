
pos1 = [11.190544128417969, -8.414779663085938, 770.0]
pos2 = [216.72702026367188, -99.75226593017578, 9193.1005859375]

# Compute slope in x and y with respect to z
dx = pos2[0] - pos1[0]
dy = pos2[1] - pos1[1]
dz = pos2[2] - pos1[2]
xslope = dx / dz
yslope = dy / dz

# extrapolate to z = 20000
newZ = 20000
newDz = newZ - pos1[2]
newDx = xslope * newDz
newDy = yslope * newDz
newX = pos1[0] + newDx
newY = pos1[1] + newDy

print(newX, newY, newZ)

# Finally write a function doing all this, and returning a x,y,z tuple for the new point
def extrapolate(pos1, pos2):
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]
    dz = pos2[2] - pos1[2]
    xslope = dx / dz
    yslope = dy / dz

    # extrapolate to z = 20000
    newZ = 20000
    newDz = newZ - pos1[2]
    newDx = xslope * newDz
    newDy = yslope * newDz
    newX = pos1[0] + newDx
    newY = pos1[1] + newDy

    return (newX, newY, newZ)

print(extrapolate(pos1, pos2))
