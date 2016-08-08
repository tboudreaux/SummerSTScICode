# FaRVaE - Fits and Region Viewer also Editor
import sep
import argparse
from astropy.io import fits
from astropy.wcs import WCS
from matplotlib.colors import LogNorm
import matplotlib
matplotlib.use('Qt4Agg')
from pylab import *
import os
import subprocess
import wcsaxes

# from gPhoton.dbasetools import find_nearest_mcat

# Argument parser
parser = argparse.ArgumentParser(description='Takes directory to run viewer on')
parser.add_argument('Cs', metavar='Folder', type=str, nargs=1, help='The Folder to scan threw')
parser.add_argument('-mov', action='store_true', help='look for movies or not')
parser.add_argument('-fc', metavar='RegionFolder', default='//SAME', type=str,
                    nargs=1, help='Tell FaRVaE to look in differnt subdirectories for region file')
parser.add_argument('-si', metavar='StartIndex', type=int, default=[1], nargs=1,
                    help='Tell FaRVaE what index to start on')

args = parser.parse_args()
dest_folder = args.Cs[0]
i = 0
print dest_folder
start = os.path.abspath('.')
os.chdir('Second_sdb/' + dest_folder)
working_dir = os.path.abspath('.')
movies = args.mov
c1 = '#66ff66'
c2 = '#ff0000'
c3 = '#33ccff'
opts = dict(fc='none', ec=c1, lw=2)
opts2 = dict(fc='none', ec=c2, lw=2)
opts3 = dict(fc='none', ec=c2, lw=4)
opts4 = dict(fc='none', ec=c3, lw=2)
axcolor = 'lightgoldenrodyellow'
# list only directories in the current working directory
dirs = [x[0] for x in os.walk(working_dir)]
dirs.pop(0)
dirs = [x.split('/') for x in dirs]
dirs = [x[-1] for x in dirs]
xloc = 0
next_go = False
# Removes hidden directories ('.')
for x in dirs:
    if x[0] == '.':
        dirs.pop(xloc)
    else:
        xloc += 1

prev_message = ''
save_yes = False


##########################
#  Function Definitions  #
##########################

def write_to_clipboard(output):
    """
    Writes string to clipboard on UNIX systems
    :param output: The string that will be written to the clipboard
    :return: out to clipboard
    """
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))


def update_ap(event):
    """
    redraw annulus
    :param event: Slider change event
    :return: N/A
    """
    global Aperture
    global changed
    changed = True
    global ax
    Aperture.remove()
    Aperture = Circle((prev_x, prev_y), ApInc.val, **opts)
    ax.add_patch(Aperture)
    bSave.color = 'red'


def update_in(event):
    """
    redraw the size of the innter annulus radius
    :param event: Slider change event
    :return: N/A
    """
    global InnerAn
    global OuterAn
    global changed
    changed = True
    global ax
    InnerAn.remove()
    # if InAnInc.val >= OutAnInc.val:
    #     OutAnInc.val = InAnInc.val + 1.5
    #     OuterAn.remove()
    #     OuterAn = Circle((center_x, center_y), OutAnInc.val, **opts3)
    #     ax.add_patch(InnerAn)
    InnerAn = Circle((prev_x, prev_y), InAnInc.val, **opts2)
    ax.add_patch(InnerAn)
    bSave.color = 'red'


def update_out(event):
    """
    redraw the size of the outer annulus radius
    :param event: Slider change event
    :return: N/A
    """
    global OuterAn
    global InnerAn
    global changed
    changed = True
    global ax
    OuterAn.remove()
    # if InAnInc.val >= OutAnInc.val:
    #     InAnInc.val = OutAnInc.val - 1.5
    #     InnerAn.remove()
    #     InnerAn = Circle((center_x, center_y), InAnInc.val, **opts2)
    #     ax.add_patch(InnerAn)
    OuterAn = Circle((prev_x, prev_y), OutAnInc.val, **opts3)
    ax.add_patch(OuterAn)
    bSave.color = 'red'


