import os
import sep
import argparse
from astropy.io import fits
from matplotlib.colors import LogNorm
from matplotlib.widgets import AxesWidget
import matplotlib
matplotlib.use('Qt4Agg')
from pylab import *

parser = argparse.ArgumentParser(description='Takes directory to run viewer on')
parser.add_argument('Cs', metavar='Folder', type=str, nargs=1, help='The Folder to scan threw')
parser.add_argument('-r', action='store_true', help='If true then the code will run recursivly in folders looking for all avalible targets, else the user must provide a path to a spesific target folder')

args = parser.parse_args()
recursive = args.r
dest_folder = args.Cs[0]
good_to_go = True
i = 0
start = os.path.abspath('.')
os.chdir('sdBs/' + dest_folder)
working_dir = os.path.abspath('.')
if recursive is True:
    dirs = [x[0] for x in os.walk(working_dir)]
    dirs.pop(0)
    dirs = [x.split('/') for x in dirs]
    dirs = [x[-1] for x in dirs]
    xloc = 0
    for x in dirs:
        if x[0] == '.':
            dirs.pop(xloc)
        else:
            xloc += 1

    prev_message = ''
    save_yes = False
    while good_to_go is True:

        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111)
        folder = dirs[i]
        changed = False
        os.chdir(folder)
        image_data = fits.getdata(folder + 'Count.fits')
        mutable_image_data = fits.getdata(folder + 'Count.fits')
        regionfile = open('region_' + folder + '.reg', 'rb')
        regionread = regionfile.readlines()
        regionread = [x.rstrip() for x in regionread]
        size_info = regionread[4:7]
        size_info = [x.replace('circle(', '') for x in size_info]
        size_info = [x.replace(') # width=2', '') for x in size_info]
        size_info = [x.replace(') # color=red width=2', '') for x in size_info]
        size_info = [x.split(',') for x in size_info]
        inc = 0
        region_file = [0]*len(size_info)
        for uvb in size_info:
            region_file[inc] = float(uvb[-1][0:-2])
            inc += 1
        regionfile.close()

        ax.set_aspect('equal')
        im1 = ax.imshow(image_data, norm=LogNorm(), cmap='gray')
        fig.colorbar(im1)
        c1 = '#66ff66'
        c2 = '#ff0000'
        opts = dict(fc='none', ec=c1, lw=2)
        opts2 = dict(fc='none', ec=c2, lw=2)
        opts3 = dict(fc='none', ec=c2, lw=4)
        axcolor = 'lightgoldenrodyellow'
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
        axmax  = fig.add_axes([0.4, 0.95, 0.5, 0.01], axisbg=axcolor)
        smin = Slider(axmin, 'Min', 0.1, 50, valinit=2)
        smax = Slider(axmax, 'Max', 0.1, 500, valinit=500)
        ApInc = Slider(axApp, 'Aperture radius', 0, region_file[0] * 6 * 2, valinit=region_file[0])
        InAnInc = Slider(axInAn, 'Inner Annulus radius', 0, region_file[1] * 6 * 2, valinit=region_file[1])
        OutAnInc = Slider(axOutAn, 'Outer Annulus radius', 1.5, region_file[2] * 2 * 2, valinit=region_file[2])
        bSave = Button(axSave, 'Save')
        bNext = Button(axNext, 'Next')
        bClose = Button(axClose, 'Close')
        bLast = Button(axPrevious, 'Back')
        bAutoFit = Button(axFit, 'aFit')
        bReload = Button(axReload, 'Reload')
        center_y = image_data.shape[0] / 2.0
        center_x = image_data.shape[1] / 2.0
        AppR = ApInc.val
        InR = InAnInc.val
        OutR = OutAnInc.val
        Aperture = Circle((center_x, center_y), AppR, **opts)
        ax.add_patch(Aperture)
        InnerAn = Circle((center_x, center_y), InR, **opts2)
        ax.add_patch(InnerAn)
        OuterAn = Circle((center_x, center_y), OutR, **opts3)
        ax.add_patch(OuterAn)
        ax.set_title(folder + ' | Target Number: ' + str(i+1) + ' (of ' + str(len(dirs)) + ')')
        plt.figtext(.1, .975, 'previous message: ' + prev_message, style='italic', bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 5})

        if save_yes is True:
            bSave.color = 'green'

        def updateAp(val):
            global Aperture
            global changed
            changed = True
            global ax
            Aperture.remove()
            Aperture = Circle((center_x, center_y), ApInc.val, **opts)
            ax.add_patch(Aperture)
            bSave.color = 'red'


        def updateIn(val):
            global InnerAn
            global changed
            changed = True
            global ax
            InnerAn.remove()
            InnerAn = Circle((center_x, center_y), InAnInc.val, **opts2)
            ax.add_patch(InnerAn)
            bSave.color = 'red'


        def updateOut(val):
            global OuterAn
            global changed
            changed = True
            global ax
            OuterAn.remove()
            OuterAn = Circle((center_x, center_y), OutAnInc.val, **opts3)
            ax.add_patch(OuterAn)
            bSave.color = 'red'


        def Save(event):
            global prev_message, save_yes
            save_yes = True
            regionfile = open('region_' + folder + '.reg', 'w')
            # generates region files for use in ds9
            regionfile.write('# Region file format: DS9 version 4.1\n'
                             '# Target Name: Test\n'
                             'global color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 '
                             'dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1\n'
                             'fk5\n'
                             'circle(' + str(region_file[0]) + ', ' + str(region_file[1]) + ','
                                                                                            ' ' + str(
                ApInc.val * 6) + '") # width=2\n'
                             'circle(' + str(region_file[0]) + ', ' + str(region_file[0]) + ', '
                                                                                            ' ' + str(
                InAnInc.val * 6) + '") # color=red width=2\n'
                               'circle(' + str(region_file[0]) + ', ' + str(region_file[0]) + ', '
                                                                                              ' ' + str(
                OutAnInc.val * 2) + '") # color=red width=2\n')
            regionfile.close()
            prev_message = 'Saved ' + folder + ' region file'
            plt.close()
            os.chdir(working_dir)


        def Next(event):
            global changed
            global i, dirs, prev_message, save_yes
            save_yes = False
            numdirs = len(dirs)
            if numdirs - i > 1:
                i += 1
                if changed is True:
                    Save('None')
                    changed = False
                else:
                    pass
                plt.close()
                os.chdir(working_dir)
            else:
                pass

        def back(event):
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


        def auto_fit(image_data):
            an_width = 3
            temp_image_data = image_data
            internal_image_data = temp_image_data.byteswap(True).newbyteorder()
            bkg = sep.Background(internal_image_data)
            thresh = 1.5 * bkg.globalback
            objects = sep.extract(internal_image_data, thresh)
            center_x = internal_image_data.shape[0]/2.0
            center_y = internal_image_data.shape[1]/2.0
            center = [center_x, center_y]
            smallest_dFoc = 1000000000
            radii = 21

            count = 0
            for i, j in zip(objects['x'], objects['y']):
                pos = [i, j]

                dFoc = math.sqrt(((pos[0]-center[0])**2) + ((pos[1]-center[1])**2))
                if abs(dFoc) < smallest_dFoc:
                    smallest_dFoc = dFoc
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
                flux, fluxerr, flag = sep.sum_circann(internal_image_data, internal_image_data.shape[0]/2, internal_image_data.shape[1]/2, i, i+an_width)
                metric = ((flux/area) - bkg.globalback)/bkg.globalrms
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
            if radii > 30:
                radii = 30
            else:
                pass
            return {'Ap': radii, 'InAn': an[0], 'OutAn': an[1]}


        def aFit(event):
            global mutable_image_data, Aperture, InnerAn, OuterAn, changed
            new_size = auto_fit(mutable_image_data)
            changed = True
            OuterAn.remove()
            Aperture.remove()
            InnerAn.remove()
            InnerAn = Circle((center_x, center_y), new_size['InAn']*6, **opts2)
            OuterAn = Circle((center_x, center_y), new_size['OutAn']*6, **opts3)
            Aperture = Circle((center_x, center_y), new_size['Ap']*2, **opts)
            ax.add_patch(Aperture)
            ax.add_patch(InnerAn)
            ax.add_patch(OuterAn)
            InAnInc.set_val(new_size['InAn']*6)
            OutAnInc.set_val(new_size['OutAn']*6)
            ApInc.set_val(new_size['Ap']*2)

        def mpl_load(event):
            os.chdir(start)
            python = sys.executable
            os.execl(python, python, * sys.argv)

        def update(val):
            global image_data
            im1.set_clim([smin.val,smax.val])
            fig.canvas.draw()


        smin.on_changed(update)
        smax.on_changed(update)
        bReload.on_clicked(mpl_load)
        bAutoFit.on_clicked(aFit)
        bLast.on_clicked(back)
        bClose.on_clicked(close)
        bSave.on_clicked(Save)
        bNext.on_clicked(Next)
        ApInc.on_changed(updateAp)
        InAnInc.on_changed(updateIn)
        OutAnInc.on_changed(updateOut)
        get_current_fig_manager().window.raise_()
        plt.show()
