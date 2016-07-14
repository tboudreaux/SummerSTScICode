import os
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.wcs import WCS
from matplotlib.colors import LogNorm
from pylab import *
import wcsaxes
startloc = os.path.abspath('.')

os.chdir('sdBs/HundredRun')
dirs = os.listdir('.')
xloc = 0
for x in dirs:
    if x[0] == '.':
        dirs.pop(xloc)
    else:
        pass
    xloc += 1
c1 = '#66ff66'
c2 = '#ff0000'

for i in dirs:
    os.chdir(i)
    image_file = i + 'Count.fits'
    hdu_list = fits.open(image_file)
    hdu = fits.open(image_file)[0]
    wcs = WCS(hdu.header)
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection = wcs)
    regionfile = open('region_' + i + '.reg', 'rb')
    regionread = regionfile.readlines()
    regionread = [x.rstrip() for x in regionread]
    size_info = regionread[4:7]
    size_info = [x.replace('circle(', '') for x in size_info]
    size_info = [x.replace(') # width=2', '') for x in size_info]
    size_info = [x.replace(') # color=red width=2', '') for x in size_info]
    size_info = [x.split(',') for x in size_info]
    print 'size info', size_info
    inc = 0
    region_file = [0]*len(size_info)
    for uvb in size_info:
        print uvb[-1][0:-1]
        region_file[inc] = float(uvb[-1][0:-1])
        inc += 1
    loc_info = [float(size_info[0][0]), float(size_info[0][1])]
    opts = dict(fc='none', ec=c1, lw=2)
    opts2 = dict(fc='none', ec=c2, lw=2)
    opts3 = dict(fc='none', ec=c2, lw=4)
    image_data=hdu_list[0].data
    center_y = image_data.shape[0] / 2.0
    center_x = image_data.shape[1] / 2.0
    tmp = ax.imshow(image_data, cmap='gray', norm=LogNorm())
    ax.set_title('gMap Image of ' + i)
    Aperture = Circle((center_x, center_y), region_file[0], **opts)
    ax.add_patch(Aperture)
    InnerAn = Circle((center_x, center_y), region_file[1], **opts2)
    ax.add_patch(InnerAn)
    OuterAn = Circle((center_x, center_y), region_file[2], **opts3)
    ax.add_patch(OuterAn)
    fig.colorbar(tmp)
    plt.savefig(i + 'Count.png', dpi=250)
    plt.close()
    os.chdir('..')
