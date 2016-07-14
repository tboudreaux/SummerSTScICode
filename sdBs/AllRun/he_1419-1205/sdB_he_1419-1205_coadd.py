from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[215.509042,-12.32525],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_he_1419-1205/sdB_he_1419-1205_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_he_1419-1205/sdB_he_1419-1205_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
