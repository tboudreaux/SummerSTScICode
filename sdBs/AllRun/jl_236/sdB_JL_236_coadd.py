from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[18.527792,-52.733856],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_JL_236/sdB_JL_236_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_JL_236/sdB_JL_236_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
