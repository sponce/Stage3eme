

pos1 = [11.190544128417969, -8.414779663085938, 770.0]
pos2 = [216.72702026367188, -99.75226593017578, 9193.1005859375]

# Compute slope in x and y with respect to z
dx = ...
dy = ...
dz = ...
xslope = dx / dz
yslope = dy / dz

# extrapolate to z = 20000
newZ = 20000
newDz = ...
newDx = ...
newDy = ...
newX = x + newDx
newY = y + newDy

# Finally write a function doing all this, and returning a x,y,z tuple for the new point
