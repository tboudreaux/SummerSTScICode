from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[143.449667,46.074969],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_US_719/sdB_US_719_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_US_719/sdB_US_719_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
