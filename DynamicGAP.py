import os
from gPhoton.gAperture import gAperture
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.coordinates import SkyCoord
from gPhoton.gphoton_utils import read_lc
from datetime import datetime
starttime = datetime.now()
filename = 'sdBHundredLs.csv'

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
    os.chdir('sdBs/HundredRun/' + readfile[i][0])
    dir = os.listdir('.')
    if 'BAD.txt' in dir:
        print 'Passing on Data Query for target number ' + str(i + 1) + '[' + readfile[i][0] + ']'
        pass
    else:
        regionfile = open('region_' + readfile[i][0] + '.reg')
        regionread = regionfile.readlines()
        regionread = [x.rstrip() for x in regionread]
        size_info = regionread[4:7]
        size_info = [x.replace('circle(', '') for x in size_info]
        size_info = [x.replace(') # width=2', '') for x in size_info]
        size_info = [x.replace(') # color=red width=2', '') for x in size_info]
        size_info = [x.split(',') for x in size_info]
        c = SkyCoord(size_info[0][0] + ' ' + size_info[0][1], unit=(u.hourangle, u.deg))
        use_parameters[0] = c.ra.degree
        use_parameters[1] = c.dec.degree
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
        print 'Begining Data Query for target number ' + str(i + 1) + '[' + readfile[i][0] + '] at time: ' + str(QueryStart)
        if 'GENLC_' + str(readfile[i][0]) + '.csv' in dir and overwriteGAppCSV is False:
            print 'File Already Present, using previous file (if in future you would like to always overide flip overwrite bool in code)'
        else:
            print 'No CSV file present, generating one using gApereture Query, please remain calm, this may take some time'
            gAperture(band='NUV', skypos=[use_parameters[0], use_parameters[1]], radius = use_parameters[2], annulus = [use_parameters[3], use_parameters[4]], stepsz = 10, csvfile = 'GENLC_' + str(readfile[i][0]) + '.csv')
        curtime = datetime.now()
        print 'Finished Data Query for target number ' + str(i + 1) + '[' + readfile[i][0] + '] at time: ' + str(curtime)
        print 'Total Query time was: ' + str(curtime-QueryStart)
        gAppFile = read_lc('GENLC_' + str(readfile[i][0]) + '.csv')
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
                pass
        gAppOutput = [x.tolist() for x in gAppOutput]
        fluxfile = [x.tolist() for x in fluxfile]
        fluxerr = [x.tolist() for x in fluxerr]
        flags = [x.tolist() for x in flags]
        exptime = [x.tolist() for x in exptime]
        detRAD = [x.tolist() for x in detRAD]

        if gapnum > 0:
            for k in range(len(gAppOutput)):
                goodflux = []
                goodtime = []
                gooderr = []
                badflux = []
                badtime = []
                baderr = []
                for p in range(len(fluxerr[k])):
                    if flags[k][p] is not 0:
                        badflux.append(fluxfile[k][p])
                        badtime.append(gAppOutput[k][p])
                        baderr.append(fluxerr[k][p])
                    else:
                        goodflux.append(fluxfile[k][p])
                        goodtime.append(gAppOutput[k][p])
                        gooderr.append(fluxerr[k][p])
                print 'Begining plot creation'
                plt.figure(1)
                ax1 = plt.subplot(311)
                plt.title('Zone # ' + str(k + 1) + ' Estimated integration time: ' + str(len(goodtime)*10 + len(badtime)*10) + '(s)')
                plt.errorbar(goodtime, goodflux, yerr=gooderr, fmt='o')
                plt.errorbar(badtime, badflux, yerr=baderr,
                             fmt='o')  # Work on getting flags running, your close but not there
                plt.plot(goodtime, goodflux, 'ko-')
                plt.plot(badtime, badflux, 'ro-')
                plt.xlabel('Time(s)')
                plt.ylabel('bgflux')
                ax2 = plt.subplot(312, sharex = ax1)
                plt.plot(gAppOutput[k], exptime[k], 'o-')
                plt.xlabel('Time(s)')
                plt.ylabel('EXP (s)')
                ax3 = plt.subplot(313, sharex = ax1)
                plt.plot(gAppOutput[k], detRAD[k], 'o-')
                plt.xlabel('Time(s)')
                plt.ylabel('RAD (units)')
                plt.savefig(readfile[i][0] + 'ZONE_' + str(k + 1) + '.png', dpi=426)
                plt.close()
                print 'plot creation complete'
        else:
            print 'Begining plot creation'
            plt.figure(1)
            ax1 = plt.subplot(311)
            plt.title('Zone # ' + str(k + 1) + 'Estimated integration time: ' + str(len(fluxfile)*10) + '(s)')
            plt.errorbar(gAppFile['t_mean'], gAppFile['flux_bgsub'], yerr=gAppFile['flux_err'], fmt='o')
            plt.plot(gAppFile['t_mean'], gAppFile['flux_bgsub'], 'ko-')
            plt.xlabel('Time(s)')
            plt.ylabel('bgflux')
            ax2 = plt.subplot(312, sharex = ax1)
            plt.plot(gAppFile['t_mean'], gAppFile['exptime'], 'o-')
            plt.xlabel('Time(s)')
            plt.ylabel('EXP (s)')
            ax3 = plt.subplot(313, sharex = ax1)
            plt.plot(gAppFile['t_mean'], gAppFile['detrad'], 'o-')
            plt.xlabel('Time(s)')
            plt.ylabel('RAD (units)')
            plt.savefig(readfile[i][0] + 'ZONE_' + str(k + 1) + '.png', dpi=426)
            plt.close()
            print 'plot creation complete'
        print 'Moving to next target'
    os.chdir('../../..')
