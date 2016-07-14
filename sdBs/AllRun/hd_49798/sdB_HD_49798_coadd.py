from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[102.019542,-44.316247],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_HD_49798/sdB_HD_49798_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_HD_49798/sdB_HD_49798_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
