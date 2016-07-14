from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[287.104167,45.142222],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kepler_j190825+450832/sdB_kepler_j190825+450832_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kepler_j190825+450832/sdB_kepler_j190825+450832_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
