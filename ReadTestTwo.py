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
	modifiedfile.append([])
	usefile.append([])
for i in range(4450):
	fileopen[i][0] = fileopen[i][0] + '_' + fileopen[i][1]
	fileopen[i].pop(1)
	colums = len(fileopen[i])
	for j in range(colums):
		if fileopen[i][j]:
			fileopen[i][j] = fileopen[i][j].replace('/', '')
			modifiedfile[i].append(fileopen[i][j])
		else:
			pass

# generated a list with only usefull enteries
for i in range(4450):
	try:
		usefile[i].append([modifiedfile[i][0], float(modifiedfile[i][4]), float(modifiedfile[i][5])])
	except ValueError:
		usefile[i].append('ERROR')
usefile.pop(0)
cont = False
overwrite = True
# some user input logig
while cont is False:
	debug_mode = raw_input('would you like to run in debug mode[Y/n]: ')
	if debug_mode == 'y' or debug_mode == 'Y':
		usefile = usefile[:10]
		cont = True
	elif debug_mode == 'n' or debug_mode == 'N':
		cont2 = False
		while cont2 is False:
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
	elif debug_mode == 'j' or debug_mode == 'J':
		pickup_location = input('Please enter the location to pick up in the search file')
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
else:
	pass
# searches gFind and only pulls out targets with a miniume total integeration time
for i in range(len(usefile)):
	# Data Query Code
	outfile = open('sdBTargOut.csv', 'a')
	print 'target number', i
	gndata = gFind(band='NUV',skypos=[usefile[i][0][1],usefile[i][0][2]],maxgap=100.,minexp=600., exponly=True)
	writefile = str(usefile[i][0][0]) + '\t' + str(usefile[i][0][1]) + '\t' + str(usefile[i][0][2]) + '\t' + str(gndata['NUV']['expt'])
	print writefile
	if gndata['NUV']['expt'] > 600:
		outfile.write(str(usefile[i][0][0]) + '\t' + str(usefile[i][0][1]) + '\t' + str(usefile[i][0][2]) + '\t' + str(gndata['NUV']['expt']) + '\n')
	elif gndata['NUV']['expt'] < 600:
		gfdata = gFind(band='FUV', skypos=[usefile[i][0][1], usefile[i][0][2]], maxgap=100., minexp=600., exponly = True)
		if gfdata['FUV']['expt'] > 600:
			outfile.write(str(usefile[i][0][0]) + '\t' + str(usefile[i][0][1]) + '\t' + str(usefile[i][0][2]) + '\t' + str(gfdata['FUV']['expt']) + '\n')
		else:
			print 'NOT ENOUGH DATA FOR TARGET [' + usefile[i][0][0] + '] SKIPING'
	else:
		pass

	# nessesary file generation code
	os.chdir('sdBs/regionfiles')
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
	os.chdir('../../..')
	outfile.close()

