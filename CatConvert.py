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
			fileopen[i][j] = fileopen[i][j].replace('/', '-')
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

outfile = open('AllTargets.csv', 'w')

for i in range(len(usefile)):
    outfile.write(str(usefile[i][0][0]).lower() + '\t' + str(usefile[i][0][1]) + '\t' + str(usefile[i][0][2]) + '\n')

outfile.close()



