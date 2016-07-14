from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[173.094542,-25.993692],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_EC_11298-2543/sdB_EC_11298-2543_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_EC_11298-2543/sdB_EC_11298-2543_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
