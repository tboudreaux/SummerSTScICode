from gPhoton.gMap import gMap
from gPhoton.gAperture import gAperture
from gPhoton.gFind import gFind
import matplotlib.pyplot as plt
from gPhoton.gphoton_utils import read_lc
import numpy as np
import os
from datetime import datetime
starttime = datetime.now()
filename = 'HS.csv'

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
		readfile = readfile[:10]
		cont = True
	elif debug_mode == 'n' or debug_mode == 'N':
		cont2 = False
		while cont2 is False:
			# check to make sure user wants to not run in debug mode -- also allows user 
			# 		to cancel before file is overwitten in order to backfileup.
			confirm_fullrun = raw_input('Please confirm that you would like to run an actual run | WARNING THIS MAY TAKE MANY MOONS [Y/n]: ')
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

# flip this bool if you would like to Generate Count maps as well as Light Curves | BE AWARE THIS WILL SIGNIFICANGLY INCREASE DISK USAGE
Map_create = True
App_create = False
# Generator
for i in range(len(readfile)):
	#Light Curve generation
	if overwrite is False:
		num = i + pickup_location + 1
	else:
		num = i + 1
	if App_create is True:
		print 'Beign work on target [' + readfile[i][0] + '] (Number: ' + str(num) + ')'
		os.chdir('sdBs/LCs')
		try:
			os.chdir(readfile[i][0])
		except OSError:
			os.mkdir(readfile[i][0])
			os.chdir(readfile[i][0])
		print 'Begining LC data capture for current target (Number: ' + str(num) + ')'
		gaData = gAperture(band = 'NUV', skypos = [float(readfile[i][1]), float(readfile[i][2])], radius = 0.03, annulus = [0.03, 0.04], stepsz = 10, csvfile = 'GENLC_' + str(readfile[i][0]) + '.csv')
		print 'LC Data Gathered for current target (Number: ' + str(num) + ')'
		readlc = read_lc('GENLC_' + str(readfile[i][0]) + '.csv')
		plt.plot(readlc['t_mean'], readlc['flux_bgsub'], 'ko')
		plt.xlabel('Time(s)')
		plt.ylabel('Flux')
		plt.title(readfile[i][0] + ' LC')
		plt.savefig('GENLC_' + str(readfile[i][0]) + '.pdf')
		plt.close()
		os.chdir('../../..')
		print 'LC Saved for current target (Number: ' + str(num) + ')'
		gaData = None # To clear it from memory, prolly not required but to be safe
	else:
		pass
	# count map generation
	if Map_create is True:
                try:
		    os.chdir('sdBs/HundredRun')
                except OSError:
                    os.mkdir('sdBs/HundredRun')
                    os.chdir('sdBs/HundredRun')
		try:
			os.chdir(readfile[i][0])
		except OSError:
			os.mkdir(readfile[i][0])
			os.chdir(readfile[i][0])
		print 'Beigning Map data capture for current target (Number: ' + str(num) + ')'
		gmData = gMap(band='NUV', skypos = [float(readfile[i][1]), float(readfile[i][2])], skyrange = [0.1, 0.1], cntfile = readfile[i][0]+'Count.fits', coadd = True, overwrite = True)
		print 'Map Data Captured and recorded for current target (Number: ' + str(num) + ')'
                print 'Writing out region file for current target (Number: ' + str(num) + ')'
                regionfile = open('region_' + readfile[i][0] + '.reg', 'w')
                # generates region files for use in ds9
                regionfile.write('# Region file format: DS9 version 4.1\n'
                                 '# Target Name: ' + readfile[i][0] + '\n'
                                 'global color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1\n'
                                 'fk5\n'
                                 'circle(' + str(readfile[i][1]) + ', ' + str(readfile[i][2]) + ', 20.") # width=2\n'
                                 'circle(' + str(readfile[i][1]) + ', ' + str(readfile[i][2]) + ', 21.5") # color=red width=2\n'
                                 'circle(' + str(readfile[i][1]) + ', ' + str(readfile[i][2]) + ', 37.4") # color=red width=2\n')
                regionfile.close()
                print 'Completed wrighting out region file for current target (Number: ' + str(num) + ')'
		os.chdir('../../..')
	else:
		pass
        percent_comp = (float(num)/len(readfile)) * 100
        temptiem = datetime.now()
        elapsedtime = temptiem-starttime
	print 'Completed Data quereies for Target [' + readfile[i][0] + '] Moving to next target | ' + str(percent_comp) + '% completed over ' + str(elapsedtime) + '(s)'

endtime = datetime.now()
print 'Completed Count map and refion file creation for ' + str(len(readfile)) + ' Targets in ' + str(endtime) + ' seconds'
