from gPhoton.gFind import gFind
import os
filename = 'WDList.csv'

fileopen = open(filename, 'rb')
fileopen = fileopen.readlines()
fileopen = [x.rsplit() for x in fileopen[1:]]
MCATLOG = open('MCATWD.log', 'w')

for target_data in fileopen:
    gndata  = gFind(band = 'NUV', skypos=[float(target_data[2]), float(target_data[3])], maxgap=100., minexp=100.)

    if 'nearest_source' in gndata['NUV'].keys():
        MCATLOG.write(str(gndata['NUV']['nearest_source']['mag']) + '\t' + str(gndata['NUV']['nearest_source']['skypos'][0]) + '\t' + str(gndata['NUV']['nearest_source']['skypos'][1]) + '\n')
    else:
        print 'NO MCAT SOURCE'
MCATLOG.close()
numobs = len(fileopen)
modifiedfile = []
usefile = []

