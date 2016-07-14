from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[284.029583,43.321944],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_Kepler_J18561+4319/sdB_Kepler_J18561+4319_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_Kepler_J18561+4319/sdB_Kepler_J18561+4319_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
