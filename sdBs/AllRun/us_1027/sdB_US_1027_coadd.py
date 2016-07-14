from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[147.729167,46.068139],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_US_1027/sdB_US_1027_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_US_1027/sdB_US_1027_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
