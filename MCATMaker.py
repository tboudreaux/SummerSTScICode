from gPhoton.gFind import gFind
import os
filename = 'catalogue_sdb_v6.csv'

fileopen = open(filename, 'rb')
fileopen = fileopen.readlines()
numobs = len(fileopen)
modifiedfile = []
usefile = []

# cheating a bit here because of issues with commas, but hardcoded the length of the list in, that is 4450
for i in range(4450):
	fileopen[i] = fileopen[i].split(',')
	# Generate arrays of correct size here
	modifiedfile.append([])
	usefile.append([])
for i in range(4450):
	# parse in file
	fileopen[i][0] = fileopen[i][0] + '_' + fileopen[i][1]
	fileopen[i].pop(1)
	colums = len(fileopen[i])
	for j in range(colums):
		if fileopen[i][j]:
			# remove any /s in starnames as they would mess up folder creation latter on
			fileopen[i][j] = fileopen[i][j].replace('/', '')
			# add only populated cells to the modified file array, removing the many unpopulated cells
			modifiedfile[i].append(fileopen[i][j])
		else:
			pass

# generated a list with only usefull enteries
for i in range(4450):
	try:
		usefile[i].append([modifiedfile[i][0], float(modifiedfile[i][4]), float(modifiedfile[i][5])])
	except ValueError:
		# should only be triggered on the first line, it is then popped latter
		usefile[i].append('ERROR')
# gets rid of header line
usefile.pop(0)
cont = False
overwrite = True
# some user input logig
while cont is False:
	# Debug mode runs with teh first 10 targets in the target file in order to check things whithout taking too much time
	# not running in debug mode will use the enture target file
	debug_mode = raw_input('would you like to run in debug mode[Y/n]: ')
	if debug_mode == 'y' or debug_mode == 'Y':
		usefile = usefile[:10]
		cont = True
	elif debug_mode == 'n' or debug_mode == 'N':
		cont2 = False
		while cont2 is False:
			# check to make sure user wants to not run in debug mode -- also allows user to cancel before file is overwitten in order to backfileup.
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
	# secret mode that allows the user to restart the gFind query at a known loaction in the target file
	# few sanity checks, only indended for my reasonalble use
	elif debug_mode == 'j' or debug_mode == 'J':
		pickup_location = input('Please enter the location to pick up in the search file: ')
		if pickup_location > 1:
			overwrite = False
			usefile = usefile[pickup_location:]
		else:
			print 'Invalid input -- Ignoring and starting at beging'
	else:
		print 'Please enter either yes or no'
		cont = False

#logic controling file overwrite
if overwrite is True:
	outfile = open('sdBTargOut.csv', 'w')
	outfile.close()
	MCATLOG = open('MCAT.log', 'w')
	MCATLOG.close()
else:
	pass
# searches gFind and only pulls out targets with a miniume total integeration time
for i in range(len(usefile)):
	# Data Query Code
	outfile = open('sdBTargOut.csv', 'a')
	MCATLOG = open('MCAT.log', 'a')
	if overwrite is False:
		print 'target number', i + pickup_location
	else:
		print 'targetnumber', i
	gndata = gFind(band='NUV',skypos=[usefile[i][0][1],usefile[i][0][2]],maxgap=100.,minexp=600., exponly=True)
	writefile = str(usefile[i][0][0]) + '\t' + str(usefile[i][0][1]) + '\t' + str(usefile[i][0][2]) + '\t' + str(gndata['NUV']['expt'])
	print writefile

	# checks for MCAT database query in gFind NUV band output
	if 'nearest_source' in gndata['NUV'].keys():
		MCAT_AVAL = True
	else:
		MCAT_AVAL = False
		
	if gndata['NUV']['expt'] > 600:
		outfile.write(str(usefile[i][0][0]) + '\t' + str(usefile[i][0][1]) + '\t' + str(usefile[i][0][2]) + '\t' + str(gndata['NUV']['expt']) + '\n')
		if MCAT_AVAL is True:
			MCATLOG.write(usefile[i][0][0] + '\t' + str(gndata['NUV']['nearest_source']['distance']) + '\t' + str(gndata['NUV']['nearest_source']['skypos'][0])+ '\t' + str(gndata['NUV']['nearest_source']['skypos'][1]) + '\t' + str(gndata['NUV']['nearest_source']['mag']) + '\n')
		else:
			MCATLOG.write(usefile[i][0][0] + '\tN/A\tN/A\tN/A\tN/A\n')
	elif gndata['NUV']['expt'] < 600:
		gfdata = gFind(band='FUV', skypos=[usefile[i][0][1], usefile[i][0][2]], maxgap=100., minexp=600., exponly = True)

		# checks for MCAT database query in gFind FUV band output
		if 'nearest_source' in gfdata['FUV'].keys():
			MCAT_AVAL = True
		else:
			MCAT_AVAL = False
		if gfdata['FUV']['expt'] > 600:
			outfile.write(str(usefile[i][0][0]) + '\t' + str(usefile[i][0][1]) + '\t' + str(usefile[i][0][2]) + '\t' + str(gfdata['FUV']['expt']) + '\n')
			if MCAT_AVAL is True:
				MCATLOG.write(usefile[i][0][0] + '\t' + str(gfdata['FUV']['nearest_source']['distance']) + '\t' + str(gfdata['FUV']['nearest_source']['skypos'][0])+ '\t' + str(gfdata['FUV']['nearest_source']['skypos'][1]) + '\t' + str(gfdata['FUV']['nearest_source']['mag']) + '\n')
			else:
				MCATLOG.write(usefile[i][0][0] + '\tN/A\tN/A\tN/A\tN/A\n')
		else:
			print 'NOT ENOUGH DATA FOR TARGET [' + usefile[i][0][0] + '] SKIPING'
	else:
		pass

	# nessesary file and folder generation code
	os.chdir('sdBs/regionfiles')
	# check if folder already exists, if not generates folder
	try:
		os.chdir(usefile[i][0][0])
	except OSError:
		os.mkdir(usefile[i][0][0])
		os.chdir(usefile[i][0][0])
	regionfile = open('region_' + usefile[i][0][0] + '.reg', 'w')
	# generates region files for use in ds9
	regionfile.write('# Region file format: DS9 version 4.1\n'
			'# Filename: ' + usefile[i][0][0] + '\n'
			'global color=green dashlist=8 3 width=1 font="helvetica 10 normal roman" select=1 highlite=1 dash=0 fixed=0 edit=1 move=1 delete=1 include=1 source=1\n'
			'fk5\n'
			'circle(' + str(usefile[i][0][1]) + ', ' + str(usefile[i][0][2]) + ', 21.") # width=2\n'
			'circle(' + str(usefile[i][0][1]) + ', ' + str(usefile[i][0][2]) + ', 22.5") # color=red width=2\n'
			'circle(' + str(usefile[i][0][1]) + ', ' + str(usefile[i][0][2]) + ', 38.4") # color=red width=2\n')
	regionfile.close()
	# return program to main running directory
	os.chdir('../../..')
	outfile.close()
	MCATLOG.close()

