from gPhoton.gFind import gFind
filename = 'catalogue_sdb_v6.csv'

fileopen = open(filename, 'rb')
fileopen = fileopen.readlines()
numobs = len(fileopen)
modifiedfile = []
usefile = []
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
			modifiedfile[i].append(fileopen[i][j])
		else:
			pass
print numobs, len(usefile), len(modifiedfile)
for i in range(4450):
	usefile[i].append([modifiedfile[i][0], modifiedfile[i][4], modifiedfile[i][5]])
usefile.pop(0)
cont = False
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
	else:
		print 'Please enter either yes or no'
		cont = False
outfile = open('sdBTargOut.csv', 'w')
outfile.close()
for i in range(len(usefile)):
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
	outfile.close()

