import numpy as np
from astropy.io import fits
import os
from matplotlib.colors import LogNorm
from numpy import pi
import sep
import math
filename = 'sdBHundredLs.csv'

readfile = open(filename, 'rb')
readfile = readfile.readlines()
readfile = [x.rsplit() for x in readfile]
startdir = os.path.abspath('.')
os.chdir('sdBs/HundredRun')
workingdir = os.path.abspath('.')
dirs = os.listdir('.')
xloc = 0
an_width = 3
incriment = 0
name_file = []
for l in readfile:
    name_file.append(l[0])
for x in dirs:
    if x[0] == '.':
        dirs.pop(xloc)
    else:
        xloc += 1
for folder in dirs:
    print 'Startning Target: ' + str(folder)
    os.chdir(folder)
    shiftto = name_file.index(folder)
    image_data = fits.getdata(folder + 'Count.fits')
    image_data = image_data.byteswap(True).newbyteorder()
    bkg = sep.Background(image_data)
    thresh = 1.5 * bkg.globalback
    objects = sep.extract(image_data, thresh)
    center_x = image_data.shape[0]/2.0
    center_y = image_data.shape[1]/2.0
    center = [center_x, center_y]
    smallest_dFoc = 1000000000

    count = 0
    for i, j in zip(objects['x'], objects['y']):
        pos = [i, j]
        dFoc = math.sqrt(((pos[0]-center[0])**2) + ((pos[1]-center[1])**2))
        if abs(dFoc) < smallest_dFoc:
            smallest_dFoc = dFoc
            center_pos = pos
            minx = objects['xmin'][count]
            miny = objects['ymin'][count]
            maxx = objects['xmax'][count]
            maxy = objects['ymax'][count]
            radii = abs(math.sqrt(((maxx-minx)**2)+((maxy-miny)**2)))
        else:
            pass
        count += 1
    i = 0
    while i < 25:
        theta = 0
        area = 0 
        while theta <= 2*pi:
            area += (((i+.1)**2)/2) - ((i**2)/2)
            theta += .001
        flux, fluxerr, flag = sep.sum_circann(image_data, image_data.shape[0]/2, image_data.shape[1]/2, i, i+an_width)
        metric = (flux - bkg.globalback)/bkg.globalrms
        metric /= area
        #print flux, metric
        if i > 1:
            if metric < smallest_metric:
                smallest_metric = metric
                annulus = [i, i+an_width]
        else:
            smallest_metric = metric
            annulus = [i, i+an_width]
        i += 1
    i = 1
    an = [math.ceil(x*6) for x in annulus]
    if radii > an[0]:
        radii = an[0] - 0.5
    else:
        pass
    regionfile = open('region_test_' + folder + '.reg', 'w')
    # generates region files for use in ds9
    regionfile.write('# Region file format: DS9 version 4.1\n'
                     '# Target Name: ' + folder + '\n'
                     'global color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 '
                     'dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1\n'
                     'fk5\n'
                     'circle(' + str(readfile[shiftto][1]) + ', ' + str(readfile[shiftto][2]) + ','
                     ' ' + str(radii) + '") # width=2\n'
                     'circle(' + str(readfile[shiftto][1]) + ', ' + str(readfile[shiftto][2]) + ', '
                     ' ' + str(an[0]) + '") # color=red width=2\n'
                     'circle(' + str(readfile[shiftto][1]) + ', ' + str(readfile[shiftto][2]) + ', '
                     ' ' + str(an[1]) + '") # color=red width=2\n')
    regionfile.close()
    os.chdir(workingdir)
