import os
from gPhoton.gAperture import gaperture as gAperture
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.coordinates import SkyCoord
from gPhoton.gphoton_utils import read_lc
from datetime import datetime
starttime = datetime.now()
filename = 'KP.csv'

readfile = open(filename, 'rb')
readfile = readfile.readlines()
readfile = [x.rsplit() for x in readfile]

cont = False
overwrite = True

# some user input logig
while cont is False:
    # Debug mode runs with teh first 10 targets in the target file in order to check
    # 		things whithout taking too much time
    # not running in debug mode will use the enture target file
    debug_mode = raw_input('would you like to run in debug mode[Y/n]: ')
    if debug_mode == 'y' or debug_mode == 'Y':
        readfile = readfile[:5]
        cont = True
    elif debug_mode == 'n' or debug_mode == 'N':
        cont2 = False
        while cont2 is False:
            # check to make sure user wants to not run in debug mode -- also allows user
            # 		to cancel before file is overwitten in order to backfileup.
            confirm_fullrun = raw_input(
                'Please confirm that you would like to run an actual run | WARNING THIS MAY TAKE MANY MOONS [Y/n]: ')
            if confirm_fullrun == 'n' or confirm_fullrun == 'N':
                print 'Returning to debug check'
                cont = False
                cont2 = True
            elif confirm_fullrun == 'y' or confirm_fullrun == 'Y':
                print 'running a full run'
                cont = True
                cont2 = True
            else:
                print 'Please enter either yes or no'
                cont = False
                cont2 = False
    # secret mode that allows the user to restart the gFind query at a known loaction
    # 		in the target file
    # few sanity checks, only indended for my reasonalble use
    elif debug_mode == 'j' or debug_mode == 'J':
        pickup_location = input('Please enter the location to pick up in the search file: ')
        if pickup_location > 1:
            overwrite = False
            readfile = readfile[pickup_location:]
        else:
            print 'Invalid input -- Ignoring and starting at beging'
    else:
        print 'Please enter either yes or no'
        cont = False
overwriteGAppCSV = False
for i in range(len(readfile)):
    use_parameters = [None] * 5
    os.chdir('PulseTest/KnownPulse/' + readfile[i][0])
    dir = os.listdir('.')
    if 'BAD.txt' in dir:
        print 'Passing on Data Query for target number ' + str(i + 1) + '[' + readfile[i][0] + ']'
        pass
    else:
        try:
            regionfile = open('region_' + readfile[i][0].lower() + '.reg')
        except IOError:
            regionfile = open('region_' + readfile[i][0].upper() + '.reg')
        regionread = regionfile.readlines()
        regionread = [x.rstrip() for x in regionread]
        size_info = regionread[4:7]
        size_info = [x.replace('circle(', '') for x in size_info]
        size_info = [x.replace(') # width=2', '') for x in size_info]
        size_info = [x.replace(') # color=red width=2', '') for x in size_info]
        size_info = [x.split(',') for x in size_info]
        # c = SkyCoord(size_info[0][0] + ' ' + size_info[0][1], unit=(u.hourangle, u.deg))
        # use_parameters[0] = c.ra.degree
        # use_parameters[1] = c.dec.degree
        use_parameters[0] = float(size_info[0][0])
        use_parameters[1] = float(size_info[0][1])
        for j in range(3):
            rad = size_info[j][2]
            rad = rad.replace('"', '')
            rad = float(rad)
            rad *= 0.000277778
            use_parameters[j + 2] = rad
        # for reference use_parameters is a 5 element list, the first element is the
        #	decimal degree RA, the second is the decimal degree dec, the third is
        #	the inner radius to be used in gAperature and the 4th and 5th are
        #	the inner and outer annuli for use in gAperature
        regionfile.close()
        QueryStart = datetime.now()
        print use_parameters
        print 'Begining Data Query for target number ' + str(i + 1) + '[' + readfile[i][0] + '] at time: ' + str(QueryStart)
        if 'GENLC_' + str(readfile[i][0]) + '.csv' in dir and overwriteGAppCSV is False:
            print 'File Already Present, using previous file (if in future you would like to always overide flip overwrite bool in code)'
        else:
            print 'No CSV file present, generating one using gApereture Query, please remain calm, this may take some time'
            print '########################'
            print 'DATA FOR THIS QUERRY'
            print '* RA:', use_parameters[0]
            print '* Dec:', use_parameters[1]
            print '* Radius:', use_parameters[2]
            print '* Annulus small:', use_parameters[3]
            print '* Annulus large:', use_parameters[4]
            print '########################'
            gAperture(band='NUV', skypos=[use_parameters[0], use_parameters[1]], radius = use_parameters[2], annulus = [use_parameters[3], use_parameters[4]], stepsz = 30, csvfile = 'GENLC_' + str(readfile[i][0]) + '.csv', verbose=3)
        curtime = datetime.now()
        print 'Finished Data Query for target number ' + str(i + 1) + '[' + readfile[i][0] + '] at time: ' + str(curtime)
        print 'Total Query time was: ' + str(curtime-QueryStart)
    os.chdir('../../..')
