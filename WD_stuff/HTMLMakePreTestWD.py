import os

start = os.path.abspath('.')
ulrs = [x.rsplit()[1] for x in open('plotlyurlsWD.csv', 'rb').readlines()]
indexes = [x.rsplit()[0] for x in open('plotlyurlsWD.csv', 'rb').readlines()]
justchanged = True
targetzone_ind = []
targetzone_use = []
prevzonenum = 0
prev_targ = 'SDSS_' + indexes[0].split('_')[0]
for target in indexes:
    target_check = target.split('_')
    if prev_targ == 'SDSS_' + target_check[0]:
        justchanged = False
        prev_targ = 'SDSS_' + target_check[0]
        zonenum = target_check[-1]
        if int(zonenum) > int(prevzonenum):
            prevzonenum = int(zonenum)
    elif prev_targ != 'SDSS_' + target_check[0] and justchanged is False:
        juctchanged = True
        targetzone_ind.append(prev_targ)
        targetzone_use.append(prevzonenum)
        zonenum = 0
        prevzonenum = 0
        prev_targ = 'SDSS_' + target_check[0]
        zonenum = target_check[-1]
        if int(zonenum) > int(prevzonenum):
            prevzonenum = int(zonenum)
    elif prev_targ != 'SDSS_' + target_check[0] and justchanged is True:
        juctchanged = True
        targetzone_ind.append(prev_targ)
        targetzone_use.append(prevzonenum)
        zonenum = 0
        prevzonenum = 0
        prev_targ = 'SDSS_' + target_check[0]
        zonenum = target_check[-1]
        if zonenum > prevzonenum:
            prevzonenum = zonenum
        targetzone_ind.append('SDSS_' + target_check[0])
        targetzone_use.append(zonenum)
os.chdir('FilesForUse')
working_dir = os.path.abspath('.')
dir = os.listdir('.')
xloc = 0
addon = 'FilesForUse'
# removes hidden files
for x in dir:
    if x[0] == '.':
        dir.pop(xloc)
    else:
        xloc += 1
