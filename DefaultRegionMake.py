from gPhoton.gMap import gMap
from gPhoton.gAperture import gAperture
from gPhoton.gFind import gFind
import matplotlib.pyplot as plt
from gPhoton.gphoton_utils import read_lc
import numpy as np
import os
from datetime import datetime
starttime = datetime.now()
filename = 'AllTargets.csv'

readfile = open(filename, 'rb')
readfile = readfile.readlines()
readfile = [x.rsplit() for x in readfile]

os.chdir('sdBs/AllRun')
workingdir = os.path.abspath('.')
num = 0
for i in range(len(readfile)):
    num += 1
    try:
        os.chdir(readfile[i][0])
    except OSError:
        print 'Making folder for target: ' + readfile[i][0]
        os.mkdir(readfile[i][0])
        os.chdir(readfile[i][0])
    print 'Writing out region file for current target ' + readfile[i][0] + ' (Number: ' + str(num) + ')'
    regionfile = open('region_' + readfile[i][0].lower() + '.reg', 'w')
    # generates region files for use in ds9
    regionfile.write('# Region file format: DS9 version 4.1\n'
                     '# Target Name: ' + readfile[i][0].lower() + '\n'
                     'global color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1\n'
                     'fk5\n'
                     'circle(' + str(readfile[i][1]) + ', ' + str(readfile[i][2]) + ', 20.") # width=2\n'
                     'circle(' + str(readfile[i][1]) + ', ' + str(readfile[i][2]) + ', 21.5") # color=red width=2\n'
                     'circle(' + str(readfile[i][1]) + ', ' + str(readfile[i][2]) + ', 37.4") # color=red width=2\n')
    regionfile.close()
    print 'Completed wrighting out region file for current target ' + readfile[i][0] + ' (Number: ' + str(num) + ')'
    os.chdir(workingdir)