else:
    while good_to_go is True:
        current_path = os.path.abspath('.')
        current_path = current_path.split('/')
        folder = current_path[-1]
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111)
        changed = False
        image_data = fits.getdata(folder + 'Count.fits')
        mutable_image_data = fits.getdata(folder + 'Count.fits')
        regionfile = open('region_' + folder + '.reg', 'rb')
        regionread = regionfile.readlines()
        regionread = [x.rstrip() for x in regionread]
        size_info = regionread[4:7]
        size_info = [x.replace('circle(', '') for x in size_info]
        size_info = [x.replace(') # width=2', '') for x in size_info]
        size_info = [x.replace(') # color=red width=2', '') for x in size_info]
        size_info = [x.split(',') for x in size_info]
        inc = 0
        region_file = [0]*len(size_info)
        for uvb in size_info:
            region_file[inc] = float(uvb[-1][0:-2])
            inc += 1
        regionfile.close()

        ax.set_aspect('equal')
        im1 = ax.imshow(image_data, norm=LogNorm(), cmap='gray')
        fig.colorbar(im1)
        c1 = '#66ff66'
        c2 = '#ff0000'
        opts = dict(fc='none', ec=c1, lw=2)
        opts2 = dict(fc='none', ec=c2, lw=2)
        opts3 = dict(fc='none', ec=c2, lw=4)
        axcolor = 'lightgoldenrodyellow'
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
        axmax  = fig.add_axes([0.4, 0.95, 0.5, 0.01], axisbg=axcolor)
        smin = Slider(axmin, 'Min', 0.1, 50, valinit=2)
        smax = Slider(axmax, 'Max', 0.1, 500, valinit=500)
        ApInc = Slider(axApp, 'Aperture radius', 0, region_file[0] * 6 * 2, valinit=region_file[0])
        InAnInc = Slider(axInAn, 'Inner Annulus radius', 0, region_file[1] * 6 * 2, valinit=region_file[1])
        OutAnInc = Slider(axOutAn, 'Outer Annulus radius', 1.5, region_file[2] * 2 * 2, valinit=region_file[2])
        bSave = Button(axSave, 'Save')
        bNext = Button(axNext, 'Next')
        bClose = Button(axClose, 'Close')
        bLast = Button(axPrevious, 'Back')
        bAutoFit = Button(axFit, 'aFit')
        bReload = Button(axReload, 'Reload')
        center_y = image_data.shape[0] / 2.0
        center_x = image_data.shape[1] / 2.0
        AppR = ApInc.val
        InR = InAnInc.val
        OutR = OutAnInc.val
        Aperture = Circle((center_x, center_y), AppR, **opts)
        ax.add_patch(Aperture)
        InnerAn = Circle((center_x, center_y), InR, **opts2)
        ax.add_patch(InnerAn)
        OuterAn = Circle((center_x, center_y), OutR, **opts3)
        ax.add_patch(OuterAn)
        ax.set_title(folder + ' | Target Number: ' + str(i+1) + ' (of ' + str(len(dirs)) + ')')
        plt.figtext(.1, .975, 'previous message: ' + prev_message, style='italic', bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 5})
        bNext.color = 'red'
        bLast.color = 'red'
        if save_yes is True:
            bSave.color = 'green'

        def updateAp(val):
            global Aperture
            global changed
            changed = True
            global ax
            Aperture.remove()
            Aperture = Circle((center_x, center_y), ApInc.val, **opts)
            ax.add_patch(Aperture)
            bSave.color = 'red'


        def updateIn(val):
            global InnerAn
            global changed
            changed = True
            global ax
            InnerAn.remove()
            InnerAn = Circle((center_x, center_y), InAnInc.val, **opts2)
            ax.add_patch(InnerAn)
            bSave.color = 'red'


        def updateOut(val):
            global OuterAn
            global changed
            changed = True
            global ax
            OuterAn.remove()
            OuterAn = Circle((center_x, center_y), OutAnInc.val, **opts3)
            ax.add_patch(OuterAn)
            bSave.color = 'red'


        def Save(event):
            global prev_message, save_yes
            save_yes = True
            regionfile = open('region_' + folder + '.reg', 'w')
            # generates region files for use in ds9
            regionfile.write('# Region file format: DS9 version 4.1\n'
                             '# Target Name: Test\n'
                             'global color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 '
                             'dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1\n'
                             'fk5\n'
                             'circle(' + str(region_file[0]) + ', ' + str(region_file[1]) + ','
                                                                                            ' ' + str(
                ApInc.val * 6) + '") # width=2\n'
                             'circle(' + str(region_file[0]) + ', ' + str(region_file[0]) + ', '
                                                                                            ' ' + str(
                InAnInc.val * 6) + '") # color=red width=2\n'
                               'circle(' + str(region_file[0]) + ', ' + str(region_file[0]) + ', '
                                                                                              ' ' + str(
                OutAnInc.val * 2) + '") # color=red width=2\n')
            regionfile.close()
            prev_message = 'Saved ' + folder + ' region file'
            plt.close()


        def Next(event):
            global prev_message
            prev_message = 'No Where to go'

        def back(event):
            global prev_message
            prev_message = 'No Where to go'

        def close(event):
            exit()


        def auto_fit(image_data):
            an_width = 3
            temp_image_data = image_data
            internal_image_data = temp_image_data.byteswap(True).newbyteorder()
            bkg = sep.Background(internal_image_data)
            thresh = 1.5 * bkg.globalback
            objects = sep.extract(internal_image_data, thresh)
            center_x = internal_image_data.shape[0]/2.0
            center_y = internal_image_data.shape[1]/2.0
            center = [center_x, center_y]
            smallest_dFoc = 1000000000
            radii = 21

            count = 0
            for i, j in zip(objects['x'], objects['y']):
                pos = [i, j]

                dFoc = math.sqrt(((pos[0]-center[0])**2) + ((pos[1]-center[1])**2))
                if abs(dFoc) < smallest_dFoc:
                    smallest_dFoc = dFoc
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
                flux, fluxerr, flag = sep.sum_circann(internal_image_data, internal_image_data.shape[0]/2, internal_image_data.shape[1]/2, i, i+an_width)
                metric = (flux - bkg.globalback)/bkg.globalrms
                metric /= area
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
            if radii > 30:
                radii = 30
            else:
                pass
            return {'Ap': radii, 'InAn': an[0], 'OutAn': an[1]}


        def aFit(event):
            global mutable_image_data, Aperture, InnerAn, OuterAn, changed
            new_size = auto_fit(mutable_image_data)
            changed = True
            OuterAn.remove()
            Aperture.remove()
            InnerAn.remove()
            InnerAn = Circle((center_x, center_y), new_size['InAn']*6, **opts2)
            OuterAn = Circle((center_x, center_y), new_size['OutAn']*6, **opts3)
            Aperture = Circle((center_x, center_y), new_size['Ap']*2, **opts)
            ax.add_patch(Aperture)
            ax.add_patch(InnerAn)
            ax.add_patch(OuterAn)
            InAnInc.set_val(new_size['InAn']*6)
            OutAnInc.set_val(new_size['OutAn']*6)
            ApInc.set_val(new_size['Ap']*2)

        def mpl_load(event):
            os.chdir(start)
            python = sys.executable
            os.execl(python, python, * sys.argv)

        def update(val):
            global image_data
            im1.set_clim([smin.val,smax.val])
            fig.canvas.draw()


        smin.on_changed(update)
        smax.on_changed(update)
        bReload.on_clicked(mpl_load)
        bAutoFit.on_clicked(aFit)
        bLast.on_clicked(back)
        bClose.on_clicked(close)
        bSave.on_clicked(Save)
        bNext.on_clicked(Next)
        ApInc.on_changed(updateAp)
        InAnInc.on_changed(updateIn)
        OutAnInc.on_changed(updateOut)
        get_current_fig_manager().window.raise_()
        plt.show()