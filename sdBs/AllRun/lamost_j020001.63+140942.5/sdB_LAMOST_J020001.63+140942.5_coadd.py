from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[30.006792,14.161806],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_LAMOST_J020001.63+140942.5/sdB_LAMOST_J020001.63+140942.5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_LAMOST_J020001.63+140942.5/sdB_LAMOST_J020001.63+140942.5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