def save_target(event):
    """
    Save out the region data to a region file
    :param event: Button Press Event
    :return: Read Below

    File -- Writes out file
            Name is based on current working directory
            Written out to current working directory
    """
    global prev_message, save_yes, prev_x, prev_y, wcs
    save_yes = True
    outloc = wcs.wcs_pix2world([[prev_x, prev_y]], 1)
    outloc = outloc[0]
    TRD = os.path.abspath('.')
    if args.fc != '//SAME':
        os.chdir(working_dir)
        os.chdir('..')
        os.chdir(args.fc[0])
        regiondirs = os.listdir('.')
        checkfolder = folder[4:].lower()
        os.chdir(regiondirs[regiondirs.index(checkfolder)])
        findregion = os.listdir('.')
        for file in findregion:
            if file[-3:] == 'reg':
                regionfileout = open(file, 'w')
                regionfindflag = True
        else:
            if regionfindflag is False:
                regionfileout = open('region_' + folder[4:].lower() + 'reg', 'w')
            else:
                regionfileout = regionfileout
    else:
        regionfileout = open('region_' + folder + '.reg', 'w')
    # generates region files for use in ds9
    regionfileout.write('# Region file format: DS9 version 4.1\n'
                     '# Target Name: Test\n'
                     'global color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 '
                     'dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1\n'
                     'fk5\n'
                     'circle(' + str(outloc[0]) + ', ' + str(outloc[1]) + ','
                                                                                    ' ' + str(
        ApInc.val) + '") # width=2\n'
                     'circle(' + str(outloc[0]) + ', ' + str(outloc[1]) + ', '
                                                                                    ' ' + str(
        InAnInc.val) + '") # color=red width=2\n'
                       'circle(' + str(outloc[0]) + ', ' + str(outloc[1]) + ', '
                                                                                      ' ' + str(
        OutAnInc.val) + '") # color=red width=2\n')
    regionfileout.close()
    prev_message = 'Saved ' + folder + ' region file'
    plt.close()
    os.chdir(working_dir)


def next_target(event):
    """
    Go to next target and save if changes have been made
    :param event: Button press event
    :return: N/A
    """
    global changed
    global i, dirs, prev_message, save_yes, next_go
    save_yes = False
    numdirs = len(dirs)
    if numdirs - i > 1:
        i += 1
        if changed is True:
            save_target('None')
            changed = False
        else:
            pass
        plt.close()
        next_go = True
        os.chdir(working_dir)
    else:
        pass


def prev_target(event):
    """
    Return to previous target
    :param event: Button Press event
    :return: N/A
    """
    global i, save_yes
    save_yes = False
    if i - 1 >= 0:
        i -= 1
        plt.close()
        os.chdir(working_dir)
    else:
        pass


def close(event):
    exit()


def auto_fit(image_data, xpos, ypos):
    """
    Refit algorithm

    :param

    image_data: fits image data 2D array {Numpy 2D array}

    xpos: centered position of the regions on the x axis {integer}

    ypos: centered position of the region on the y axis {integer}

    ##############################################################

    :return: Dictionary of values
    {
    radii [Ap] -- Aperture radius {float}

    an[0] [InAn] -- Inner annulus radius {float}

    an[1] [OutAn] -- Outer annulus radius {float}

    radii_disagree [disagree] -- The difference between the directly returned radius from SEP and the radius from SEP
                                flux sums {float}
    }
    """
    an_width = 18  # defines annulus width | TODO Make this a free parameter in the auto fit function
    temp_image_data = image_data  # creates non mutable version of array internally
    internal_image_data = temp_image_data.byteswap(True).newbyteorder()  # SEP requires that data be byte swaped
    bkg = sep.Background(internal_image_data)
    thresh = 1.5 * bkg.globalback
    objects = sep.extract(internal_image_data, thresh)
    center_x = internal_image_data.shape[0]/2.0
    center_y = internal_image_data.shape[1]/2.0
    center = [center_x, center_y]
    smallest_dFoc = 1000000000  # big distance so it can only go down
    radii = 21
    radii_sep = 21
    sdev = np.std(internal_image_data)

    count = 0

    # Finds radius of center target from the min and max x and y pixel locations of that target returned from SEP
    for i, j in zip(objects['x'], objects['y']):
        pos = [i, j]

        dFoc = math.sqrt(((pos[0]-center[0])**2) + ((pos[1]-center[1])**2))
        if abs(dFoc) < smallest_dFoc:
            smallest_dFoc = dFoc
            minx = objects['xmin'][count]
            miny = objects['ymin'][count]
            maxx = objects['xmax'][count]
            maxy = objects['ymax'][count]
            radii_sep = abs(math.sqrt(((maxx-minx)**2)+((maxy-miny)**2)))
        else:
            pass
        count += 1
    i = 1

    # Finds optimal inner and outer annulus radii based off SEP flux sums
    while i < 90:
        area = (2*np.pi*((i+an_width)**2))-(2*np.pi*(i**2))
        flux, fluxerr, flag = sep.sum_circann(internal_image_data, prev_x,
                                              prev_y, i, i+an_width)
        metric = ((flux/area) - bkg.globalback)
        if i > 1:
            if metric < smallest_metric:
                smallest_metric = metric
                annulus = [i, i+an_width]
        else:
            smallest_metric = metric
            annulus = [i, i+an_width]
        i += 1

    i = 1

    # Finds radius of center target using SEP flux sums
    while i < 90:
        area = 2*np.pi*(i**2)
        flux, fluxerr, flag = sep.sum_circle(internal_image_data, prev_x,
                                             prev_y, i)
        flux = sum(flux)
        metric = flux/area
        if metric > sdev + bkg.globalback:
            radii = i
        i += 1

    # used more pixels
    an = [math.ceil(x) for x in annulus]

    # sanity checks for size
    if radii > an[0]:
        radii = an[0] - 0.5
    if radii > 30:
        radii = 30
    else:
        pass

    if an[0] > an[1]:
        an[0] = an[1] - 0.1 * an[1]
    radii_disagree = abs(radii-radii_sep)
    return {'Ap': radii, 'InAn': an[0], 'OutAn': an[1], 'disagree': radii_disagree}


