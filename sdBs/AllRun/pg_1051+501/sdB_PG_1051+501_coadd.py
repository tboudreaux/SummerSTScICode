from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[163.577292,49.833431],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_1051+501/sdB_PG_1051+501_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_1051+501/sdB_PG_1051+501_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
