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
import plotly.tools as tls
import plotly.graph_objs as go
from plotly import tools
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

FLAGARRAY = [ONE, TWO, FOUR, EIGHT, SIXTEEN, THIRTYTWO, SIXTYFOUR, ONETWENTYEIGHT, 'NO FLAGS']
NUMERICFLAGARRAY = [0, 1, 2, 3, 4, 5, 6, 7, 8]

marker_style = dict(color='green', linestyle=':', marker='o',
                            markersize=5, markerfacecoloralt='gray')

start = os.path.abspath('.')

filename = 'sdBHundredLs.csv'

readfile = [x.rsplit() for x in open(filename, 'rb').readlines()]
readfile.pop(0)
urlout = []
urlfile = open('plotlyurls.csv', 'w')
# Target iterator loop
for i in range(len(readfile)):
    print readfile[i][0]
    try:
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
                    if gAppFile['t_mean'][k + 1] - gAppFile['t_mean'][k] > 500:
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
                            dataflags.append([0])
                    print 'Begining plot creation for target ' + readfile[i][0]
                    print dataflags
                    useflags = [str(x) for x in dataflags]
                    writeflags = []
                    for q in dataflags:
                        for p in q:
                            writeflags.append(FLAGARRAY[NUMERICFLAGARRAY.index(p) - 1])
                    print writeflags
                    LCTraceGeneralBad = go.Scatter(
                            x = badtime,
                            y = badflux,
                            mode = 'markers',
                            text = writeflags,
                            marker = dict(
                                    color='rgba(255, 182, 193, 0.9)',
                                )
                            )
                    LCTraceGeneralAll = go.Scatter(
                            x = gAppOutput[k],
                            y = fluxfile[k],
                            mode = 'lines+markers'
                            text = writeflags
                            marker = dict(
                                    color = 'rgba(1, 182, 193, 0.9)',
                                )
                            )
                    LCTraceBad = go.Scatter(
                            x = badtime,
                            y = badflux,
                            mode = 'markers',
                            text = writeflags,
                            error_y=dict(
                                    type='data',
                                    array=fluxerr[k],
                                    visible=True,
                                ),
                            marker = dict(
                                color = 'rgba(255, 182, 193, .9)',
                                ),
                            yaxis = 'y2'
                            )
                    LCTraceAll = go.Scatter(
                            x = gAppOutput[k],
                            y = fluxfile[k],
                            mode = 'lines+markers',
                            text = writeflags,
                            error_y=dict(
                                    type='data',
                                    array=fluxerr[k],
                                    visible=True,
                                ),
                            marker = dict(
                                color = 'rgba(1, 182, 193, .9)',
                                ),
                            yaxis = 'y2'
                            )
                    DetRadTrace = go.Scatter(
                            x = gAppOutput[k],
                            y = detRAD[k],
                            mode = 'lines+markers',
                            yaxis = 'y3'
                            )
                    ExpTrace = go.Scatter(
                            x = gAppOutput[k],
                            y = exptime[k],
                            mode = 'lines+markers',
                            yaxis = 'y4'
                            )
                    data = [LCTraceAll, LCTraceGeneralAll, LCTraceGeneralBad, LCTraceBad, ExpTrace, DetRadTrace]
                    layout = go.Layout(
                            yaxis=dict(
                                domain=[0.75, 1],
                                title='Flux NE'
                                ),
                            yaxis2=dict(
                                domain=[0.50, 0.75],
                                title='Flux'
                                ),
                            yaxis3=dict(
                                domain=[0.25, 0.50],
                                title='Det Rad'
                                ),
                            yaxis4 = dict(
                                domain=[0, 0.25],
                                title='EXP Time'
                                ),
                            title = 'Zone: ' + str(k+1) + ' total exposure time: ' + str(len(gAppOutput[k])* 30)
                            )
                    pfig = go.Figure(data=data, layout=layout)
                    maxx = int(math.ceil(max(gAppOutput[k])))
                    minx = int(math.floor(min(gAppOutput[k])))
                    tiemdelta = maxx - minx
                    slicewidth = int(math.ceil(tiemdelta/len(gAppOutput[k])))
                    prev_datapoint = 'N/A'
                    inc = 0
                    inc_width = 0
                    recording = False
                    numsave += 1
                    url = py.plot(pfig, filename = readfile[i][0] + '_ZONE_' + str(k+1), auto_open = False)
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
                #plt.errorbar(gAppFile['t_mean'], gAppFile['flux_bgsub'], yerr=gAppFile['flux_err'], fmt='o')
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
                #axt.errorbar(gAppFile['t_mean'], gAppFile['flux_bgsub'], yerr=gAppFile['flux_err'], fmt='o')
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
    except OSError:
        print 'NO FILE ADVICICINT'
for i in urlout:
    print 'wrightint:', i
    urlfile.write(i)
urlfile.close()
