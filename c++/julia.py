import sys
import numpy as np
import matplotlib.pyplot as plt
from ctypes import *

if len(sys.argv) != 3:
    print ("Wrong arguments")
    print ("usage : %s cx cy" % sys.argv[0])

libmandel = CDLL('libmandel.so')

minx = -1
maxx = 1
nx = 4000
dx = (maxx - minx) / nx
miny = -1
maxy = 1
ny = 4000
dy = (maxy - miny) / ny

buffer = ((c_int * nx) * ny) ()
libmandel.julia(buffer, c_float(minx), c_float(dx), c_uint(nx), c_float(miny), c_float(dy), c_uint(ny), c_float(float(sys.argv[1])), c_float(float(sys.argv[2])))

plt.imshow(buffer, cmap = plt.cm.get_cmap('RdPu'), interpolation = 'none', extent = (minx, maxx, maxy, miny))
plt.xlabel("Re(c)")
plt.ylabel("Im(c)")
plt.savefig("mandelbrot_python.jpg")
plt.show()

# 0.39 0.03
# 0.39 0.1
# 0.39 0.2
# 0.38 0.23
