from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[20.053792,-55.297756],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_JL_241/sdB_JL_241_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_JL_241/sdB_JL_241_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
