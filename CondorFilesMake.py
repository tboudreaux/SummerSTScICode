import os
from astropy import units as u
from astropy.coordinates import SkyCoord
filename = 'AllTargets.csv'

readfile = open(filename, 'rb')
readfile = readfile.readlines()
readfile = [x.rsplit() for x in readfile]
addon = 'sdBs/AllRun'
start = os.path.abspath('.')
os.chdir(addon)
working_directory = os.path.abspath('.')
xloc = 0
dir = os.listdir('.')
for x in dir:
    if x[0] == '.':
        dir.pop(xloc)
    else:
        xloc += 1
for i in range(len(readfile)):
    use_parameters = [None] * 5
    shiftto = dir.index(readfile[i][0])
    try: 
        try:
            os.chdir(readfile[i][0])
        except OSError:
            print 'Creating Folder for: ' + str(readfile[i][0])
            os.mkdir(readfile[i][0])
            os.chdir(readfile[i][0])
        checkdir = os.listdir('.')
        Coadd_Condor = open('sdB_' + readfile[i][0] + '_coadd.condor', 'w')
        LC_Condor = open('sdB_' + readfile[i][0] + '_lc.condor', 'w')
        Coadd_SH = open('sdB_' + readfile[i][0] + '_coadd.sh', 'w')
        LC_SH = open('sdB_' + readfile[i][0] + '_lc.sh', 'w')
        Coadd_PY = open('sdB_' + readfile[i][0] + '_coadd.py', 'w')
        LC_PY = open('sdB_' + readfile[i][0] + '_lc.py', 'w')
        regionfile = open('region_' + readfile[i][0] + '.reg')
        regionread = regionfile.readlines()
        regionread = [x.rstrip() for x in regionread]
        size_info = regionread[4:7]
        size_info = [x.replace('circle(', '') for x in size_info]
        size_info = [x.replace(') # width=2', '') for x in size_info]
        size_info = [x.replace(') # color=red width=2', '') for x in size_info]
        size_info = [x.split(',') for x in size_info]
        try:
            c = SkyCoord(size_info[0][0] + ' ' + size_info[0][1], unit=(u.hourangle, u.deg))
        except:
            print '#################'
            print 'INFO: '
            print 'RA: ' + str(size_info[0][0])
            print 'DEC: ' + str(size_info[0][1])
            print 'Star Name: ' + str(readfile[i][0])
            print '#################'
        use_parameters[0] = readfile[i][1]
        use_parameters[1] = readfile[i][2]
        for j in range(3):
            rad = size_info[j][2]
            rad = rad.replace('"', '')
            rad = float(rad)
            rad *= 0.000277778
            use_parameters[j + 2] = rad
        # WRITE OUT COADD CONDOR FILE
        print 'Writing Condor Coadd File for: ' + readfile[i][0]
        Coadd_Condor.write('executable = /data2/fleming/GPHOTON_INPUT/sdBs/CONDOR/sdB_' + readfile[i][0] + '_coadd.sh\n'
                            'output = /data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/CONDOR_OUTPUT/sdB_' + readfile[i][0] + '_coadd.condor_stdout\n'
                            'error = /data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/CONDOR_OUTPUT/sdB_' + readfile[i][0] + '_coadd.condor_stderr\n'
                            'log = /data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/CONDOR_OUTPUT/sdB_' + readfile[i][0] + '_coadd.condor_log\n'
                            'getenv = True\n'
                            'notification = Never\n'
                            'universe = vanilla\n'
                            'queue = 1\n')
        # WRITE OUT THE LC CONDOR FILE
        print 'Writing Condor Light Curve File for: ' + readfile[i][0]
        LC_Condor.write('executable = /data2/fleming/GPHOTON_INPUT/sdBs/CONDOR/sdB_' + readfile[i][0] + '_lc.sh\n'
                            'output = /data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/CONDOR_OUTPUT/sdB_' + readfile[i][0] + '_lc.condor_stdout\n'
                            'error = /data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/CONDOR_OUTPUT/sdB_' + readfile[i][0] + '_lc.condor_stderr\n'
                            'log = /data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/CONDOR_OUTPUT/sdB_' + readfile[i][0] + '_lc.condor_log\n'
                            'getenv = True\n'
                            'notification = Never\n'
                            'universe = vanilla\n'
                            'queue = 1\n')

        # WRITE OUT LC SHELL FILE
        print 'Writing Shell Light Curve File for: ' + readfile[i][0]
        LC_SH.write('#!/bin/tcsh\n'
                    'date\n'
                    'mkdir -p /data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_' + readfile[i][0] + '/\n'
                    'python sdB_' + readfile[i][0] + '_lc.py\n'
                    'date')

        # WRITE OUT COADD SHELL FILE
        print 'Writing Shell Coadd File for: ' + readfile[i][0]
        Coadd_SH.write('#!/bin/tcsh\n'
                    'date\n'
                    'mkdir -p /data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_' + readfile[i][0] + '/\n'
                    'python sdB_' + readfile[i][0] + '_coadd.py\n'
                    'date')

        # WRITE OUT LC PYTHON FILE
        print 'Writing python Light Curve File for: ' + readfile[i][0]
        LC_PY.write('from gPhoton.gAperture import gAperture\n'
                    'def main():\n'
                    '\tgAperture(band="NUV", skypos=[' + str(use_parameters[0]) + ',' + str(use_parameters[1]) + '], stepsz=30., csvfile="/data2/fleming/GPHOTON_OUTPU/LIGHTCURVES/sdBs/sdB_' + readfile[i][0] + '/sdB_' + readfile[i][0] + '_lc.csv", maxgap=1000., overwrite=True, radius=' + str(use_parameters[2]) + ', annulus=[' + str(use_parameters[3]) + ',' +  str(use_parameters[4]) + '], verbose=3)\n'
                    'if __name__ == "__main__":\n'
                    '\tmain()\n')

        # WRITE OUT COADD PYTHON FILE
        print 'Writing python Coadd File for: ' + readfile[i][0]
        Coadd_PY.write('from gPhoton.gMap import gMap\n'
                        'def main():\n'
                        '\tgMap(band="NUV", skypos=[' + str(use_parameters[0]) + ',' + str(use_parameters[1]) + '],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_'+ readfile[i][0] + '/sdB_' + readfile[i][0] + '_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_' + readfile[i][0] + '/sdB_' + readfile[i][0] + '_count_coadd.fits", overwrite=True, verbose=3)\n'
                        'if __name__ == "__main__":\n'
                        '\tmain()\n')
        Coadd_Condor.close()
        LC_Condor.close()
        LC_SH.close()
        Coadd_SH.close()
        LC_PY.close()
        LC_SH.close()
        os.chdir(working_directory)
    except OSError as e:
        print 'ERROR:', e
        os.chdir(working_directory)
