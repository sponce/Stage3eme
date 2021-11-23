import matplotlib.pyplot as plt

def mandel(cr, ci):
    zr = 0
    zi = 0
    for n in range(1, 100):
        nzr = zr**2 - zi**2 + cr
        nzi = 2*zr*zi + ci
        if nzr**2+nzi**2 > 4:
            return n
        zr = nzr
        zi = nzi
    return -1

minx = 0.3
maxx = 0.4
nx = 400
miny = 0.03
maxy = 0.13
ny = 400

dx = (maxx-minx)/(nx-1)
dy = (maxy-miny)/(ny-1)
img = []
for iy in range(ny):
    line = []
    for ix in range(nx):
        line.append(mandel(minx+ix*dx, miny+iy*dy))
    img.append(line)

plt.imshow(img, cmap = plt.cm.get_cmap('GnBu'), interpolation='none',
       extent = (minx, maxx, miny, maxy))
plt.savefig("mandelbrot_python.svg")
plt.show()
