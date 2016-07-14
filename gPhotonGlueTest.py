import argparse
from gPhoton.gFind import gFind
from gPhoton.gMap import gMap
from gPhoton.gAperture import gAperture
from gPhoton.gphoton_utils import read_lc
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
from glue import qglue
from astropy.io import fits
import os

parser = argparse.ArgumentParser(description='Take RA and Dec and other parameters relating to generaing glue data.')
parser.add_argument('Cs', metavar='RA/Dec', type=float, nargs=2, help='The Right Acension and Declioation of target')
parser.add_argument('-FUV', action='store_true', help='Use the Far UV band, default is the Near UV')
parser.add_argument('-ran', metavar='range', type=float, nargs=2, help='The height and width of the image returned by gMap in decimal degrees')
parser.add_argument('-name', metavar='target name', type=str, nargs=1, help='enter the target name here')
parser.add_argument('-reg', metavar='Region', type=float, nargs=3, help='enter the Aperture and then the smaller and larger annulus')
parser.add_argument('-o', action='store_true', help='Use exiting data file?')
args = parser.parse_args()
# scripts that will be called by the program when loading glue stuff


def g_find_check(ra, dec, b='NUV'):
    gdata = gFind(band=b, skypos=[ra, dec], maxgap=100., minexp=100.)
    if len(gdata) > 0:
        return '//GD'
    else:
        return '//ND'


def g_map_make(ra, dec, name, skrngh=0.1, skrngw=0.1, b='NUV'):
    gData = gMap(band=b, skypos=[ra, dec], skyrange=[skrngh, skrngw], cntfile=name+'Count.fits', coadd=True, overwrite=True, verbose=3)
    return gData


def g_app_make(ra, dec, name, b='NUV', ap=21, in_an=22.5, out_an=38):
    start_time = datetime.now()
    print 'Beginning Data Query for target: ' + name
    ap *= 0.000277778
    in_an *= 0.000277778
    out_an *= 0.000277778
    gData = gAperture(band=b, skypos=[ra, dec], radius=ap, annulus=[in_an, out_an], stepsz=10, csvfile='GENLC_' + name + '.csv', verbose=3)
    end_time = datetime.now()
    runtime = end_time-start_time
    print 'Finished Data Query for target: ' + name
    return gData

if args.name:
    TargName = args.name[0]
else:
    TargName = str(args.Cs[0]) + str(args.Cs[1])

if args.FUV is True:
    UseBand = 'FUV'
else:
    UseBand = 'NUV'


find_return = g_find_check(args.Cs[0], args.Cs[1], b=UseBand)


if find_return == '//GD':
    if args.ran:
        print 'Begining gMap Output'
        if args.o is True and TargName + 'Count.fits' in os.listdir('.'):
            pass
        else:
            CountMap = g_map_make(args.Cs[0], args.Cs[1], TargName, skrngh=args.ran[0], skrngw=args.ran[1], b=UseBand)
        print 'gMap Output Complete'
    else:
        print 'Begining gMap Output'
        if args.o is True and TargName + 'Count.fits' in os.listdir('.'):
            pass
        else:
            CountMap = g_map_make(args.Cs[0], args[1], TargName, b=UseBand)
        print 'gMap Output Complete'

    if args.reg:
        print 'Beginign gAperture Output'
        if args.o is True:
            try:
                LC = read_lc('GENLC_' + TargName + '.csv')
            except IOError:
                LC = g_app_make(args.Cs[0], args.Cs[1], TargName, b=UseBand, ap=args.reg[0], in_an=args.reg[1], out_an=args.reg[2])
        else:
            LC = g_app_make(args.Cs[0], args.Cs[1], TargName, b=UseBand, ap=args.reg[0], in_an=args.reg[1], out_an=args.reg[2])
        print 'finished gAperture Output'
    else:
        print 'Begining gAperture Output'
        if args.o is True:
            try:
                LC = read_lc('GENLC_' + TargName + '.csv')
            except IOError:
                LC = g_app_make(args.Cs[0], args.Cs[1], TargName, b=UseBand, ap=args.reg[0], in_an=args.reg[1], out_an=args.reg[2])
        else:
            LC = g_app_make(args.Cs[0], args.Cs[1], TargName, b=UseBand)
        print 'Finished gAperture Output'
    print 'One'
    gAppFile = LC
    gAppOutput = []
    fluxfile = []
    fluxerr = []
    flags = []
    exptime = []
    detRAD = []
    gapnum = 0
    prevloc = 0
    greatestdiffernce = 0
    for k in range(len(gAppFile['t_mean'])):
        if k + 1 < len(gAppFile['t_mean']):
            if gAppFile['t_mean'][k + 1] - gAppFile['t_mean'][k] > 1800:
                differnce = gAppFile['t_mean'][k + 1] - gAppFile['t_mean'][k]
                if differnce > greatestdiffernce:
                    greatestdiffernce = differnce
                else:
                    pass
                gAppOutput.append(gAppFile['t_mean'][prevloc:k + 1])
                fluxfile.append(gAppFile['flux_bgsub'][prevloc:k + 1])
                fluxerr.append(gAppFile['flux_err'][prevloc:k + 1])
                flags.append(gAppFile['flags'][prevloc:k + 1])
                exptime.append(gAppFile['exptime'][prevloc:k + 1])
                detRAD.append(gAppFile['detrad'][prevloc:k + 1])
                prevloc = k + 1
                gapnum += 1
            else:
                pass
        else:
            gAppOutput.append(gAppFile['t_mean'][prevloc:-1])
            fluxfile.append(gAppFile['flux_bgsub'][prevloc:-1])
            fluxerr.append(gAppFile['flux_err'][prevloc:-1])
            flags.append(gAppFile['flags'][prevloc:-1])
            exptime.append(gAppFile['exptime'][prevloc:-1])
            detRAD.append(gAppFile['detrad'][prevloc:-1])

    gAppOutput = [x.tolist() for x in gAppOutput]
    fluxfile = [x.tolist() for x in fluxfile]
    fluxerr = [x.tolist() for x in fluxerr]
    flags = [x.tolist() for x in flags]
    exptime = [x.tolist() for x in exptime]
    detRAD = [x.tolist() for x in detRAD]
    LC_data = []
    gaplen = len(gAppOutput)
    print gAppOutput
    for i in range(len(gAppOutput)):
        LC_data.append({'time': gAppOutput[i], 'flux': fluxfile[i]})
    glue_call = 'qglue(ZONE1='
    print 'six'
    print 'gapnum is:', gapnum
    lenLC = len(LC_data)
    print 'hold'
    for i in range(gapnum+1):
        if gapnum-i >= 1:
            glue_call += 'LC_data[' + str(i) + '], ZONE' + str(i+2) + '='
        else:
            glue_call += 'LC_data[' + str(i) + '], IMG='
    glue_call += 'image_data)'
    print glue_call
    print len(LC_data)
    image_data = fits.getdata(TargName + 'Count.fits')
    eval(glue_call)
else:
    print 'NO DATA FOR GIVEN RA AND DEC'
    exit()
