from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[293.800833,45.928333],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kepler_j19352+4555/sdB_kepler_j19352+4555_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kepler_j19352+4555/sdB_kepler_j19352+4555_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