def a_fit(event):
    """
    Region file refit compartmentalized function
    :param event: Button Press event
    :return: N/A
    """
    global mutable_image_data, Aperture, InnerAn, OuterAn, changed, prev_x, prev_y
    new_size = auto_fit(mutable_image_data, prev_x, prev_y)
    changed = True
    OuterAn.remove()
    Aperture.remove()
    InnerAn.remove()
    InnerAn = Circle((prev_x, prev_y), new_size['InAn'], **opts2)
    OuterAn = Circle((prev_x, prev_y), new_size['OutAn'], **opts3)
    Aperture = Circle((prev_x, prev_y), new_size['Ap'], **opts)
    ax.add_patch(Aperture)
    ax.add_patch(InnerAn)
    ax.add_patch(OuterAn)
    InAnInc.set_val(new_size['InAn'])
    OutAnInc.set_val(new_size['OutAn'])
    ApInc.set_val(new_size['Ap'])


def mpl_load(event):
    """
    Reloads Python script
    :param event: button press event
    :return: N/A
    """
    os.chdir(start)
    python = sys.executable
    os.execl(python, python, * sys.argv)


def update(event):
    """
    Redraws image to show changes in min max valies
    :param event: event change in slider widgets
    :return: N/A
    """
    global image_data
    im1.set_clim([smin.val, smax.val])
    fig.canvas.draw()


def toggle_play(event):
    """
    toggle play / pause of fits image cubes
    :param event: button press event
    :return: N/A
    """
    global pausecheck
    pausecheck = not pausecheck


def key_control(event):
    """
    Key Control event handeler
    :param event: keyboard press event
    :return: N/A
    """
    keydown = event.key
    global Aperture, InnerAn, OuterAn, changed, prev_x, prev_y, wcs
    MCATFILENAME = 'MCATWD.log'
    if keydown == 'r':
        changed = True
        x_loc = event.xdata
        y_loc = event.ydata
        prev_x = x_loc
        prev_y = y_loc
        InnerAn.remove()
        OuterAn.remove()
        Aperture.remove()
        InnerAn = Circle((prev_x, prev_y), InAnInc.val, **opts2)
        OuterAn = Circle((prev_x, prev_y), OutAnInc.val, **opts3)
        Aperture = Circle((prev_x, prev_y), ApInc.val, **opts)
        ax.add_patch(InnerAn)
        ax.add_patch(OuterAn)
        ax.add_patch(Aperture)
        plt.draw()
    if keydown == 'k':
        plt.savefig(folder + '_RegionWidgetFig.pdf', dpi=200)
    if keydown == 'm':
        tempdir = os.path.abspath('.')
        os.chdir(start)
        MCATREAD = [x.rsplit() for x in open(MCATFILENAME, 'rb').readlines()]
        minim = wcs.wcs_pix2world([[0, 0]], 1)[0]
        maxim = wcs.wcs_pix2world([[image_data.shape[0], image_data.shape[1]]], 1)[0]
        ax.add_patch(Circle((0, 0), 5, **opts4))
        ax.add_patch(Circle((image_data.shape[0], image_data.shape[1]), 5, **opts4))
        plt.draw()
        for MSource in MCATREAD:
            print minim[0], MSource[1], maxim[0], minim[1], MSource[2], maxim[1]
           # if minim[0] >= float(MSource[1]) >= maxim[0] and minim[1] >= float(MSource[2]) >= maxim[1]:
            print 'found qulifier'
            pixcoods = wcs.wcs_world2pix([[float(MSource[1]), float(MSource[2])]], 1)[0]
            ax.add_patch(Circle((pixcoods[0], pixcoods[1]), 40, **opts4))
            plt.draw()
        MCATREAD = None
        skypos = wcs.wcs_pix2world([[prev_x, prev_y]], 1)[0]
        MCATS = find_nearest_mcat('NUV', skypos, 1)
        print MCATS
        os.chdir(tempdir)


