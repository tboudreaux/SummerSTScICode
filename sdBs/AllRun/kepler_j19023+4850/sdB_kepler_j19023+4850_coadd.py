from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[285.59125,48.847778],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_kepler_j19023+4850/sdB_kepler_j19023+4850_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_kepler_j19023+4850/sdB_kepler_j19023+4850_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
