# Program to generate graphs based on data outputed from gAperture
import math
import os
from gPhoton.gAperture import gAperture
import matplotlib.pyplot as plt
from astropy import units as u
from astropy.coordinates import SkyCoord
from gPhoton.gphoton_utils import read_lc
from datetime import datetime
import plotly.plotly as py
starttime = datetime.now()
#py.sign_in('tboudreaux', 'Nhv#r&HBlVlb6K9UR#0ihHxX0OK7!2')
### FLAGS ###
ONE = 'Hotspot'
TWO = 'Mask Edge'
FOUR = 'Exptime'
EIGHT = 'Respose'
SIXTEEN = 'Nonlinearity'
THIRTYTWO = 'Detector Edge'
SIXTYFOUR = 'bg Hotspot'
ONETWENTYEIGHT = 'bg Mask'

FLAGARRAY = [ONE, TWO, FOUR, EIGHT, SIXTEEN, THIRTYTWO, SIXTYFOUR, ONETWENTYEIGHT]
NUMERICFLAGARRAY = [0, 1, 2, 3, 4, 5, 6, 7]

marker_style = dict(color='green', linestyle=':', marker='o',
                            markersize=5, markerfacecoloralt='gray')

start = os.path.abspath('.')

filename = 'sdBHundredLs.csv'

readfile = open(filename, 'rb')
readfile = readfile.readlines()
readfile = [x.rsplit() for x in readfile]
urlout = []
urlfile = open('plotlyurls.csv', 'w')
# Target iterator loop
for i in range(len(readfile)):
        numsave = 1
