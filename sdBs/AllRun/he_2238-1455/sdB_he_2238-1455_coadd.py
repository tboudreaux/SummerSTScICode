from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[340.409417,-14.660969],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_he_2238-1455/sdB_he_2238-1455_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_he_2238-1455/sdB_he_2238-1455_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
