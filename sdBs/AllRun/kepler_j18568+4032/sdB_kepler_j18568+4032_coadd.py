from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[284.20625,40.5475],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kepler_j18568+4032/sdB_kepler_j18568+4032_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kepler_j18568+4032/sdB_kepler_j18568+4032_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