#for i in range(5):
        os.chdir('sdBs/HundredRun/' + readfile[i][0])
	dir = os.listdir('.')
        # Checks for data file
        if 'GENLC_' + readfile[i][0] + '.csv' in dir: #and readfile[i][0] + 'ZONE_1.png' not in dir:
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

            # Greates multiple data sets form single monolithic data set "zoomed" into data so that there is not massive
            #   Time deltas between data making it impossible to read
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
            if gapnum > 0:
                for k in range(len(gAppOutput)):
                    goodflux = []
                    goodtime = []
                    gooderr = []
                    badflux = []
                    badtime = []
                    baderr = []
                    dataflags = []

                    # flag checks
                    for p in range(len(fluxerr[k])):
                        flag_pos = []
                        if flags[k][p] != 0.0:
                            print 'bad flag for target ' + readfile[i][0] + ' | f: ' + str(flags[k][p])
                            flag = int(flags[k][p])
                            flag = bin(flag)[2:]
                            for numeral in range(len(flag)):
                                if flag[numeral] == '1':
                                    flag_pos.append(len(flag)-numeral)
                            badflux.append(fluxfile[k][p])
                            badtime.append(gAppOutput[k][p])
                            baderr.append(fluxerr[k][p])
                            dataflags.append(flag_pos)
                        else:
                            print 'Good flag for target ' + readfile[i][0] + ' | f: ' + str(flags[k][p])
                            goodflux.append(fluxfile[k][p])
                            goodtime.append(gAppOutput[k][p])
                            gooderr.append(fluxerr[k][p])
                    print 'Begining plot creation for target ' + readfile[i][0]
                    plt.figure(1, figsize=(7, 5))
                    fig, axt = plt.subplots()
                    ax1 = plt.subplot(412)
                    checks = plt.subplot(411, sharex=ax1)
                    checks.set_ylim(0, 8)
                    for num in range(8):
                        checks.axhline(y = num, linestyle='--', color='gray')
                    checks.set_ylabel('flag (power 2 scale)')
                    maxx = int(math.ceil(max(gAppOutput[k])))
                    minx = int(math.floor(min(gAppOutput[k])))
                    tiemdelta = maxx - minx
                    slicewidth = int(math.ceil(tiemdelta/len(gAppOutput[k])))
                    prev_datapoint = 'N/A'
                    inc = 0
                    inc_width = 0
                    recording = False
                    for datapoint in flags[k]:
                        if prev_datapoint == datapoint or inc == 0:
                            prev_datapoint = datapoint
                            recording = True
                            inc_width += 1
                        else:
                            if recording is True:
                                recording = False
                                loc = int(math.floor(inc_width/2))
                                inc_width = 0
                                toplotx = []
                                toploty = []
                                for flagstore in dataflags:
                                    for errormessage in flagstore:
                                        toplotx.append(gAppOutput[k][inc-loc])
                                        toploty.append(NUMERICFLAGARRAY[errormessage-1])
                                checks.plot(toplotx, toploty, fillstyle='full', **marker_style)
                                moreploty = []
                                toplotx = []
                                for value in range(8):
                                    if value not in toploty:
                                        moreploty.append(value)
                                        toplotx.append(gAppOutput[k][inc-loc])
                                    else:
                                        pass
                                checks.plot(toplotx, moreploty, fillstyle='none', **marker_style)
                            prev_datapoint = datapoint
                            ax1.axvline(x = gAppOutput[k][inc], linestyle='--', color='black')
                        inc += 1
                    plt.title('Zone # ' + str(k + 1) + ' Estimated integration time: ' + str(len(goodtime)*10 + len(badtime)*10) + '(s)')
                    ax1.errorbar(goodtime, goodflux, yerr=gooderr, fmt='o')
                    ax1.errorbar(badtime, badflux, yerr=baderr,
                                 fmt='ro')  # Work on getting flags running, your close but not there
                    ax1.plot(gAppOutput[k], fluxfile[k], 'ko-')
                    ax1.plot(goodtime, goodflux, 'ko')
                    ax1.plot(badtime, badflux, 'ro')
                    ax1.set_xlabel('Time(s)')
                    ax1.set_ylabel('bgflux')
                    ax2 = plt.subplot(413, sharex = ax1)
                    plt.plot(gAppOutput[k], exptime[k], 'o-')
                    plt.xlabel('Time(s)')
                    plt.ylabel('EXP (s)')
                    ax3 = plt.subplot(414, sharex = ax1)
                    plt.plot(gAppOutput[k], detRAD[k], 'o-')
                    plt.xlabel('Time(s)')
                    plt.ylabel('RAD (units)')
                    print '###########'
                    print 'saving fig for ' + readfile[i][0] + ' this is the #' + str(numsave) + ' time'
                    plt.savefig(readfile[i][0] + 'ZONE_' + str(k + 1) + '.png', dpi=200)
                    numsave += 1
                    plt.close()
                    print 'plot creation complete'
                    axt.set_title('Zone # ' + str(k + 1) + ' Estimated integration time: ' + str(len(goodtime)*10 + len(badtime)*10) + '(s)')
                    axt.errorbar(goodtime, goodflux, yerr=gooderr, fmt='o')
                    axt.errorbar(badtime, badflux, yerr=baderr,
                                 fmt='ro')  # Work on getting flags running, your close but not there
                    axt.plot(gAppOutput[k], fluxfile[k], 'ko-')
                    axt.plot(goodtime, goodflux, 'ko')
                    axt.plot(badtime, badflux, 'ro')
                    url = 'TEST' #py.plot_mpl(fig, filename = readfile[i][0] + '_ZONE_' + str(k+1), auto_open = False)
                    urlout.append(readfile[i][0] + '_ZONE_' + str(k+1) + '\t' + url + '\n')
                    currentdir = os.path.abspath('.')
                    os.chdir(start)
                    try:
                        logfile = open('HTMLOUT.log', 'a')
                    except IOError:
                        logfile = open('HTMLOUT.log', 'w')
                    logfile.write(readfile[i][0] + '\t' + str(k+1) + '\n')
                    logfile.close()
                    os.chdir(currentdir)
            else:

                print 'Outputing single zone plot for target ', readfile[i][0]
                plt.figure(1)
                fig, axt = plt.subplots() 
                ax1 = plt.subplot(311)
                plt.title('Zone # 1 Estimated integration time: ' + str(len(fluxfile)*10) + '(s)')
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
                plt.savefig(readfile[i][0] + 'ZONE_1.png', dpi=250)
                plt.close()
                print 'plot creation complete'
                axt.errorbar(gAppFile['t_mean'], gAppFile['flux_bgsub'], yerr=gAppFile['flux_err'], fmt='o')
                axt.plot(gAppFile['t_mean'], gAppFile['flux_bgsub'], 'ko-')
                axt.set_xlabel('Time(s)')
                axt.set_ylabel('bgflux')
                url = py.plot_mpl(fig, filename = readfile[i][0] + '_ZONE_1', auto_open=False)
                urlout.append(readfile[i][0] + '_ZONE_1' + '\t' + url + '\n')
        #elif 'GENLC_' + readfile[i][0] + '.csv' in dir and readfile[i][0] + 'ZONE_1.png' in dir:
        #    print 'Skipping, graphs alrady exist for target ' + readfile[i][0]
        elif 'GENLC_' + readfile[i][0] + '.csv' not in dir:
            print 'SKIPPING NO CSV DATA FILE FOR TAGRET ' + readfile[i][0]
        print 'Moving to next target'
        os.chdir('../../..')
for i in urlout:
    print 'wrightint:', i
    urlfile.write(i)
urlfile.close()