xloc = 0
numtarg = len(dir)
firstlinkrec = False
firstlink = 'http://www.google.com'
nextlink = 'http://www.google.com'
count = 1
incriment = 'NAN'
prevlink = '../../index.html'
imageforpage = 'NOIMAGEFOUND'
for i in range(numtarg):
    htmlgo = False
    if dir[i] == 'SDSS_204038.41-010215.7':
        print 'GO CHECK'
    alright = False
    onetimefilp = False
    cont = False
    numzones = 0
    pagenum = 0
    pathtox = ['../../../404.png'] * 100
    #try:
    os.chdir(dir[i])
    checkzones = os.listdir('.')
    if dir[i] == 'SDSS_204038.41-010215.7':
        print 'GO CHECK 2'
    for x in checkzones:
        if x[0] == '.':
            checkzones.pop(xloc)
        else:
            xloc += 1
    xloc = 0
    for x in checkzones:
        if '.png' in x and 'ZONE' in x and not '._' in x:
            zonefind = x.find('ZONE')
            try:
                checknum = int(x[zonefind + 5:zonefind + 7])
                pathtox[checknum - 1] = x
            except ValueError:
                checknum = int(x[zonefind + 5])
                pathtox[checknum -1] = x
            if checknum > int(numzones):
                numzones = checknum
            else:
                pass
        elif '.png' in x and 'Count' in x and '._' not in x[0:3]:
            imageforpage = x
    if firstlinkrec is False:
        firstlink = addon + '/' + dir[i] + '/' + dir[i] + 'ViewPage.html'
        firstlinkrec = True
    else:
        pass
    if dir[i] == 'SDSS_204038.41-010215.7':
        print 'GO CHECK 3'
    # if alright is False:
    #    htmlout = open(dir[i] + 'ViewPage.html', 'w')
    try:
        zoneindex = targetzone_ind.index(dir[i])
        if dir[i] == 'SDSS_204038.41-010215.7':
            print zoneindex
    except ValueError:
        os.chdir(working_dir)
        if dir[i] == 'SDSS_204038.41-010215.7':
            print 'continuing'
        continue
    numzones = targetzone_use[zoneindex]
    if dir[i] == 'SDSS_204038.41-010215.7':
        print 'GO CHECK 4'
    for k in range((len(dir) - i) - 1):
        precheckhtml = os.listdir(os.path.abspath('..') + '/' + dir[i + k + 1])
        for x in precheckhtml:
            if '.png' in x and 'ZONE' in x and not '._' in x:
                htmlgo = True
                incriment = k + 1
                cont = True
                break
            else:
                pass
        if cont is True:
            break
        else:
            pass
    if htmlgo is True:
        nextlink = '../../' + addon + '/' + dir[i+incriment] + '/' + dir[i+incriment] + 'ViewPage.html'
    else:
        nextlink = '../../' + addon + '/' + dir[i] + '/' + dir[i] + 'ViewPage.html'
    pagenum += 1
    if dir[i] == 'SDSS_204038.41-010215.7':
        print 'GO CHECK 5'
    URLINDEX = 0
    if htmlgo is True and alright is False:
        htmlout = open(dir[i] + 'ViewPage.html', 'w')
        htmlout.write('<!DOCTYPE html>\n'
                      '<html>\n'
                      '<head>\n'
                      '<title>Summer STScI gPhoton HTML pipleline</title>\n'
                      '</head>\n'
                      '<body>\n'
                      '<h1>STScI Summer internship pipeline | Target ' + dir[i] + '</h1>\n'
                      '<form action="' + nextlink + '">\n'
                      '\t<input type="submit" value="Go To Next Target">\n'
                      '</form>\n'
                      '<form action="' + prevlink + '">\n'
                      '\t<input type="submit" value="Go To Previous Target">\n'
                      '</form>'
                      '<table style = "width:75%">\n')
        if numzones > 1:
            if dir[i] == 'SDSS_204038.41-010215.7':
                print 'Going into the break'
            for p in xrange(0, numzones, 2):
                UI1 = indexes.index(dir[i][5:] + '_ZONE_' + str(p+1))
                if numzones % 2 == 0 or p+1 != numzones:
                    UI2 = indexes.index(dir[i][5:] + '_ZONE_' + str(p+2))
                htmlout.write('<tr>\n')
                #htmlout.write('\t<td><img src="' + pathtox[p] + '" alt="plt", style="width:500px;height:500px;"><a href="' + ulrs[UI1] + '.embed">Left plot</a></td>\n')
                #htmlout.write('\t<td><img src="' + pathtox[p+1] + '" alt="plt", style="width:500px;height:500px;"><a href="' + ulrs[UI2] + '.embed">Right plot</a></td>\n')
                htmlout.write('\t<td><iframe width="650" height="650" frameborder="0" scrolling="no" src="' + ulrs[UI1] + '.embed"></iframe></td>\n')
                if numzones % 2 == 0 or p+1 != numzones:
                    htmlout.write('\t<td><iframe width="650" height="650" frameborder="0" scrolling="no" src="' + ulrs[UI2] + '.embed"></iframe></td>\n')
                #htmlout.write('\t<td><a href="' + ulrs[UI1] + '.embed">Left plot</a><a href="' + ulrs[UI2] + '.embed">Right plot</a></td>>\n')
                htmlout.write('</tr>\n')
        elif numzones == 1:
            UI1 = indexes.index(dir[i] + '_ZONE_1')
            htmlout.write('\t<td><img src="' + pathtox[0] + '" alt="plt", style="width:500px;height:500px;"></td>\n')
            htmlout.write('\t<td><a href="' + ulrs[UI1] + '.embed">Left plot</a>\n')
        htmlout.write('\t<td><img src="' + imageforpage + '" alt="star", style="width:500px;height500px;"></td>\n'
                      '</table>\n'
                      '<h2>Flag Lookup Table</h2>'
                      '<table>\n'
                          '<tr><td>1 - (0 power scale) - Hotspot</td></tr>\n'
                          '<tr><td>2 - (1 power scale) - Mask Edge</td></tr>\n'
                          '<tr><td>4 - (3 power scale) - exptime</td></tr>\n'
                          '<tr><td>8 - (4 power scale) - respose</td></tr>\n'
                          '<tr><td>16 - (5 power scale) - nonlinearity</td></tr>\n'
                          '<tr><td>32 - (6 power scale) - detector edge</td></tr>\n'
                          '<tr><td>64 - (7 power scale) - Backgrond hotspot</td></tr>\n'
                          '<tr><td>128 - (8 power scale) - Backgound mask</td></tr>\n'
                      '</table>\n'
                      '<form action="' + nextlink + '">\n'
                      '\t<input type="submit" value="Go To Next Target">\n'
                      '</form>\n'
                      '<form action="' + prevlink + '">\n'
                      '\t<input type="submit" value="Go To Previous Target">\n'
                      '</form>'
                      '</body>\n'
                      '</html>')
        htmlgo = False
        alright = True
    elif htmlgo is False and alright is False:
        htmlout = open(dir[i] + 'ViewPage.html', 'w')
        alright = True
        htmlout.write('<!DOCTYPE html>\n'
                      '<html>\n'
                      '<head>\n'
                      '<title>Summer STScI gPhoton HTML pipleline</title>\n'
                      '</head>\n'
                      '<body>\n'
                      '<h1>STScI Summer internship pipeline | Target ' + dir[i] + '</h1>\n'
                      '<form action="' + prevlink + '">\n'
                      '\t<input type="submit" value="Go To Previous Target">\n'
                      '</form>\n'
                      '<form action="' + prevlink + '">\n'
                      '\t<input type="submit" value="Go To Previous Target">\n'
                      '</form>'
                      '<table style = "width:75%">\n')
        if numzones > 1:
            if dir[i] == 'SDSS_204038.41-010215.7':
                print 'Going into the break'
            for p in xrange(0, numzones, 2):
                UI1 = indexes.index(dir[i][5:] + '_ZONE_' + str(p+1))
                if numzones % 2 == 0 or p+1 != numzones:
                    UI2 = indexes.index(dir[i][5:] + '_ZONE_' + str(p+2))
                htmlout.write('<tr>\n')
                #htmlout.write('\t<td><img src="' + pathtox[p] + '" alt="plt", style="width:500px;height:500px;"><a href="' + ulrs[UI1] + '.embed">Left plot</a></td>\n')
                #htmlout.write('\t<td><img src="' + pathtox[p+1] + '" alt="plt", style="width:500px;height:500px;"><a href="' + ulrs[UI2] + '.embed">Right plot</a></td>\n')
                htmlout.write('\t<td><iframe width="650" height="650" frameborder="0" scrolling="no" src="' + ulrs[UI1] + '.embed"></iframe></td>\n')
                if numzones % 2 == 0 or p+1 != numzones:
                    htmlout.write('\t<td><iframe width="650" height="650" frameborder="0" scrolling="no" src="' + ulrs[UI2] + '.embed"></iframe></td>\n')
                #htmlout.write('\t<td><a href="' + ulrs[UI1] + '.embed">Left plot</a><a href="' + ulrs[UI2] + '.embed">Right plot</a></td>>\n')
                htmlout.write('</tr>\n')
        elif numzones == 1:
            UI1 = indexes.index(dir[i] + '_ZONE_1')
            htmlout.write('\t<td><img src="' + pathtox[0] + '" alt="plt", style="width:500px;height:500px;"></td>\n')
            htmlout.write('\t<td><a href="' + ulrs[UI1] + '.embed">Left plot</a>\n')
        htmlout.write('\t<td><img src="' + imageforpage + '" alt="star", style="width:500px;height500px;"></td>\n'
                      '</table>\n'
                      '<h2>Flag Lookup Table</h2>'
                      '<table>\n'
                          '<tr><td>1 - (0 power scale) - Hotspot</td></tr>\n'
                          '<tr><td>2 - (1 power scale) - Mask Edge</td></tr>\n'
                          '<tr><td>4 - (3 power scale) - exptime</td></tr>\n'
                          '<tr><td>8 - (4 power scale) - respose</td></tr>\n'
                          '<tr><td>16 - (5 power scale) - nonlinearity</td></tr>\n'
                          '<tr><td>32 - (6 power scale) - detector edge</td></tr>\n'
                          '<tr><td>64 - (7 power scale) - Backgrond hotspot</td></tr>\n'
                          '<tr><td>128 - (8 power scale) - Backgound mask</td></tr>\n'
                      '</table>\n'
                      '<form action="' + prevlink + '">\n'
                      '\t<input type="submit" value="Go To Previous Target">\n'
                      '</form>\n'
                      '<form action="' + prevlink + '">\n'
                      '\t<input type="submit" value="Go To Previous Target">\n'
                      '</form>'
                      '</body>\n'
                      '</html>')
        print 'NOW HERE'
    print 'AND HERE'
    if dir[i] == 'SDSS_204038.41-010215.7':
        print 'about to close'
    htmlout.close()
    if pagenum > 0:
        prevlink = '../../' + addon + '/' + dir[i] + '/' + dir[i] + 'ViewPage.html'
    os.chdir('..')
   # except OSError as e:
   #     print os.path.abspath('.')
   #     print e
   #     print dir[i]
    os.chdir(working_dir)
os.chdir(start)
indexpage = open('index.html', 'w')
indexpage.write('<!DOCTYPE html>\n'
                '<html>\n'
                '<head>\n'
                '<title>WD Summer STScI gPhoton HTML pipleline</title>\n'
                '</head>\n'
                '<body>\n'
                '<h1>WD STScI Summer internship FIRST PAGE</h1>\n'
                '<p>This is currently being created with the prerun script meaning it is in active development, features may not work or may be semi working, thanks for your paitience'
                '<p> Currently there is an issue with the flag system so just ignore the colors, also it cause PG_0016+151 to break, the jackalope is the placeholder and there are some issues, hopefully they will be sorted soon, bye now'
                '<form action="' + firstlink + '">\n'
                '\t<input type="submit" value="Go To First Target">\n'
                '</form>'
                '</body>\n'
                '</html>')
indexpage.close()
