import sys
import numpy as np
import matplotlib.pyplot as plt
from ctypes import *

if len(sys.argv) > 2:
    print ("Too many arguments")
    print ("usage : %s <arch>?" % sys.argv[0])

arch = '' if len(sys.argv) < 2 else sys.argv[1]

libmandel = CDLL('libmandel%s.so' % arch)

minx = -0.586
maxx = -0.574
nx = 2000
dx = (maxx - minx) / nx
miny = -0.648
maxy = -0.656
ny = 2000
dy = (maxy - miny) / ny

buffer = ((c_int * nx) * ny) ()
libmandel.mandel(buffer, c_float(minx), c_float(dx), c_uint(nx), c_float(miny), c_float(dy), c_uint(ny))

plt.imshow(buffer, cmap = plt.cm.get_cmap('RdPu'), interpolation = 'none', extent = (minx, maxx, maxy, miny))
plt.xlabel("Re(c)")
plt.ylabel("Im(c)")
plt.savefig("mandelbrot_python.jpg")
plt.show()