i += args.si[0] - 1
while True:
    next_go = False
    folder = dirs[i]
    pausecheck = False
    changed = False
    os.chdir(folder)
    have_movies = False
    # WD Code
    if movies is False:
        filename = ['sdB_' + folder + '_count_coadd.fits', 'sdB_' + folder + '_FUV_count_coadd.fits']
        have_movies = False
        try:
            image_data = fits.getdata(filename[0])
            hdu = fits.open('sdB_' + folder + '_count_coadd.fits')
            wcs = WCS(hdu[0].header)
            mutable_image_data = fits.getdata(filename[0])
        except IOError:
            image_data = fits.getdata(filename[1])
            hdu = fits.open('sdB_' + folder + '_FUV_count_coadd.fits')
            wcs = WCS(hdu[0].header)
            mutable_image_data = fits.getdata(filename[1])
    else:
        filename = [folder + '_movie_count.fits', folder + '_movie_count.fits']
        try:
            image_data = fits.getdata(filename[0])
            hdu = fits.open(folder + '_count_coadd.fits')
            wcs = WCS(hdu[0].header)
            mutable_image_data = fits.getdata(filename[0])
            have_movies = True
        except IOError:
            try:
                image_data = fits.getdata(filename[1])
                hdu = fits.open(folder + '_count_coadd.fits')
                wcs = WCS(hdu[0].header)
                mutable_image_data = fits.getdata(filename[1])
                have_movies = True
            except IOError:
                filename = [folder + '_count_coadd.fits', folder + '_count_coadd.fits']
                have_movies = False
                try:
                    image_data = fits.getdata(filename[0])
                    hdu = fits.open(folder + '_count_coadd.fits')
                    wcs = WCS(hdu[0].header)
                    mutable_image_data = fits.getdata(filename[0])
                except IOError:
                    image_data = fits.getdata(filename[1])
                    hdu = fits.open(folder + '_count_coadd.fits')
                    wcs = WCS(hdu[0].header)
                    mutable_image_data = fits.getdata(filename[1])

    # sdB code
    # image_data = fits.getdata(folder + 'Count.fits')
    # mutable_image_data = fits.getdata(folder + 'Count.fits')
    check = os.path.abspath('.')
    if args.fc == '//SAME':
        regiondirs = os.listdir('.')
        regionfile = open('region_' + folder + '.reg', 'rb')
        regionread = regionfile.readlines()
        regionread = [x.rstrip() for x in regionread]
        size_info = regionread[4:7]
        size_info = [x.replace('circle(', '') for x in size_info]
        size_info = [x.replace(') # width=2', '') for x in size_info]
        size_info = [x.replace(') # color=red width=2', '') for x in size_info]
        size_info = [x.split(',') for x in size_info]
        print regionread
        inc = 0
        region_file = [0] * len(size_info)
        for uvb in size_info:
            region_file[inc] = float(uvb[-1][0:-1])
            inc += 1
        print folder
        loc_info = [float(size_info[0][0]), float(size_info[0][1])]
        wcs_loc = wcs.wcs_world2pix([loc_info], 1)
        wcs_loc = [math.floor(x + 0.5001) for x in wcs_loc[0]]
        regionfile.close()
        try:
            infofile = open(folder.upper() + '_info_full.txt', 'rb')
        except IOError:
            infofile = open(folder.lower() + '_info_full.txt', 'rb')
        infofile = infofile.readlines()
        infofile = infofile[1]
        infofile = infofile.split(',')
        FUV = infofile[5]
        NUV = infofile[6]
        if float(FUV) >= 600 or float(NUV) >= 600:
            print 'Good Target', NUV, FUV
        else:
            print FUV, NUV
            i += 1
            os.chdir(working_dir)
            continue
    else:
        TRD = os.path.abspath('.')
        os.chdir(working_dir)
        os.chdir('..')
        try:
            os.chdir(args.fc[0])
            regiondirs = os.listdir('.')
            try:
                checkfolder = folder[4:].lower()
                os.chdir(regiondirs[regiondirs.index(checkfolder)])
                regionfile = open('region_' + regiondirs[regiondirs.index(checkfolder)] + '.reg', 'rb')
            except IOError:
                checkfolder = folder[4:].upper()
                os.chdir(regiondirs[regiondirs.index(checkfolder)])
                regionfile = open('region_' + regiondirs[regiondirs.index(checkfolder)] + '.reg', 'rb')
            regionread = regionfile.readlines()
            regionread = [x.rstrip() for x in regionread]
            size_info = regionread[4:7]
            size_info = [x.replace('circle(', '') for x in size_info]
            size_info = [x.replace(') # width=2', '') for x in size_info]
            size_info = [x.replace(') # color=red width=2', '') for x in size_info]
            size_info = [x.split(',') for x in size_info]
            inc = 0
            region_file = [0] * len(size_info)
            for uvb in size_info:
                region_file[inc] = float(uvb[-1][0:-1])
                inc += 1
            loc_info = [float(size_info[0][0]), float(size_info[0][1])]
            try:
                wcs_loc = wcs.wcs_world2pix([loc_info], 1)
            except ValueError:
                loc_info.append(0)
                wcs_loc = wcs.wcs_world2pix([loc_info], 1)
            wcs_loc = [math.floor(x + 0.5001) for x in wcs_loc[0]]
            regionfile.close()
            try:
                print regiondirs[regiondirs.index(checkfolder)] + '_info_full.txt'
                checkfolder = folder[4:].lower()
                starname = regiondirs[regiondirs.index(checkfolder)]
                print 'two'
            except IOError:
                print 'here'
                checkfolder = folder[4:].upper()
                starname = regiondirs[regiondirs.index(checkfolder)]
            infofile = open(starname.upper() + '_info_full.txt', 'rb')
            infofile = infofile.readlines()
            infofile = infofile[1]
            infofile = infofile.split(',')
            FUV = infofile[5]
            NUV = infofile[6]
            if float(FUV) >= 600 or float(NUV) >= 600:
                print 'Good Target', NUV, FUV
            else:
                print FUV, NUV
                i += 1
                os.chdir(working_dir)
                continue
            os.chdir(TRD)
        except OSError:
            os.chdir(TRD)
            try:
                regionfile = open('region_' + folder + '.reg', 'rb')
                regionread = regionfile.readlines()
                regionread = [x.rstrip() for x in regionread]
                size_info = regionread[4:7]
                size_info = [x.replace('circle(', '') for x in size_info]
                size_info = [x.replace(') # width=2', '') for x in size_info]
                size_info = [x.replace(') # color=red width=2', '') for x in size_info]
                size_info = [x.split(',') for x in size_info]
                inc = 0
                region_file = [0] * len(size_info)
                for uvb in size_info:
                    region_file[inc] = float(uvb[-1][0:-1])
                    inc += 1
                loc_info = [float(size_info[0][0]), float(size_info[0][1])]
                wcs_loc = wcs.wcs_world2pix([loc_info], 1)
                wcs_loc = [math.floor(x + 0.5001) for x in wcs_loc[0]]
                regionfile.close()
            except IOError:
                print 'UNABLE TO LOCATE REGION FILE EXITING'
                exit()
    check = os.path.abspath('.')
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection=wcs)
    ax.set_aspect('equal')
    if movies is True and have_movies is True:
        ax = fig.add_subplot(111)
        im1 = ax.imshow(image_data[0], norm=LogNorm(), cmap='gray')
        fig.colorbar(im1)
        axApp = axes([0.25, 0.01, 0.65, 0.01], axisbg=axcolor)
        axInAn = axes([0.25, 0.03, 0.65, 0.01], axisbg=axcolor)
        axOutAn = axes([0.25, 0.05, 0.65, 0.01], axisbg=axcolor)
        axSave = axes([0.91, 0.40, 0.075, 0.075], axisbg=axcolor)
        axNext = axes([0.91, 0.10, 0.075, 0.075], axisbg=axcolor)
        axClose = axes([0.91, 0.55, 0.075, 0.075], axisbg=axcolor)
        axPrevious = axes([0.91, 0.25, 0.075, 0.075], axisbg=axcolor)
        axFit = axes([0.91, 0.70, 0.075, 0.075], axisbg=axcolor)
        axReload = axes([0.91, 0.85, 0.075, 0.075], axisbg=axcolor)
        axmin = fig.add_axes([0.4, 0.93, 0.5, 0.01], axisbg=axcolor)
        axmax = fig.add_axes([0.4, 0.95, 0.5, 0.01], axisbg=axcolor)
        aplay = fig.add_axes([0.1, 0.1, 0.05, 0.05], axisbg=axcolor)
        smin = Slider(axmin, 'Min', 0.1, 50, valinit=2)
        smax = Slider(axmax, 'Max', 0.1, 500, valinit=500)
        ApInc = Slider(axApp, 'Aperture radius', 0, region_file[0] * 2, valinit=region_file[0])
        InAnInc = Slider(axInAn, 'Inner Annulus radius', 0, region_file[1] * 2, valinit=region_file[1])
        OutAnInc = Slider(axOutAn, 'Outer Annulus radius', 1.5, region_file[2] * 2, valinit=region_file[2])
        bSave = Button(axSave, 'Save')
        bNext = Button(axNext, 'Next')
        bClose = Button(axClose, 'Close')
        bLast = Button(axPrevious, 'Back')
        bAutoFit = Button(axFit, 'aFit')
        bReload = Button(axReload, 'Reload')
        bTogglePlay = Button(aplay, '||>')
        center_y = image_data.shape[0] / 2.0
        center_x = image_data.shape[1] / 2.0
        prev_x = wcs_loc[0]
        prev_y = wcs_loc[1]
        AppR = ApInc.val
        InR = InAnInc.val
        OutR = OutAnInc.val
        Aperture = Circle((wcs_loc[0], wcs_loc[1]), AppR, **opts)
        ax.add_patch(Aperture)
        InnerAn = Circle((wcs_loc[0], wcs_loc[1]), InR, **opts2)
        ax.add_patch(InnerAn)
        OuterAn = Circle((wcs_loc[0], wcs_loc[1]), OutR, **opts3)
        ax.add_patch(OuterAn)
        plt.figtext(.1, .975, 'previous message: ' + prev_message, style='italic', bbox={'facecolor': 'red',
                                                                                         'alpha': 0.5, 'pad': 5})
        if save_yes is True:
            bSave.color = 'green'

        if movies is False and have_movies is False:
            bTogglePlay.color = 'red'
        elif movies is True and have_movies is False:
            bTogglePlay.color = 'yellow'
        elif movies is True and have_movies is True:
            bTogglePlay.color = 'green'
        else:
            bTogglePlay.color = 'blue'

        smin.on_changed(update)
        smax.on_changed(update)
        bReload.on_clicked(mpl_load)
        bAutoFit.on_clicked(a_fit)
        bLast.on_clicked(prev_target)
        bClose.on_clicked(close)
        bSave.on_clicked(save_target)
        bNext.on_clicked(next_target)
        ApInc.on_changed(update_ap)
        InAnInc.on_changed(update_in)
        OutAnInc.on_changed(update_out)
        bTogglePlay.on_clicked(toggle_play)
        get_current_fig_manager().window.raise_()
        fig.canvas.mpl_connect('key_press_event', key_control)
        frame = 1
        frame_run = True
        while True:
            if frame == len(image_data) - 1:
                frame = 1
            else:
                frame += 1
                if next_go is False:
                    ax = fig.add_subplot(111)
                    ax.set_title(
                        folder + ' | Target Number: ' + str(i + 1) + ' (of ' + str(len(dirs)) + ') | frame ' + str(
                            frame + 1) + '/' + str(len(image_data)))
                    im1 = ax.imshow(image_data[frame], norm=LogNorm(), cmap='gray')
                    if pausecheck is True:
                        while True:
                            if pausecheck is False:
                                break
                            else:
                                plt.pause(0.1)

                    plt.draw()
                    plt.pause(0.001)
                    fig.delaxes(ax)
                else:
                    next_go = False
                    break
    if have_movies is False:
        im1 = ax.imshow(image_data, norm=LogNorm(), cmap='gray')
        fig.colorbar(im1)
        #                [ x,   y,   width, height]
        axApp = axes([0.25, 0.01, 0.65, 0.01], axisbg=axcolor)
        axInAn = axes([0.25, 0.03, 0.65, 0.01], axisbg=axcolor)
        axOutAn = axes([0.25, 0.05, 0.65, 0.01], axisbg=axcolor)
        axSave = axes([0.91, 0.40, 0.075, 0.075], axisbg=axcolor)
        axNext = axes([0.91, 0.10, 0.075, 0.075], axisbg=axcolor)
        axClose = axes([0.91, 0.55, 0.075, 0.075], axisbg=axcolor)
        axPrevious = axes([0.91, 0.25, 0.075, 0.075], axisbg=axcolor)
        axFit = axes([0.91, 0.70, 0.075, 0.075], axisbg=axcolor)
        axReload = axes([0.91, 0.85, 0.075, 0.075], axisbg=axcolor)
        axmin = fig.add_axes([0.4, 0.93, 0.5, 0.01], axisbg=axcolor)
        axmax = fig.add_axes([0.4, 0.95, 0.5, 0.01], axisbg=axcolor)
        aplay = fig.add_axes([0.1, 0.1, 0.05, 0.05], axisbg=axcolor)
        smin = Slider(axmin, 'Min', 0.1, 50, valinit=2)
        smax = Slider(axmax, 'Max', 0.1, 500, valinit=500)
        ApInc = Slider(axApp, 'Aperture radius', 0, region_file[0] * 2, valinit=region_file[0])
        InAnInc = Slider(axInAn, 'Inner Annulus radius', 0, region_file[1] * 2, valinit=region_file[1])
        OutAnInc = Slider(axOutAn, 'Outer Annulus radius', 1.5, region_file[2] * 2, valinit=region_file[2])
        bSave = Button(axSave, 'Save')
        bNext = Button(axNext, 'Next')
        bClose = Button(axClose, 'Close')
        bLast = Button(axPrevious, 'Back')
        bAutoFit = Button(axFit, 'aFit')
        bReload = Button(axReload, 'Reload')
        bTogglePlay = Button(aplay, '||>')
        center_y = image_data.shape[0] / 2.0
        center_x = image_data.shape[1] / 2.0
        prev_x = wcs_loc[0]
        prev_y = wcs_loc[1]
        AppR = ApInc.val
        InR = InAnInc.val
        OutR = OutAnInc.val
        Aperture = Circle((wcs_loc[0], wcs_loc[1]), AppR, **opts)
        ax.add_patch(Aperture)
        InnerAn = Circle((wcs_loc[0], wcs_loc[1]), InR, **opts2)
        ax.add_patch(InnerAn)
        OuterAn = Circle((wcs_loc[0], wcs_loc[1]), OutR, **opts3)
        ax.add_patch(OuterAn)
        ax.set_title(folder + ' | Target Number: ' + str(i+1) + ' (of ' + str(len(dirs)) + ')')
        plt.figtext(.1, .975, 'previous message: ' + prev_message, style='italic', bbox={'facecolor': 'red', 'alpha': 0.5,
                                                                                         'pad': 5})
        write_to_clipboard(folder)

        if save_yes is True:
            bSave.color = 'green'

        if movies is False and have_movies is False:
            bTogglePlay.color = 'red'
        elif movies is True and have_movies is False:
            bTogglePlay.color = 'yellow'
        elif movies is True and have_movies is True:
            bTogglePlay.color = 'green'
        else:
            bTogglePlay.color = 'blue'

        smin.on_changed(update)
        smax.on_changed(update)
        bReload.on_clicked(mpl_load)
        bAutoFit.on_clicked(a_fit)
        bLast.on_clicked(prev_target)
        bClose.on_clicked(close)
        bSave.on_clicked(save_target)
        bNext.on_clicked(next_target)
        ApInc.on_changed(update_ap)
        InAnInc.on_changed(update_in)
        OutAnInc.on_changed(update_out)
        bTogglePlay.on_clicked(toggle_play)
        get_current_fig_manager().window.raise_()
        fig.canvas.mpl_connect('key_press_event', key_control)
        fig.canvas.set_window_title('FaRVaE')
        if pausecheck is True:
            while True:
                if pausecheck is False:
                    break
                else:
                    plt.pause(0.1)
        check = os.path.abspath('.')
        print ''
        plt.show()
        print ''
